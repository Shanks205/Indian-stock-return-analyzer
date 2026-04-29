# Time Technoplast Source Log

## Purpose

This file records the public-source inputs used for the Time Technoplast public-source v1 research pack and separates completed v1 inputs from later refresh requirements.

---

## Primary company sources

| Source type | Use in model | Status |
|---|---|---|
| FY25 annual report | Historical revenue, margins, cash flow, working capital, debt and product mix | Use for historical base and audited reconciliation |
| Quarterly results | FY26 revenue, EBITDA, PAT, margin and segment trends | Used for public-source v1 context |
| Investor presentation | Value-added product mix, composite cylinders, IBCs, capex and debt reduction | Used for v1 qualitative interpretation |
| Exchange filings | Results, corporate actions, shareholding and dividend updates | Requires periodic refresh |
| Management commentary | Demand, product mix, margins, raw material and working capital | Used for thesis and risk framing |

---

## Public-source data points used in v1

| Data item | Value / interpretation | Source type | Model treatment |
|---|---|---|---|
| Q3 FY26 total income | ₹1,567.1 crore | Public result coverage / company presentation | Supports FY26 revenue run-rate context |
| Q3 FY26 EBITDA | ₹235.8 crore | Public result coverage / company presentation | Supports margin context |
| Q3 FY26 EBITDA margin | Around 15.0% | Public result coverage / company presentation | Used as improved-margin reference |
| Q3 FY26 PAT | ₹126.3 crore | Public result coverage / company presentation | Supports profitability context |
| 9M FY26 total income | ₹4,432.8 crore | Public result coverage / company presentation | Used as FY26E base input |
| 9M FY26 EBITDA | ₹655.4 crore | Public result coverage / company presentation | Used for profitability context |
| 9M FY26 PAT | ₹336.9 crore | Public result coverage / company presentation | Used for profitability context |
| Value-added product growth | Faster than established product growth | Company presentation / result commentary | Used in growth-driver section |
| Valuation date | 29 April 2026 | Project standard | Used for model timestamp |

---

## Market data sources to refresh

| Data item | Required source | Status |
|---|---|---|
| Current market price | NSE / BSE / reliable market-data source | Needs date-specific refresh |
| Market capitalization | NSE / BSE / reliable market-data source | Needs date-specific refresh |
| Shares outstanding | Annual report / exchange filings | Needs verification |
| Enterprise value | Market cap + debt - cash | Needs reconciliation |
| Beta | Regression vs Nifty / packaging or industrial peers | Needs calculation |
| Risk-free rate | India 10-year government bond yield | Refresh before model lock |
| Equity risk premium | Reliable India ERP estimate | Refresh before model lock |
| Working-capital days | Annual report / quarterly balance sheet | Needs refresh |
| Segment/product mix | Investor presentation / annual report | Refresh before final model |

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
- net debt / equity
- working-capital days
- value-added product mix
- capex intensity

Suggested peers:

- Mold-Tek Packaging
- EPL Limited
- Supreme Industries
- Nilkamal
- TPL Plastech
- Hitech Corporation

---

## Data-quality classification

Current classification:

```text
Public-Source Complete v1 — audited-data refresh pending
```

The research framework is complete for public-source v1. Future improvement should focus on audited-data refresh, working-capital validation, value-added product mix refresh and date-consistent peer numerical validation.

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
- value-added product mix update

---

## Source-control note

Every future update should record:

- date of update
- source used
- data item changed
- reason for change
- impact on valuation output
