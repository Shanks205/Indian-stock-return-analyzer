"""Indian Stock Return Analyzer

This script downloads historical stock price data and calculates basic
risk-return metrics used in finance.
"""

from data_loader import download_price_data
from calculations import calculate_performance_metrics
from charts import plot_price_chart, plot_cumulative_return_chart, plot_drawdown_chart
from excel_export import export_metrics_to_excel


def main() -> None:
    """Run the stock return analysis project."""
    ticker = "RELIANCE.NS"
    start_date = "2020-01-01"
    end_date = None

    prices = download_price_data(ticker=ticker, start_date=start_date, end_date=end_date)
    metrics, returns, cumulative_returns, drawdowns = calculate_performance_metrics(prices)

    print("Indian Stock Return Analyzer")
    print("Ticker:", ticker)
    print("\nPerformance Metrics")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")

    plot_price_chart(prices, ticker)
    plot_cumulative_return_chart(cumulative_returns, ticker)
    plot_drawdown_chart(drawdowns, ticker)
    export_metrics_to_excel(metrics, ticker)


if __name__ == "__main__":
    main()
