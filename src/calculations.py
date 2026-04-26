"""Financial calculation functions for the Indian Stock Return Analyzer."""

import numpy as np
import pandas as pd

TRADING_DAYS_PER_YEAR = 252


def calculate_performance_metrics(prices: pd.Series) -> tuple[dict[str, float], pd.Series, pd.Series, pd.Series]:
    """Calculate basic stock performance metrics.

    Metrics explained simply:
    - Daily return: percentage change in price from one trading day to the next.
    - Annualized return: estimated yearly return based on daily average return.
    - Annualized volatility: estimated yearly risk based on daily return fluctuation.
    - Sharpe ratio: return earned per unit of risk, assuming 0% risk-free rate for simplicity.
    - Maximum drawdown: worst percentage fall from a previous peak.
    """
    daily_returns = prices.pct_change().dropna()
    cumulative_returns = (1 + daily_returns).cumprod() - 1

    annualized_return = daily_returns.mean() * TRADING_DAYS_PER_YEAR
    annualized_volatility = daily_returns.std() * np.sqrt(TRADING_DAYS_PER_YEAR)

    if annualized_volatility == 0:
        sharpe_ratio = 0.0
    else:
        sharpe_ratio = annualized_return / annualized_volatility

    wealth_index = (1 + daily_returns).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks) / previous_peaks
    maximum_drawdown = drawdowns.min()

    metrics = {
        "Annualized Return": annualized_return,
        "Annualized Volatility": annualized_volatility,
        "Sharpe Ratio": sharpe_ratio,
        "Maximum Drawdown": maximum_drawdown,
    }

    return metrics, daily_returns, cumulative_returns, drawdowns
