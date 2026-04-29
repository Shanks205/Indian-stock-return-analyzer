# Hindustan Zinc Source Log

## Purpose

This file records the public-source inputs used for the Hindustan Zinc public-source v1 research pack and separates completed v1 inputs from later refresh requirements.

---

## Primary company sources

| Source type | Use in model | Status |
|---|---|---|
| FY25 annual report | Full-year revenue, profit, balance-sheet and operating context | Use for historical base and audited reconciliation |
| Quarterly results | FY26 revenue, profit, margin and volume trends | Used for public-source v1 context |
| Press releases | Current quarterly performance and operational commentary | Used for v1 summary |
| Investor presentation | Metal mix, mine life, capex and strategic priorities | Use latest available version |
| Exchange filings | Results, corporate actions, shareholding and dividend updates | Requires periodic refresh |

---

## Public-source data points used in v1

| Data item | Value / interpretation | Source type | Model treatment |
|---|---|---|---|
| Q3 FY26 revenue from operations | Around ₹10,627 crore | Public result coverage / company result communication | Supports FY26 revenue run-rate context |
| Q3 FY26 net profit | Around ₹3,916 crore | Public result coverage / company result communication | Supports strong profitability context |
| Q3 FY26 YoY profit growth | Around 46% | Public result coverage | Indicates strong metal-cycle support |
| FY26 earnings support | Zinc and silver price strength | Public metals-market/result commentary | Used as commodity-cycle context |
| Spot price reference | Around ₹570–₹580 range | Market quote reference around late April 2026 | Used as valuation-date reference |
| Market cap reference | Around ₹2.4 lakh crore | Market quote approximation | Needs date-specific refresh |
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
| Zinc / silver price deck | LME / commodity data source | Refresh before model lock |

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
- zinc/silver exposure
- capex pipeline

Suggested peers:

- NALCO
- Vedanta
- Hindalco Industries
- NMDC
- Coal India
- global zinc/silver producers where available

---

## Data-quality classification

Current classification:

```text
Public-Source Complete v1 — audited-data refresh pending
```

The research framework is complete for public-source v1. Future improvement should focus on audited-data refresh, commodity-price deck validation and date-consistent peer numerical validation.

---

## Required before final numerical lock

- FY26 audited annual report reconciliation
- full FY26 cash-flow statement
- exact latest share count
- exact cash and debt balance
- beta regression
- date-consistent peer numerical table
- latest market price timestamp
- zinc/silver commodity price deck

---

## Source-control note

Every future update should record:

- date of update
- source used
- data item changed
- reason for change
- impact on valuation output
