"""Data loading functions for the Indian Stock Return Analyzer."""

import pandas as pd
import yfinance as yf


def download_price_data(ticker: str, start_date: str, end_date: str | None = None) -> pd.Series:
    """Download adjusted closing prices for a stock.

    Parameters
    ----------
    ticker:
        Yahoo Finance ticker. Indian NSE stocks usually end with .NS.
        Example: RELIANCE.NS, TCS.NS, INFY.NS.
    start_date:
        First date for the analysis in YYYY-MM-DD format.
    end_date:
        Last date for the analysis. If None, yfinance uses the latest available date.

    Returns
    -------
    pd.Series
        Adjusted closing prices.
    """
    data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=True, progress=False)

    if data.empty:
        raise ValueError(f"No data found for ticker: {ticker}")

    return data["Close"].dropna()
