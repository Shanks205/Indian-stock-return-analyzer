"""Charting functions for the Indian Stock Return Analyzer."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

OUTPUT_DIR = Path("outputs/charts")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def plot_price_chart(prices: pd.Series, ticker: str) -> None:
    """Plot the historical stock price chart."""
    plt.figure(figsize=(10, 5))
    prices.plot(title=f"{ticker} Price Chart")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"{ticker}_price_chart.png")
    plt.close()


def plot_cumulative_return_chart(cumulative_returns: pd.Series, ticker: str) -> None:
    """Plot cumulative return over time."""
    plt.figure(figsize=(10, 5))
    cumulative_returns.plot(title=f"{ticker} Cumulative Return")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"{ticker}_cumulative_return.png")
    plt.close()


def plot_drawdown_chart(drawdowns: pd.Series, ticker: str) -> None:
    """Plot drawdowns, showing how far the stock fell from previous peaks."""
    plt.figure(figsize=(10, 5))
    drawdowns.plot(title=f"{ticker} Drawdown")
    plt.xlabel("Date")
    plt.ylabel("Drawdown")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"{ticker}_drawdown.png")
    plt.close()
