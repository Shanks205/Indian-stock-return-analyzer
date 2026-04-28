# Indian Equity Valuation Lab

A practical Python and Excel-based equity research project for Indian listed companies, combining stock-return analysis, fundamental screening, Piotroski F-Score, discounted cash flow valuation, WACC stress testing, margin-of-safety rules, and barbell portfolio construction.

This repository started as a beginner-friendly Indian stock return analyzer. It is now being expanded into a full equity valuation lab suitable for finance learning, GitHub portfolio development, interview discussion, and future research-paper development.

> This project is for education, research, and portfolio demonstration only. It is not investment advice or a buy/sell recommendation.

---

## Project objective

The objective is to build a repeatable analyst-style framework for evaluating Indian equities.

The project aims to answer:

> Can a disciplined framework combining accounting quality, intrinsic valuation, margin of safety, and portfolio-fit rules improve Indian equity selection compared with simple return analysis?

The final project will move from raw market data to a structured investment research output:

```text
Stock universe
→ Fundamental screening
→ Piotroski F-Score
→ Historical financial analysis
→ DCF valuation
→ Scenario and sensitivity analysis
→ Margin-of-safety decision
→ Portfolio-fit score
→ Analyst-style research summary
```

---

## Why this project matters

This project is designed to demonstrate skills relevant to:

- Financial analysis
- Equity research
- Investment banking
- Portfolio analytics
- Fundamental valuation
- Python-based financial modeling
- Excel-based valuation modeling
- Research documentation

It connects practical finance concepts with Python implementation and analyst-style reporting.

---

## Current status

### Completed foundation

- Historical stock price download using `yfinance`
- Daily returns
- Cumulative returns
- Annualized return
- Annualized volatility
- Sharpe ratio
- Maximum drawdown
- Charts
- Excel export
- Beginner-friendly methodology notes

### New valuation-lab extension

The project is now being expanded with:

- Piotroski F-Score module
- FCFF DCF model skeleton
- Equity valuation methodology
- Research pipeline documentation
- Investment banking-style project blueprint

---

## Initial company universe

The first research universe follows a barbell framework: core value/quality companies plus selective growth companies.

### Core value / quality candidates

- Hero MotoCorp
- Natco Pharma
- NALCO
- Hindustan Zinc
- CPCL
- Sharda Cropchem

### Growth / satellite candidates

- Fiem Industries
- Time Technoplast
- Force Motors
- Triveni Turbine

Hero MotoCorp and Fiem Industries have already been analysed in first-pass Excel DCF models outside this repository. The next step is to standardize those models inside the repository workflow.

---

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
│   ├── excel_export.py
│   ├── piotroski_score.py
│   └── dcf_model.py
│
├── docs/
│   ├── methodology.md
│   ├── interview_notes.md
│   ├── equity_valuation_lab_blueprint.md
│   ├── valuation_methodology.md
│   └── research_pipeline.md
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── company_dcf_models/
│
├── outputs/
│   ├── .gitkeep
│   ├── charts/
│   └── valuation_summary/
│
└── paper/
    └── ssrn_working_paper_draft/
```

Some folders may be added gradually as the project develops.

---

## Core modules

### 1. Stock return analyzer

The original project calculates:

- daily returns
- cumulative returns
- annualized return
- annualized volatility
- Sharpe ratio
- maximum drawdown
- price chart
- cumulative return chart
- drawdown chart
- Excel performance summary

### 2. Piotroski F-Score module

`src/piotroski_score.py` calculates the 9-point Piotroski F-Score using profitability, leverage/liquidity, and operating-efficiency signals.

The score is based on:

1. Positive net income
2. Positive operating cash flow
3. Improving ROA
4. Operating cash flow greater than net income
5. Lower leverage
6. Improving current ratio
7. No equity dilution
8. Improving gross margin
9. Improving asset turnover

### 3. DCF valuation module

`src/dcf_model.py` provides a reusable free cash flow to firm valuation skeleton.

The model estimates:

- projected FCFF
- present value of forecast cash flows
- terminal value
- enterprise value
- equity value
- intrinsic value per share

---

## Valuation methodology

The project uses FCFF DCF valuation for non-financial companies.

### FCFF formula

```text
FCFF = EBIT × (1 - Tax Rate) + Depreciation and Amortization - Capital Expenditure - Change in Net Working Capital
```

### WACC framework

```text
WACC = Cost of Equity × Equity Weight + After-tax Cost of Debt × Debt Weight
```

Cost of equity is estimated using:

```text
Cost of Equity = Risk-free Rate + Beta × Equity Risk Premium + Company-specific Risk Premium
```

### Terminal value

```text
Terminal Value = Final Year FCFF × (1 + Terminal Growth) / (WACC - Terminal Growth)
```

---

## Analyst checks added to every valuation

Each company valuation should include:

- historical financial analysis
- source log
- assumption log
- WACC build-up
- base, bear, and bull scenarios
- WACC vs terminal-growth sensitivity
- margin-of-safety calculation
- risk-regime check
- AI attention-bias check
- governance check
- cash-conversion check
- portfolio-fit conclusion

---

## Future research-paper direction

This project may later be converted into a working paper for SSRN.

Possible paper title:

> From Screening to Intrinsic Value: A Practical Fundamental Research Framework for Indian Stocks

Possible research themes:

- DCF-implied undervaluation in Indian equities
- Piotroski F-Score as a quality filter before valuation
- Margin of safety and portfolio construction
- Barbell strategy combining value and growth stocks
- Risk-regime and WACC stress testing in Indian equity valuation

---

## How to run the current project

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

Run the original return analyzer:

```bash
python src/main.py
```

Run the Piotroski module demo:

```bash
python src/piotroski_score.py
```

Run the DCF module demo:

```bash
python src/dcf_model.py
```

---

## Tools and libraries

- Python
- pandas
- numpy
- matplotlib
- yfinance
- openpyxl
- Excel
- GitHub

---

## Disclaimer

This repository is for education, research, and portfolio demonstration only. It does not provide investment advice, financial advice, or buy/sell recommendations. All valuation outputs depend heavily on assumptions and must be independently verified before use.
