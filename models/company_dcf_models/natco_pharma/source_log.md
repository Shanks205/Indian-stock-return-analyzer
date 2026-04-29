# Natco Pharma Source Log

## Purpose

This file records the public-source inputs used for the Natco Pharma public-source v1 research pack and separates completed v1 inputs from later refresh requirements.

---

## Primary company sources

| Source type | Use in model | Status |
|---|---|---|
| FY25 annual report | FY25 revenue, EBITDA, PAT, ROE, ROCE, balance-sheet context | Used for v1 framework |
| Quarterly results | FY26 quarterly revenue, EBITDA, PAT, margin trend | Used for v1 normalization logic |
| Investor presentation | Product pipeline, segment commentary, management priorities | Use latest available version |
| Exchange filings | Results, demerger/restructuring, shareholding, corporate actions | Requires periodic refresh |
| Earnings commentary | Management discussion on exports, domestic, pipeline and capex | Use latest available commentary |

---

## Public-source data points used in v1

| Data item | Value / interpretation | Source type | Model treatment |
|---|---|---|---|
| FY25 total revenue | INR 47,840 million | Annual report | Shows peak year / high profitability base |
| FY25 EBITDA | INR 25,505 million | Annual report | Used to identify peak margin risk |
| FY25 EBITDA margin | 53.3% | Annual report | Not treated as permanent long-run margin |
| FY25 PAT | INR 18,834 million | Annual report | Used for profitability context |
| FY25 ROE | 24.7% | Annual report | Business-quality context |
| FY25 ROCE | 30.1% | Annual report | Capital-efficiency context |
| Q3 FY26 revenue | Around INR 7,054 million | Quarterly results | Shows normalization vs FY25 / Q2 FY26 |
| Q3 FY26 PAT | Around INR 1,513 million | Quarterly results | Supports conservative base-case reset |
| Net cash profile | Strong net cash / investments | Public financial data | Added separately to equity value in DCF |
| Valuation date | 29 April 2026 | Project standard | Used for model timestamp |

---

## Market data sources to refresh

| Data item | Required source | Status |
|---|---|---|
| Current market price | NSE / BSE / reliable market-data source | Needs date-specific refresh |
| Market capitalization | NSE / BSE / reliable market-data source | Needs date-specific refresh |
| Shares outstanding | Annual report / exchange filings | Needs verification |
| Enterprise value | Market cap + debt - cash/investments | Needs reconciliation |
| Beta | Regression vs Nifty Pharma / Nifty 50 | Needs calculation |
| India risk-free rate | India 10-year government bond yield | Refresh before model lock |
| Equity risk premium | Reliable India ERP estimate | Refresh before model lock |

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
- R&D intensity
- export/domestic mix

Suggested peers:

- Divi's Laboratories
- Laurus Labs
- Granules India
- Ajanta Pharma
- IPCA Laboratories
- Sun Pharma as large-cap reference

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
- exact cash, debt, and investment balance
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
