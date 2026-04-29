# Natco Pharma Numerical DCF Refresh v1

## Research classification

```text
Public-Source Complete v1 — Institutional-Style Preliminary Valuation
```

This numerical refresh adds a conservative, normalized DCF layer to the Natco Pharma research work. It is designed for GitHub portfolio demonstration and interview discussion, not for investment advice.

---

## Valuation date

**Valuation date:** 29 April 2026  
**Currency:** INR crore except per-share values  
**Spot price reference used:** ₹1,094.10 per share  
**Status:** Preliminary numerical model; needs audited FY26 annual report reconciliation.

---

## Key public-source data used

| Input | Value used | Source / logic |
|---|---:|---|
| FY25 total revenue | ₹4,784 crore | FY25 annual report figure converted from INR million |
| FY25 EBITDA | ₹2,550.5 crore | FY25 annual report figure converted from INR million |
| FY25 EBITDA margin | 53.3% | FY25 annual report |
| FY25 PAT | ₹1,883.4 crore | FY25 annual report figure converted from INR million |
| Q3 FY26 consolidated total revenue | ₹705.4 crore | Natco Q3 FY26 press release |
| Q3 FY26 EBITDA including other income | ₹216.8 crore | Natco Q3 FY26 press release |
| Q3 FY26 PAT | ₹151.3 crore | Natco Q3 FY26 press release |
| Spot price reference | ₹1,094.10 | ICICI Direct share-price page, 29 Apr 2026 |
| Shares outstanding used | 17.911 crore | StockAnalysis share statistics, April 2026 |
| Market cap reference | ₹19,550 crore | StockAnalysis market-cap reference |
| Enterprise value reference | ₹16,611 crore | StockAnalysis valuation reference |
| Net cash proxy | ₹2,939 crore | Market cap minus enterprise value proxy; needs audited balance-sheet reconciliation |
| Risk-free rate | 6.98% | India 10-year government bond yield reference used in project |
| India ERP | 7.00% | India ERP assumption used in project |
| Beta | 0.19 | StockAnalysis beta reference; adjusted using company-specific risk premium |

---

## Why the model normalizes Natco heavily

Natco's FY25 EBITDA margin of 53.3% is very high. Q3 FY26 shows a much lower quarterly margin profile. This means a professional DCF should not simply assume FY25 profitability continues forever.

The model therefore uses:

- a reset in FY27 revenue
- normalized margins below FY25 peak
- conservative capex and working-capital assumptions
- explicit net cash addition
- company-specific risk premium in cost of equity

---

## WACC build-up used in v1

| WACC input | Value |
|---|---:|
| Risk-free rate | 6.98% |
| Beta | 0.19 |
| Equity risk premium | 7.00% |
| Company-specific risk premium | 3.00% |
| Cost of equity / WACC used | 11.31% |
| Debt weight | 0.00% |
| Equity weight | 100.00% |

The company-specific risk premium is used because a low observed beta can understate fundamental risks such as product concentration, regulatory events, price erosion, and launch dependence.

---

## Base-case operating assumptions

| Assumption | Value |
|---|---:|
| FY26 revenue base | ₹3,790 crore |
| FY27 revenue reset | -36.7% |
| FY28 revenue growth | 8.0% |
| FY29 revenue growth | 10.0% |
| FY30 revenue growth | 9.0% |
| FY31 revenue growth | 8.0% |
| FY27 EBITDA margin | 24.4% |
| FY28 EBITDA margin | 26.0% |
| FY29 EBITDA margin | 28.0% |
| FY30 EBITDA margin | 29.0% |
| FY31 EBITDA margin | 29.5% |
| D&A as % of revenue | 6.5% |
| Capex as % of revenue | 8.0% |
| NWC investment as % of incremental revenue | 5.0% |
| Tax rate | 17.0% |
| Terminal growth | 4.0% |

---

## Preliminary output

| Scenario | Fair value / share | Upside / downside vs ₹1,094.10 |
|---|---:|---:|
| Bear | ₹409 | -62.6% |
| Base | ₹525 | -52.0% |
| Bull | ₹672 | -38.6% |

---

## Interpretation

The conservative public-source v1 DCF does not yet justify the current spot price. This does not automatically mean the stock is a poor business. It means the market price appears to be discounting stronger future optionality than the conservative normalized base case.

For Natco, the biggest valuation debate is not whether the company has growth opportunities. The biggest debate is whether pipeline launches can offset the normalization of high-margin product-cycle profits.

---

## Required before final numerical lock

- FY26 audited annual report reconciliation
- actual FY26 revenue, EBIT, tax, capex, and working capital
- exact share count
- exact cash, investments, and debt
- beta regression vs Nifty Pharma / Nifty 50
- date-consistent peer numerical table
- refreshed market price

---

## Analyst note

Natco is a valuable research case because it prevents the analyst from confusing a strong product-cycle year with permanent earnings power.

Correct public-source v1 conclusion:

```text
Natco Pharma remains a strong research case, but the conservative normalized DCF requires audited-data refresh and pipeline validation before any final valuation view is locked.
```

---

## Not investment advice

This file is for education, research, modelling practice, and portfolio demonstration only. It does not provide investment advice or a buy/sell recommendation.
