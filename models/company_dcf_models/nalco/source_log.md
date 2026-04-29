# NALCO Source Log

## Purpose

This file records the public-source inputs used for the NALCO public-source v1 research pack and separates completed v1 inputs from later refresh requirements.

---

## Primary company sources

| Source type | Use in model | Status |
|---|---|---|
| FY25 annual report | FY25 revenue, profit, balance-sheet and operating context | Used for v1 framework |
| Quarterly results | FY26 revenue, profit and margin trend | Used for v1 normalization logic |
| Press releases | Record quarterly performance and operational commentary | Used for v1 summary |
| Investor presentation | Segment mix, capex and strategic priorities | Use latest available version |
| Exchange filings | Results, corporate actions, shareholding and dividend updates | Requires periodic refresh |

---

## Public-source data points used in v1

| Data item | Value / interpretation | Source type | Model treatment |
|---|---|---|---|
| FY25 net sales | Around ₹16,787.6 crore | Annual-report / financial data reference | Shows strong recent revenue base |
| FY25 PAT | Around ₹5,324.7 crore | Annual-report / financial data reference | Shows strong recent profitability |
| Q3 FY26 net profit | Around ₹1,601 crore | Company result communication | Supports strong FY26 profitability context |
| Q3 FY26 total income | Around ₹4,925 crore | Company result communication | Supports FY26 run-rate context |
| 9M FY26 revenue from operations | Around ₹12,830 crore | Company result communication | Used as FY26E base input |
| 9M FY26 net profit | Around ₹4,098 crore | Company result communication | Used for profitability context |
| Spot price reference | Around ₹437–₹440 | Market quote reference for 29 Apr 2026 | Used as valuation-date reference |
| Market cap reference | Around ₹80,000+ crore | Market quote reference | Needs date-specific refresh |
| Risk-free rate | India 10-year government bond yield | Project-wide WACC input | Refresh before model lock |
| India ERP | India equity risk premium estimate | Project-wide WACC input | Refresh before model lock |

---

## Market data sources to refresh

| Data item | Required source | Status |
|---|---|---|
| Current market price | NSE / BSE / reliable market-data source | Needs date-specific refresh |
| Market capitalization | NSE / BSE / reliable market-data source | Needs date-specific refresh |
| Shares outstanding | Annual report / exchange filings | Needs verification |
| Enterprise value | Market cap + debt - cash | Needs reconciliation |
| Beta | Regression vs Nifty Metal / Nifty 50 | Needs calculation |
| Risk-free rate | India 10-year government bond yield | Refresh before model lock |
| Equity risk premium | Reliable India ERP estimate | Refresh before model lock |

---

## Peer data sources

Peer comparison should be refreshed from a consistent source and date for:

- P/E
- EV/EBITDA
- EBITDA margin
- PAT margin
- ROE
- ROCE
- net cash / debt
- dividend yield
- revenue growth
- commodity exposure
- capex pipeline

Suggested peers:

- Hindalco Industries
- Vedanta
- Hindustan Zinc
- NMDC
- Coal India
- global aluminium producers where available

---

## Data-quality classification

Current classification:

```text
Public-Source Complete v1 — audited-data refresh pending
```

The research framework is complete for public-source v1. Future improvement should focus on audited-data refresh and date-consistent peer numerical validation.

---

## Required before final numerical lock

- FY26 audited annual report reconciliation
- full FY26 cash-flow statement
- exact latest share count
- exact cash and debt balance
- beta regression
- date-consistent peer numerical table
- latest market price timestamp

---

## Source-control note

Every future update should record:

- date of update
- source used
- data item changed
- reason for change
- impact on valuation output
