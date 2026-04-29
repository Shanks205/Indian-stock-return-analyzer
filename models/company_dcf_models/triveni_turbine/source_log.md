# Triveni Turbine Source Log

## Purpose

This file records the public-source inputs used for the Triveni Turbine public-source v1 research pack and separates completed v1 inputs from later refresh requirements.

---

## Primary company sources

| Source type | Use in model | Status |
|---|---|---|
| FY25 annual report | Historical revenue, margins, cash flow, balance sheet, order book and export context | Use for historical base and audited reconciliation |
| Quarterly results | FY26 revenue, EBITDA, PAT, order book and margin trends | Used for public-source v1 context |
| Investor presentation / results release | Q3 FY26 revenue, EBITDA, PBT, PAT and outstanding order book | Used for public-source v1 figures |
| Exchange filings | Results, corporate actions, shareholding and dividend updates | Requires periodic refresh |
| Management commentary | Order inflow, exports, aftermarket, margins and working capital | Used for thesis and risk framing |

---

## Public-source data points used in v1

| Data item | Value / interpretation | Source type | Model treatment |
|---|---|---|---|
| Q3 FY26 revenue from operations | ₹624 crore / ₹6.24 billion | Company investor/result disclosure | Supports FY26 revenue run-rate context |
| Q3 FY26 EBITDA | ₹154 crore / ₹1.54 billion | Company investor/result disclosure | Supports margin context |
| Q3 FY26 EBITDA margin | Around 24.6% | Result coverage / implied from EBITDA and revenue | Strong-margin reference, not permanent assumption |
| Q3 FY26 PBT | ₹144 crore / ₹1.44 billion | Company investor/result disclosure | Profitability context |
| Q3 FY26 PAT | ₹91.7 crore / ₹917 million | Company investor/result disclosure | Profitability context |
| Outstanding order book | ₹1,986 crore / ₹19.86 billion | Company investor/result disclosure | Revenue visibility and order-book context |
| 9M FY26 revenue | Around ₹1,501.5 crore | Public result coverage | FY26E base input |
| 9M FY26 EBITDA | Around ₹382.4 crore | Public result coverage | Margin context |
| 9M FY26 PAT | Around ₹247.5 crore | Public result coverage | Profitability context |
| Valuation date | 29 April 2026 | Project standard | Used for model timestamp |

---

## Market data sources to refresh

| Data item | Required source | Status |
|---|---|---|
| Current market price | NSE / BSE / reliable market-data source | Needs date-specific refresh |
| Market capitalization | NSE / BSE / reliable market-data source | Needs date-specific refresh |
| Shares outstanding | Annual report / exchange filings | Needs verification |
| Enterprise value | Market cap + debt - cash | Needs reconciliation |
| Beta | Regression vs Nifty Capital Goods / Nifty 50 | Needs calculation |
| Risk-free rate | India 10-year government bond yield | Refresh before model lock |
| Equity risk premium | Reliable India ERP estimate | Refresh before model lock |
| Order book and order inflow | Company filings / investor presentation | Refresh before final model |
| Export and aftermarket mix | Annual report / investor presentation | Refresh before final model |

---

## Peer data sources

Peer comparison should be refreshed from a consistent source and date for:

- P/E
- EV/EBITDA
- revenue growth
- EBITDA margin
- PAT margin
- ROE
- ROCE
- net cash / debt
- order book
- order inflow growth
- export mix
- aftermarket/service mix
- working-capital days

Suggested peers:

- Thermax
- Siemens India
- ABB India
- Kirloskar Brothers
- TD Power Systems
- Bharat Bijlee

---

## Data-quality classification

Current classification:

```text
Public-Source Complete v1 — audited-data refresh pending
```

The research framework is complete for public-source v1. Future improvement should focus on audited-data refresh, order-book validation, export/aftermarket mix refresh and date-consistent peer numerical validation.

---

## Required before final numerical lock

- FY26 audited annual report reconciliation
- full FY26 cash-flow statement
- exact latest share count
- exact cash and debt balance
- beta regression
- date-consistent peer numerical table
- latest market price timestamp
- order book and order inflow refresh
- export and aftermarket mix update

---

## Source-control note

Every future update should record:

- date of update
- source used
- data item changed
- reason for change
- impact on valuation output
