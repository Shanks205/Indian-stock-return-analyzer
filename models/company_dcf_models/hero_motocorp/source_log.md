# Hero MotoCorp Source Log

## Purpose

This file tracks the sources required for the Hero MotoCorp valuation model and research note.

The purpose is to separate:

- available v1 research inputs
- data that still needs refresh
- data required before institutional-grade publication

---

## Primary company sources

| Source type | Use in model | Status |
|---|---|---|
| Annual report | Revenue, EBIT, PAT, tax, debt, cash, working capital, capex | Needs latest audited FY26 annual report refresh |
| Quarterly results | Recent revenue, EBITDA, PAT, margin, management commentary | Use latest available quarterly release |
| Investor presentation | Growth drivers, segment commentary, strategy | Use latest available investor deck |
| Earnings call transcript | Management commentary and demand outlook | Use latest available transcript |
| Shareholding pattern | Ownership and promoter/institutional holding | Needs latest exchange filing |

---

## Market data sources

| Data item | Required source | Status |
|---|---|---|
| Current market price | NSE / BSE / reliable market-data provider | Needs timestamped refresh |
| Market capitalization | NSE / BSE / reliable market-data provider | Needs timestamped refresh |
| Shares outstanding | Annual report / exchange / financial database | Needs verification |
| Beta | Regression calculation vs Nifty 50 / Nifty Auto | Needs calculation |
| Risk-free rate | India 10-year government bond yield | Needs latest refresh |
| Equity risk premium | Reliable ERP estimate | Needs validation |

---

## Peer data sources

Peer comparison should use reliable and consistent sources for:

- P/E
- EV/EBITDA
- revenue growth
- EBITDA margin
- ROE
- ROCE
- net cash / debt
- dividend yield
- 1-year return
- 3-year sales CAGR

Suggested peers:

- Bajaj Auto
- TVS Motor
- Eicher Motors
- M&M
- EV references such as Ola Electric / Ather, where relevant

---

## Data-quality classification

Current classification:

```text
Final Research v1 — Institutional-Style Preliminary Valuation
```

This means the model structure and research framework are complete, but final numerical investment conclusions require audited data and live market-data refresh.

---

## Required before fully institutional-grade publication

- FY26 audited annual report reconciliation
- latest quarterly results update
- current market price timestamp
- share count verification
- net debt / cash reconciliation
- peer numerical table validation
- beta and WACC recalculation
- compliance-style review

---

## Source-control note

Every future update should record:

- date of update
- source used
- data item changed
- reason for change
- impact on valuation output
