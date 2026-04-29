# Fiem Industries Source Log

## Purpose

This file records the public-source inputs used for the Fiem Industries public-source v1 research pack and separates completed v1 inputs from later refresh requirements.

---

## Primary company sources

| Source type | Use in model | Status |
|---|---|---|
| FY25 annual report | Historical revenue, margins, cash flow, balance sheet, customer and segment context | Use for historical base and audited reconciliation |
| Quarterly results | FY26 revenue, PAT, margin and segment/customer trends | Used for public-source v1 context |
| Investor presentation | Product mix, customer mix, two-wheeler exposure, EV/LED strategy | Used for v1 qualitative interpretation |
| Exchange filings | Results, corporate actions, shareholding and dividend updates | Requires periodic refresh |
| Management commentary | Demand, customer mix, margin trend, auto-cycle conditions | Used for thesis and risk framing |

---

## Public-source data points used in v1

| Data item | Value / interpretation | Source type | Model treatment |
|---|---|---|---|
| Q3 FY26 total income | Around ₹695.01 crore | Public result coverage | Supports FY26 revenue run-rate context |
| Q3 FY26 net sales | Around ₹685.81 crore | Public result coverage | Used as operating revenue reference |
| Q3 FY26 PAT | Around ₹63.45 crore | Public result coverage | Shows strong profit growth |
| Q3 FY26 EPS | Around ₹24.08 | Public result coverage | Profitability context |
| 9M FY26 total sales | Around INR 20,475 million | Investor/result presentation reference | Used as FY26E base input |
| 9M FY26 PAT margin | Around 9.01% | Investor/result presentation reference | Margin context |
| Automotive segment sales share | Around 99.80% | Investor presentation reference | Shows business concentration |
| Two-wheeler customer exposure | Around 97.32% of automotive segment revenue | Investor presentation reference | Key concentration risk |
| Major customers | TVS Motor and Honda Two Wheeler Group | Investor presentation reference | Customer concentration context |
| Valuation date | 29 April 2026 | Project standard | Used for model timestamp |

---

## Market data sources to refresh

| Data item | Required source | Status |
|---|---|---|
| Current market price | NSE / BSE / reliable market-data source | Needs date-specific refresh |
| Market capitalization | NSE / BSE / reliable market-data source | Needs date-specific refresh |
| Shares outstanding | Annual report / exchange filings | Needs verification |
| Enterprise value | Market cap + debt - cash | Needs reconciliation |
| Beta | Regression vs Nifty Auto / Nifty 50 | Needs calculation |
| Risk-free rate | India 10-year government bond yield | Refresh before model lock |
| Equity risk premium | Reliable India ERP estimate | Refresh before model lock |
| Customer mix | Investor presentation / annual report | Refresh before final model |

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
- customer concentration
- two-wheeler exposure
- capex intensity

Suggested peers:

- Lumax Industries
- Minda Corporation
- Uno Minda
- Varroc Engineering
- Endurance Technologies
- Suprajit Engineering

---

## Data-quality classification

Current classification:

```text
Public-Source Complete v1 — audited-data refresh pending
```

The research framework is complete for public-source v1. Future improvement should focus on audited-data refresh, customer-mix validation and date-consistent peer numerical validation.

---

## Required before final numerical lock

- FY26 audited annual report reconciliation
- full FY26 cash-flow statement
- exact latest share count
- exact cash and debt balance
- beta regression
- date-consistent peer numerical table
- latest market price timestamp
- customer concentration refresh

---

## Source-control note

Every future update should record:

- date of update
- source used
- data item changed
- reason for change
- impact on valuation output
