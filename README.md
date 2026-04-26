# Indian Stock Return Analyzer

A beginner-friendly Python project to analyze Indian stock returns, risk, and performance metrics.

This project is built for finance learning, GitHub portfolio development, and resume demonstration. It connects basic equity analysis concepts with practical Python implementation.

## Project objective

The objective is to download historical stock price data for an Indian listed company and calculate important risk-return metrics used in finance.

The current version analyzes one stock at a time. The default example is:

```text
RELIANCE.NS
```

## Features

- Download stock price data using `yfinance`
- Calculate daily returns
- Calculate cumulative returns
- Calculate annualized return
- Calculate annualized volatility
- Calculate Sharpe ratio
- Calculate maximum drawdown
- Generate price chart
- Generate cumulative return chart
- Generate drawdown chart
- Export performance summary to Excel
- Provide methodology and interview notes

## Tools and libraries

- Python
- pandas
- numpy
- matplotlib
- yfinance
- openpyxl
- GitHub

## Project structure

```text
Indian-stock-return-analyzer/
│
├── README.md
├── AGENTS.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── calculations.py
│   ├── charts.py
│   └── excel_export.py
│
├── docs/
│   ├── methodology.md
│   └── interview_notes.md
│
└── outputs/
    ├── .gitkeep
    └── charts/
```

## Finance concepts covered

### Daily return

Daily return measures the percentage change in stock price from one trading day to the next.

```text
Daily Return = Today's Price / Yesterday's Price - 1
```

### Annualized return

Annualized return estimates the yearly return based on average daily return.

```text
Annualized Return = Average Daily Return × 252
```

### Annualized volatility

Annualized volatility measures yearly risk based on daily return fluctuation.

```text
Annualized Volatility = Standard Deviation of Daily Returns × √252
```

### Sharpe ratio

Sharpe ratio measures return earned per unit of risk.

```text
Sharpe Ratio = Annualized Return / Annualized Volatility
```

### Maximum drawdown

Maximum drawdown measures the worst fall from a previous peak. It helps understand downside risk.

## Outputs generated

When the project is run locally, it generates:

- Price chart
- Cumulative return chart
- Drawdown chart
- Excel performance summary

The Excel file is useful because finance analysts often review and share results in spreadsheet format.

## How to run this project

First install the required Python libraries:

```bash
pip install -r requirements.txt
```

Then run the main script:

```bash
python src/main.py
```

## Important note

This project is for education and portfolio demonstration only. It does not provide investment advice or buy/sell recommendations.

## Future improvements

- Add multiple-stock comparison
- Add benchmark comparison with NIFTY 50
- Add beta and Jensen's alpha
- Add Streamlit dashboard
- Add portfolio-level analysis
- Add technical indicators such as RSI and moving averages

## Resume bullet

Built a Python-based Indian equity analytics tool to calculate annualized return, volatility, Sharpe ratio, cumulative return, and maximum drawdown using historical stock price data, with chart generation and Excel reporting.
