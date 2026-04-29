# CPCL Source Log

## Purpose

This file records the public-source inputs used for the CPCL public-source v1 research pack and separates completed v1 inputs from later refresh requirements.

---

## Primary company sources

| Source type | Use in model | Status |
|---|---|---|
| FY25 annual report | Full-year revenue, profit, debt, working capital and operating context | Use for historical base and audited reconciliation |
| Quarterly results | FY26 revenue, PAT, GRM, throughput and utilization trends | Used for public-source v1 context |
| Press releases | Current quarterly performance and operational commentary | Used for v1 summary |
| Investor presentation | Refinery throughput, capex, product mix and strategy | Use latest available version |
| Exchange filings | Results, corporate actions, shareholding and dividend updates | Requires periodic refresh |

---

## Public-source data points used in v1

| Data item | Value / interpretation | Source type | Model treatment |
|---|---|---|---|
| Q3 FY26 revenue from operations | Around ₹19,438 crore | Public result coverage / company results | Supports FY26 revenue run-rate context |
| Q3 FY26 PAT | Around ₹987 crore | Public result coverage / company results | Shows strong turnaround from prior year |
| Q3 FY25 PAT comparison | Around ₹10 crore | Public result coverage / company results | Highlights refining-margin sensitivity |
| 9M FY26 GRM | Around US$7.72/bbl | Public result coverage / company results | Used as strong-cycle reference |
| 9M FY25 GRM comparison | Around US$3.40/bbl | Public result coverage / company results | Shows margin-cycle improvement |
| Q3 FY26 capacity utilization | Above 100% | Public result coverage / company results | Supports strong throughput context |
| Valuation date | 29 April 2026 | Project standard | Used for model timestamp |

---

## Market data sources to refresh

| Data item | Required source | Status |
|---|---|---|
| Current market price | NSE / BSE / reliable market-data source | Needs date-specific refresh |
| Market capitalization | NSE / BSE / reliable market-data source | Needs date-specific refresh |
| Shares outstanding | Annual report / exchange filings | Needs verification |
| Enterprise value | Market cap + debt - cash | Needs reconciliation |
| Beta | Regression vs Nifty Energy / Nifty 50 | Needs calculation |
| Risk-free rate | India 10-year government bond yield | Refresh before model lock |
| Equity risk premium | Reliable India ERP estimate | Refresh before model lock |
| GRM deck | Company / industry refining-margin data | Refresh before model lock |

---

## Peer data sources

Peer comparison should be refreshed from a consistent source and date for:

- P/E
- EV/EBITDA
- GRM
- refinery utilization
- revenue growth
- EBITDA margin
- PAT margin
- ROE
- ROCE
- net debt / equity
- dividend yield
- capex intensity

Suggested peers:

- Indian Oil Corporation
- Bharat Petroleum Corporation
- Hindustan Petroleum Corporation
- Mangalore Refinery and Petrochemicals
- Reliance Industries as large private refining reference
- global refining peers where available

---

## Data-quality classification

Current classification:

```text
Public-Source Complete v1 — audited-data refresh pending
```

The research framework is complete for public-source v1. Future improvement should focus on audited-data refresh, GRM deck validation and date-consistent peer numerical validation.

---

## Required before final numerical lock

- FY26 audited annual report reconciliation
- full FY26 cash-flow statement
- exact latest share count
- exact cash and debt balance
- beta regression
- date-consistent peer numerical table
- latest market price timestamp
- mid-cycle GRM assumption deck

---

## Source-control note

Every future update should record:

- date of update
- source used
- data item changed
- reason for change
- impact on valuation output
