# Methodology

## Project objective

The objective of this project is to analyze the historical performance of an Indian listed stock using Python.

The project calculates basic risk-return metrics that are commonly used in equity analysis and portfolio management.

## Data source

The project uses Yahoo Finance through the `yfinance` Python library.

Indian NSE tickers usually use the `.NS` suffix.

Examples:

- `RELIANCE.NS`
- `TCS.NS`
- `INFY.NS`

## Metrics calculated

### Daily return

Daily return measures the percentage change in stock price from one trading day to the next.

Formula:

```text
Daily Return = Today's Price / Yesterday's Price - 1
```

### Annualized return

Annualized return estimates the yearly return based on average daily return.

Formula:

```text
Annualized Return = Average Daily Return × 252
```

252 is commonly used because there are approximately 252 trading days in a year.

### Annualized volatility

Annualized volatility measures how much the stock return fluctuates in a year.

Formula:

```text
Annualized Volatility = Standard Deviation of Daily Returns × √252
```

Higher volatility means higher price fluctuation or risk.

### Sharpe ratio

Sharpe ratio measures return per unit of risk.

For simplicity, this beginner version assumes a 0% risk-free rate.

Formula:

```text
Sharpe Ratio = Annualized Return / Annualized Volatility
```

### Maximum drawdown

Maximum drawdown measures the worst fall from a previous peak.

It helps understand downside risk.

Example:

If a stock rises to ₹100 and then falls to ₹70, the drawdown is -30%.

## Limitations

- This project is for education and portfolio demonstration only.
- It does not provide buy/sell recommendations.
- It uses historical price data only.
- It does not include dividends, taxes, transaction costs, or fundamental analysis.
- The risk-free rate is assumed to be 0% in the first version.

## Future improvements

- Add multiple-stock comparison.
- Add benchmark comparison with NIFTY 50.
- Add beta and alpha calculation.
- Add Excel export.
- Add Streamlit dashboard.
- Add portfolio-level analysis.
