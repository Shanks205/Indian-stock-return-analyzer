# Sharda Cropchem Source Log

## Purpose

This file records the public-source inputs used for the Sharda Cropchem public-source v1 research pack and separates completed v1 inputs from later refresh requirements.

---

## Primary company sources

| Source type | Use in model | Status |
|---|---|---|
| FY25 annual report | Historical revenue, margins, cash flow, working capital and balance-sheet context | Use for historical base and audited reconciliation |
| Quarterly results | FY26 revenue, EBITDA, PAT, margin and segment/geography trends | Used for public-source v1 context |
| Investor presentation | Product registrations, geography mix, strategy and working-capital commentary | Use latest available version |
| Exchange filings | Results, corporate actions, shareholding and dividend updates | Requires periodic refresh |
| Management commentary | Demand, product mix, Europe growth, input costs and channel inventory | Used for v1 qualitative interpretation |

---

## Public-source data points used in v1

| Data item | Value / interpretation | Source type | Model treatment |
|---|---|---|---|
| Q3 FY26 revenue | ₹1,288.8 crore | Public result coverage / company results | Supports FY26 recovery run-rate |
| Q3 FY26 EBITDA | ₹245.5 crore | Public result coverage / company results | Supports margin recovery context |
| Q3 FY26 EBITDA margin | 19.1% | Public result coverage / company results | Used as strong-quarter margin reference, not permanent assumption |
| Q3 FY26 PAT | ₹145.1 crore | Public result coverage / company results | Supports profit recovery context |
| 9M FY26 revenue | ₹3,202.7 crore | Public result coverage / company results | Used as FY26E base input |
| 9M FY26 PAT | ₹362.3 crore | Public result coverage / company results | Used for profitability context |
| Europe contribution | Important Q3 FY26 growth driver | Management commentary / result coverage | Used in growth-driver section |
| Input-cost stabilization | Margin-support factor | Management commentary / result coverage | Used in margin-normalization discussion |
| Valuation date | 29 April 2026 | Project standard | Used for model timestamp |

---

## Market data sources to refresh

| Data item | Required source | Status |
|---|---|---|
| Current market price | NSE / BSE / reliable market-data source | Needs date-specific refresh |
| Market capitalization | NSE / BSE / reliable market-data source | Needs date-specific refresh |
| Shares outstanding | Annual report / exchange filings | Needs verification |
| Enterprise value | Market cap + debt - cash | Needs reconciliation |
| Beta | Regression vs Nifty / chemical or agrochemical peer index | Needs calculation |
| Risk-free rate | India 10-year government bond yield | Refresh before model lock |
| Equity risk premium | Reliable India ERP estimate | Refresh before model lock |
| Working-capital days | Annual report / quarterly balance sheet | Needs refresh |

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
- working-capital days
- R&D / registration intensity
- geography mix

Suggested peers:

- UPL
- PI Industries
- Sumitomo Chemical India
- Rallis India
- Dhanuka Agritech
- Bharat Rasayan

---

## Data-quality classification

Current classification:

```text
Public-Source Complete v1 — audited-data refresh pending
```

The research framework is complete for public-source v1. Future improvement should focus on audited-data refresh, working-capital validation and date-consistent peer numerical validation.

---

## Required before final numerical lock

- FY26 audited annual report reconciliation
- full FY26 cash-flow statement
- exact latest share count
- exact cash and debt balance
- beta regression
- date-consistent peer numerical table
- latest market price timestamp
- working-capital days refresh

---

## Source-control note

Every future update should record:

- date of update
- source used
- data item changed
- reason for change
- impact on valuation output
