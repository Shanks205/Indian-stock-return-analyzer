# Consolidated Research Tracker

## Project

Indian Equity Valuation Lab

This tracker records the status of each company valuation inside the repository.

---

## Research status labels

| Label | Meaning |
|---|---|
| Not started | Company selected but no valuation work added yet |
| Research in progress | Business/financial analysis started |
| DCF in progress | DCF model being built |
| Final Research v1 complete | Institutional-style preliminary research note completed |
| Numerical refresh v1 complete | DCF numerical assumptions, WACC framework, sensitivity framework, and summary added |
| Needs audited refresh | Requires latest annual report, filings, and market data update |
| Fully institutional-grade | Only after audited reconciliation, peer validation, and compliance-style review |

---

## Company tracker

| Company | Category | Status | Research note | Assumptions log | Source log | DCF model | Next action |
|---|---|---|---|---|---|---|---|
| Hero MotoCorp | Core value / quality | Numerical refresh v1 complete | Added | Added | Added | Build script added; workbook generated locally | Add audited FY26 refresh, beta regression, and peer numerical table |
| Natco Pharma | Core value / quality | Not started | Pending | Pending | Pending | Pending | Begin company research |
| NALCO | Core value / quality | Not started | Pending | Pending | Pending | Pending | Begin company research |
| Hindustan Zinc | Core value / quality | Not started | Pending | Pending | Pending | Pending | Begin company research |
| CPCL | Core value / quality | Not started | Pending | Pending | Pending | Pending | Begin company research |
| Sharda Cropchem | Core value / quality | Not started | Pending | Pending | Pending | Pending | Begin company research |
| Fiem Industries | Growth / satellite | Not started in repo | Pending | Pending | Pending | Pending | Standardize prior model inside repo |
| Time Technoplast | Growth / satellite | Not started | Pending | Pending | Pending | Pending | Begin company research |
| Force Motors | Growth / satellite | Not started | Pending | Pending | Pending | Pending | Begin company research |
| Triveni Turbine | Growth / satellite | Not started | Pending | Pending | Pending | Pending | Begin company research |

---

## Current completed company

### Hero MotoCorp

Current classification:

```text
Numerical refresh v1 complete — still needs audited FY26 data refresh
```

Completed files:

- `models/company_dcf_models/hero_motocorp/hero_motocorp_research_note.md`
- `models/company_dcf_models/hero_motocorp/assumptions_log.md`
- `models/company_dcf_models/hero_motocorp/source_log.md`
- `outputs/valuation_summary/hero_motocorp_numerical_refresh_v1.md`
- `scripts/build_hero_motocorp_dcf_model.py`

Pending:

- audited FY26 annual report reconciliation
- actual FY26 revenue, EBIT, tax, capex, and working capital refresh
- share count verification
- cash and debt reconciliation
- beta regression vs Nifty 50 / Nifty Auto
- peer numerical table validation
- latest market price refresh

---

## Next recommended company

The next company should be analysed using the same institutional sequence:

1. Business overview
2. Industry context
3. Investment thesis
4. Growth drivers
5. Financial performance review
6. DCF assumptions
7. WACC framework
8. Peer comparison
9. Scenario analysis
10. Sensitivity analysis
11. Risk matrix
12. Data-quality status
13. Final Research v1 conclusion
14. Numerical DCF refresh

---

## Reminder

This tracker is for project management and research discipline only. It does not represent investment advice or a buy/sell recommendation.
