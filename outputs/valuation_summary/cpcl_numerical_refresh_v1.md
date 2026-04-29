# CPCL Numerical DCF Refresh v1

## Research classification

```text
Public-Source Complete v1 — Institutional-Style Preliminary Valuation
```

This numerical refresh adds a conservative, cycle-normalized DCF layer to the CPCL research work. It is designed for GitHub portfolio demonstration and interview discussion, not for investment advice.

---

## Valuation date

**Valuation date:** 29 April 2026  
**Currency:** INR crore except per-share values  
**Spot price reference used:** To refresh with NSE/BSE quote  
**Status:** Preliminary numerical model; needs audited FY26 annual report reconciliation.

---

## Key public-source data used

| Input | Value used | Source / logic |
|---|---:|---|
| Q3 FY26 revenue from operations | ₹19,438 crore | Public result coverage / company results |
| Q3 FY26 PAT | ₹987 crore | Public result coverage / company results |
| Q3 FY25 PAT comparison | ₹10 crore | Public result coverage / company results |
| 9M FY26 GRM | US$7.72/bbl | Public result coverage / company results |
| 9M FY25 GRM comparison | US$3.40/bbl | Public result coverage / company results |
| Q3 FY26 capacity utilization | Above 100% | Public result coverage / company results |
| Risk-free rate | 6.98% | India 10-year government bond yield reference used in project |
| India ERP | 7.00% | India ERP assumption used in project |
| Beta | 1.20 | Placeholder refining-cycle beta; requires regression vs Nifty Energy / Nifty 50 |

---

## Why the model normalizes CPCL heavily

CPCL's Q3 FY26 profitability improved sharply because of better GRMs and strong throughput. However, refining margins are cyclical. A professional DCF should not assume a strong refining-margin period continues forever.

The model therefore uses:

- FY26E revenue based on 9M run-rate and Q3 strength
- margin fade toward mid-cycle refining margins
- conservative working-capital treatment
- moderate-to-high capex intensity
- refining-cycle risk premium in cost of equity
- no permanent extrapolation of inventory gains

---

## WACC build-up used in v1

| WACC input | Value |
|---|---:|
| Risk-free rate | 6.98% |
| Beta | 1.20 |
| Equity risk premium | 7.00% |
| Refining-cycle risk premium | 1.50% |
| Cost of equity / WACC used | 16.88% |
| Debt weight | To refresh |
| Equity weight | To refresh |

The refining-cycle risk premium reflects GRM volatility, inventory-risk, working-capital swings, crude/product price exposure and policy risk.

---

## Base-case operating assumptions

| Assumption | Value |
|---|---:|
| FY26 revenue base | ₹75,000 crore |
| FY27 revenue growth | 2.0% |
| FY28 revenue growth | 3.0% |
| FY29 revenue growth | 3.0% |
| FY30 revenue growth | 2.5% |
| FY31 revenue growth | 2.5% |
| FY27 EBITDA margin | 6.0% |
| FY28 EBITDA margin | 5.5% |
| FY29 EBITDA margin | 5.0% |
| FY30 EBITDA margin | 4.8% |
| FY31 EBITDA margin | 4.7% |
| D&A as % of revenue | 1.5% |
| Capex as % of revenue | 3.5% |
| NWC investment as % of incremental revenue | 5.0% |
| Tax rate | 25.0% |
| Terminal growth | 3.0% |

---

## Preliminary interpretation

The public-source v1 DCF should be interpreted as a normalized refining-cycle model, not a forecast of one strong quarter continuing permanently.

For CPCL, the biggest valuation debate is not whether Q3 FY26 was strong. The biggest debate is what GRM should be treated as sustainable through the cycle.

---

## Required before final numerical lock

- FY26 audited annual report reconciliation
- actual FY26 revenue, EBIT, tax, capex and working capital
- exact share count
- exact cash and debt balance
- beta regression vs Nifty Energy / Nifty 50
- date-consistent peer numerical table
- refreshed market price
- mid-cycle GRM assumption deck

---

## Analyst note

CPCL is a valuable research case because it prevents the analyst from confusing a strong refining-margin period with permanent earnings power.

Correct public-source v1 conclusion:

```text
CPCL remains a strong research case, but the conservative normalized DCF requires audited-data refresh and GRM-cycle validation before any final valuation view is locked.
```

---

## Not investment advice

This file is for education, research, modelling practice and portfolio demonstration only. It does not provide investment advice or a buy/sell recommendation.
