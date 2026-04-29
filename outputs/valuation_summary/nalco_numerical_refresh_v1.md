# NALCO Numerical DCF Refresh v1

## Research classification

```text
Public-Source Complete v1 — Institutional-Style Preliminary Valuation
```

This numerical refresh adds a conservative, cycle-normalized DCF layer to the NALCO research work. It is designed for GitHub portfolio demonstration and interview discussion, not for investment advice.

---

## Valuation date

**Valuation date:** 29 April 2026  
**Currency:** INR crore except per-share values  
**Spot price reference used:** ₹437.05 per share  
**Status:** Preliminary numerical model; needs audited FY26 annual report reconciliation.

---

## Key public-source data used

| Input | Value used | Source / logic |
|---|---:|---|
| Q3 FY26 net profit | ₹1,601 crore | NALCO company communication |
| Q3 FY26 total income | ₹4,925 crore | NALCO company communication |
| 9M FY26 revenue from operations | ₹12,830 crore | NALCO company communication |
| 9M FY26 net profit | ₹4,098 crore | NALCO company communication |
| FY25 net sales | ₹16,787.6 crore | Public annual-report / financial-data reference |
| FY25 PAT | ₹5,324.7 crore | Public annual-report / financial-data reference |
| Spot price reference | ₹437.05 | Market quote reference around late April 2026 |
| Shares outstanding used | 183.66 crore | Approximation from paid-up equity / face value and market data; needs verification |
| Market cap reference | Around ₹80,000 crore | Spot price × share count approximation |
| Risk-free rate | 6.98% | India 10-year government bond yield reference used in project |
| India ERP | 7.00% | India ERP assumption used in project |
| Beta | 1.10 | Placeholder commodity beta; requires regression vs Nifty Metal / Nifty 50 |

---

## Why the model normalizes NALCO heavily

NALCO's FY25 and 9M FY26 profitability are very strong. However, aluminium and alumina businesses are cyclical, so a professional DCF should not assume current commodity margins continue forever.

The model therefore uses:

- FY26E revenue based on 9M FY26 plus normalized Q4
- margin fade from strong current levels to mid-cycle levels
- moderate growth after a high base
- higher capex intensity than asset-light businesses
- conservative terminal growth
- commodity / PSU risk premium in cost of equity

---

## WACC build-up used in v1

| WACC input | Value |
|---|---:|
| Risk-free rate | 6.98% |
| Beta | 1.10 |
| Equity risk premium | 7.00% |
| Commodity / PSU risk premium | 1.00% |
| Cost of equity / WACC used | 15.68% |
| Debt weight | 0.00% |
| Equity weight | 100.00% |

The commodity / PSU risk premium reflects aluminium-price cyclicality, public-sector ownership considerations, capex-cycle risk and policy influence.

---

## Base-case operating assumptions

| Assumption | Value |
|---|---:|
| FY26 revenue base | ₹17,200 crore |
| FY27 revenue growth | 3.0% |
| FY28 revenue growth | 4.0% |
| FY29 revenue growth | 4.0% |
| FY30 revenue growth | 4.0% |
| FY31 revenue growth | 3.5% |
| FY27 EBITDA margin | 36.0% |
| FY28 EBITDA margin | 34.0% |
| FY29 EBITDA margin | 32.0% |
| FY30 EBITDA margin | 30.0% |
| FY31 EBITDA margin | 29.0% |
| D&A as % of revenue | 6.0% |
| Capex as % of revenue | 10.0% |
| NWC investment as % of incremental revenue | 6.0% |
| Tax rate | 25.0% |
| Terminal growth | 3.5% |

---

## Preliminary output

| Scenario | Fair value / share | Upside / downside vs ₹437.05 |
|---|---:|---:|
| Bear | ₹197 | -54.9% |
| Base | ₹263 | -39.8% |
| Bull | ₹357 | -18.3% |

---

## Interpretation

The conservative public-source v1 DCF does not yet justify the current spot price under normalized commodity-cycle assumptions. This does not mean the company is weak. It means the market price appears to be discounting strong aluminium/alumina conditions, high profitability and dividend appeal.

For NALCO, the biggest valuation debate is not whether recent results are strong. The biggest debate is what level of aluminium/alumina margin should be treated as sustainable mid-cycle profitability.

---

## Required before final numerical lock

- FY26 audited annual report reconciliation
- actual FY26 revenue, EBIT, tax, capex and working capital
- exact share count
- exact cash and debt balance
- beta regression vs Nifty Metal / Nifty 50
- date-consistent peer numerical table
- refreshed market price

---

## Analyst note

NALCO is a valuable research case because it prevents the analyst from confusing a strong commodity-price period with permanent earnings power.

Correct public-source v1 conclusion:

```text
NALCO remains a strong research case, but the conservative normalized DCF requires audited-data refresh and commodity-cycle validation before any final valuation view is locked.
```

---

## Not investment advice

This file is for education, research, modelling practice and portfolio demonstration only. It does not provide investment advice or a buy/sell recommendation.
