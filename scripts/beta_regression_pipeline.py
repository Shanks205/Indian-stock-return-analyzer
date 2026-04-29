"""Beta regression pipeline for the Indian Equity Valuation Lab.

Purpose:
- calculate regression beta for each covered company
- use a consistent benchmark and lookback window
- export a beta table for WACC refresh

This script is intentionally reproducible and transparent. It does not hardcode
final beta values into the research notes.

Requirements:
    pip install yfinance pandas numpy openpyxl

Example:
    python scripts/beta_regression_pipeline.py
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

OUTPUT_DIR = Path("outputs/valuation_summary")
OUTPUT_FILE = OUTPUT_DIR / "beta_regression_output.xlsx"

DEFAULT_BENCHMARK = "^NSEI"
DEFAULT_PERIOD = "5y"
DEFAULT_INTERVAL = "1wk"


@dataclass
class BetaInput:
    company: str
    ticker: str
    benchmark: str = DEFAULT_BENCHMARK
    period: str = DEFAULT_PERIOD
    interval: str = DEFAULT_INTERVAL


COMPANY_BETAS = [
    BetaInput("Hero MotoCorp", "HEROMOTOCO.NS", "^NSEI"),
    BetaInput("Natco Pharma", "NATCOPHARM.NS", "^NSEI"),
    BetaInput("NALCO", "NATIONALUM.NS", "^NSEI"),
    BetaInput("Hindustan Zinc", "HINDZINC.NS", "^NSEI"),
    BetaInput("CPCL", "CHENNPETRO.NS", "^NSEI"),
    BetaInput("Sharda Cropchem", "SHARDACROP.NS", "^NSEI"),
    BetaInput("Fiem Industries", "FIEMIND.NS", "^NSEI"),
    BetaInput("Time Technoplast", "TIMETECHNO.NS", "^NSEI"),
    BetaInput("Force Motors", "FORCEMOT.NS", "^NSEI"),
    BetaInput("Triveni Turbine", "TRITURBINE.NS", "^NSEI"),
]


def download_adjusted_close(ticker: str, period: str, interval: str) -> pd.Series:
    data = yf.download(ticker, period=period, interval=interval, auto_adjust=True, progress=False)
    if data.empty:
        raise ValueError(f"No data returned for {ticker}")
    if isinstance(data.columns, pd.MultiIndex):
        close = data["Close"].iloc[:, 0]
    else:
        close = data["Close"]
    close.name = ticker
    return close.dropna()


def calculate_beta(stock_returns: pd.Series, benchmark_returns: pd.Series) -> tuple[float, float, int]:
    returns = pd.concat([stock_returns, benchmark_returns], axis=1).dropna()
    if len(returns) < 30:
        raise ValueError("Not enough overlapping return observations for beta regression")
    stock = returns.iloc[:, 0]
    benchmark = returns.iloc[:, 1]
    covariance = np.cov(stock, benchmark, ddof=1)[0, 1]
    variance = np.var(benchmark, ddof=1)
    beta = covariance / variance
    correlation = stock.corr(benchmark)
    r_squared = correlation ** 2
    return float(beta), float(r_squared), int(len(returns))


def run_beta_pipeline(inputs: list[BetaInput]) -> pd.DataFrame:
    rows = []
    for item in inputs:
        stock_close = download_adjusted_close(item.ticker, item.period, item.interval)
        benchmark_close = download_adjusted_close(item.benchmark, item.period, item.interval)
        stock_returns = stock_close.pct_change().dropna()
        benchmark_returns = benchmark_close.pct_change().dropna()
        beta, r_squared, observations = calculate_beta(stock_returns, benchmark_returns)
        rows.append({
            "Company": item.company,
            "Ticker": item.ticker,
            "Benchmark": item.benchmark,
            "Period": item.period,
            "Interval": item.interval,
            "Beta": beta,
            "R-squared": r_squared,
            "Observations": observations,
            "Status": "Calculated",
            "Use in WACC": "Review before final valuation lock",
        })
    return pd.DataFrame(rows)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    result = run_beta_pipeline(COMPANY_BETAS)
    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
        result.to_excel(writer, sheet_name="Beta Regression", index=False)
    print(f"Saved {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
