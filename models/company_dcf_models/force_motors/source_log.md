# Force Motors Source Log

## Purpose

This file records the public-source inputs used for the Force Motors public-source v1 research pack and separates completed v1 inputs from later refresh requirements.

---

## Primary company sources

| Source type | Use in model | Status |
|---|---|---|
| FY25 annual report | Historical revenue, margins, cash flow, balance sheet, segment and product context | Use for historical base and audited reconciliation |
| Quarterly results | FY26 revenue, EBITDA, PBT, PAT, margin and debt trends | Used for public-source v1 context |
| Official company results release | Q3 FY26 and 9M FY26 revenue, EBITDA, PBT, PAT and debt status | Used for v1 public-source figures |
| Investor presentation | Product mix, platform strategy, capex and aggregate manufacturing context | Use latest available version |
| Exchange filings | Results, corporate actions, shareholding and dividend updates | Requires periodic refresh |

---

## Public-source data points used in v1

| Data item | Value / interpretation | Source type | Model treatment |
|---|---|---|---|
| Q3 FY26 revenue | ₹2,155 crore | Official company result release | Supports FY26 revenue run-rate context |
| Q3 FY26 revenue growth | 13% YoY | Official company result release | Growth context |
| 9M FY26 revenue | ₹6,583 crore | Official company result release | Used as FY26E base input |
| 9M FY26 revenue growth | 14% YoY | Official company result release | Growth context |
| Q3 FY26 EBITDA | ₹401 crore | Official company result release | Supports strong operating leverage context |
| Q3 FY26 EBITDA growth | 63% YoY | Official company result release | Margin / operating leverage context |
| 9M FY26 EBITDA | ₹1,145 crore | Official company result release | Profitability context |
| Q3 FY26 PBT before exceptional | ₹328 crore | Official company result release | Normalized operating profit context |
| Q3 FY26 PAT after exceptional | ₹403 crore | Official company result release | Reported profit context, not recurring run-rate |
| Debt status | Nil total debt reported | Official company result release | Balance-sheet strength context; needs annual report verification |
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
| Product / segment mix | Annual report / investor presentation | Refresh before final model |

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
- vehicle volume growth
- customer/program concentration
- capex intensity

Suggested peers:

- Ashok Leyland
- Tata Motors
- Mahindra & Mahindra
- SML Isuzu
- Atul Auto
- Eicher Motors / VECV context where appropriate

---

## Data-quality classification

Current classification:

```text
Public-Source Complete v1 — audited-data refresh pending
```

The research framework is complete for public-source v1. Future improvement should focus on audited-data refresh, segment/product mix validation, recurring earnings normalization and date-consistent peer numerical validation.

---

## Required before final numerical lock

- FY26 audited annual report reconciliation
- full FY26 cash-flow statement
- exact latest share count
- exact cash and debt balance
- beta regression
- date-consistent peer numerical table
- latest market price timestamp
- product and segment mix update
- exceptional item normalization

---

## Source-control note

Every future update should record:

- date of update
- source used
- data item changed
- reason for change
- impact on valuation output
