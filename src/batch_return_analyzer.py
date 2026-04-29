"""Batch return analyzer for the screener company universe.

This script reads the company universe from data/templates/scenario_inputs_template.csv
and runs stock-return analysis for every ticker in that file.

Important:
- RELIANCE.NS is intentionally excluded.
- The script focuses on return/risk metrics, not buy/sell recommendations.
- Failed tickers are logged instead of stopping the whole batch.

Default output:
    outputs/valuation_summary/return_metrics_summary.csv
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, List

import pandas as pd

from calculations import calculate_performance_metrics
from data_loader import download_price_data


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_UNIVERSE_PATH = PROJECT_ROOT / "data" / "templates" / "scenario_inputs_template.csv"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "outputs" / "valuation_summary" / "return_metrics_summary.csv"
EXCLUDED_TICKERS = {"RELIANCE.NS"}


def load_screener_universe(universe_path: Path = DEFAULT_UNIVERSE_PATH) -> List[Dict[str, str]]:
    """Load tickers and company labels from the screener universe CSV."""
    companies: List[Dict[str, str]] = []

    with universe_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            ticker = str(row.get("ticker", "")).strip().upper()
            if not ticker or ticker in EXCLUDED_TICKERS:
                continue
            companies.append(
                {
                    "ticker": ticker,
                    "company_name": str(row.get("company_name", "")).strip(),
                    "bucket": str(row.get("bucket", "")).strip(),
                }
            )
    return companies


def _latest_price(prices: pd.Series) -> float:
    """Return the latest available closing price as a plain float."""
    latest = prices.dropna().iloc[-1]
    if hasattr(latest, "iloc"):
        latest = latest.iloc[0]
    return float(latest)


def analyze_company(company: Dict[str, str], start_date: str, end_date: str | None) -> Dict[str, str]:
    """Download prices and calculate risk-return metrics for one company."""
    ticker = company["ticker"]
    prices = download_price_data(ticker=ticker, start_date=start_date, end_date=end_date)
    metrics, _, cumulative_returns, _ = calculate_performance_metrics(prices)

    total_return = float(cumulative_returns.iloc[-1]) if not cumulative_returns.empty else 0.0

    return {
        "ticker": ticker,
        "company_name": company["company_name"],
        "bucket": company["bucket"],
        "start_date": start_date,
        "end_date": end_date or "latest_available",
        "latest_price": f"{_latest_price(prices):.2f}",
        "total_return": f"{total_return:.2%}",
        "annualized_return": f"{metrics['Annualized Return']:.2%}",
        "annualized_volatility": f"{metrics['Annualized Volatility']:.2%}",
        "sharpe_ratio": f"{metrics['Sharpe Ratio']:.2f}",
        "maximum_drawdown": f"{metrics['Maximum Drawdown']:.2%}",
        "status": "OK",
        "notes": "Return analysis completed from Yahoo Finance price data",
    }


def failed_company_row(company: Dict[str, str], start_date: str, end_date: str | None, error: Exception) -> Dict[str, str]:
    """Create a consistent output row when a company fails."""
    return {
        "ticker": company["ticker"],
        "company_name": company["company_name"],
        "bucket": company["bucket"],
        "start_date": start_date,
        "end_date": end_date or "latest_available",
        "latest_price": "",
        "total_return": "",
        "annualized_return": "",
        "annualized_volatility": "",
        "sharpe_ratio": "",
        "maximum_drawdown": "",
        "status": "FAILED",
        "notes": str(error),
    }


def run_batch_return_analysis(
    start_date: str = "2020-01-01",
    end_date: str | None = None,
    universe_path: Path = DEFAULT_UNIVERSE_PATH,
    output_path: Path = DEFAULT_OUTPUT_PATH,
) -> None:
    """Run return analysis for every screener company except excluded tickers."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    companies = load_screener_universe(universe_path)
    results: List[Dict[str, str]] = []

    for company in companies:
        try:
            results.append(analyze_company(company, start_date, end_date))
        except Exception as error:  # Keep batch automation running even if one ticker fails.
            results.append(failed_company_row(company, start_date, end_date, error))

    fieldnames = [
        "ticker",
        "company_name",
        "bucket",
        "start_date",
        "end_date",
        "latest_price",
        "total_return",
        "annualized_return",
        "annualized_volatility",
        "sharpe_ratio",
        "maximum_drawdown",
        "status",
        "notes",
    ]

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    completed = sum(1 for row in results if row["status"] == "OK")
    failed = sum(1 for row in results if row["status"] == "FAILED")
    print(f"Batch return analysis complete. Completed: {completed}. Failed: {failed}.")
    print(f"Results saved to: {output_path}")


if __name__ == "__main__":
    run_batch_return_analysis()
