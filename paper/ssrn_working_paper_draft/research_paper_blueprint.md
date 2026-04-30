# SSRN Working Paper Blueprint

## Indian Equity Valuation Lab

**Working paper status:** Draft blueprint  
**Project status:** Public-Source Complete v1  
**Purpose:** Convert the 10-company valuation lab into a serious working paper suitable for SSRN submission after final editing, PDF formatting and disclosure review.

---

## 1. Recommended paper title

### Preferred title

```text
From Screening to Intrinsic Value: A Public-Source Fundamental Valuation Framework for Indian Equities
```

### Alternative titles

```text
A Practical Multi-Sector DCF Framework for Indian Equity Research: Evidence from Ten Listed Companies
```

```text
Building a Public-Source Equity Research Framework for Indian Stocks: DCF, WACC, Peer Analysis and Risk Normalization
```

```text
Sector-Specific Normalization in Indian Equity Valuation: A Public-Source Case Study of Ten Listed Companies
```

---

## 2. Core research problem

Most beginner-level equity analysis projects focus on stock returns, charts, ratios or simple screening. They often fail to connect business-model differences with intrinsic valuation assumptions.

This paper attempts to solve the following research problem:

```text
How can a disciplined public-source valuation framework be designed to evaluate Indian listed companies across sectors while avoiding over-extrapolation of recent earnings, commodity cycles, one-off gains and sector-specific margin peaks?
```

---

## 3. What the paper is trying to solve

The paper tries to bridge the gap between:

1. simple stock screening and ratio analysis
2. analyst-style intrinsic valuation
3. sector-specific normalization
4. transparent assumption documentation
5. reproducible Python/Excel workflow

The goal is not to claim precise target prices. The goal is to demonstrate a structured research method that converts public information into disciplined valuation assumptions.

---

## 4. Main research objective

```text
To develop and demonstrate a public-source, reproducible equity valuation framework for Indian listed companies using FCFF DCF, WACC construction, peer-comparison design, risk matrices, source logs and sector-specific normalization.
```

---

## 5. Specific research objectives

1. To build a structured public-source valuation framework for Indian equities.
2. To apply the framework to ten Indian listed companies across different sectors.
3. To examine how DCF assumptions differ by sector and business model.
4. To identify the key valuation risks for each sector.
5. To design a reproducible Python/Excel workflow for valuation documentation and dashboarding.
6. To distinguish complete public-source research from institutional-grade audited research.

---

## 6. Research questions

### Main research question

```text
Can a structured public-source valuation framework improve the quality and transparency of Indian equity research compared with simple return or ratio-based analysis?
```

### Supporting research questions

1. How should DCF assumptions be normalized across different Indian sectors?
2. What are the main sector-specific valuation risks in Indian equities?
3. How can WACC and company-specific risk premiums be documented transparently in a public-source research project?
4. How can peer comparison be used as a valuation sanity check without replacing intrinsic valuation?
5. What data limitations remain when using public sources instead of audited institutional databases?
6. How can Python and Excel automation improve reproducibility in equity research documentation?

---

## 7. Hypotheses

### Hypothesis 1

```text
H1: A structured DCF-based framework with explicit assumption logs produces more transparent valuation outputs than simple ratio or return-based analysis.
```

### Hypothesis 2

```text
H2: Sector-specific normalization materially changes the interpretation of company valuation quality.
```

Example: commodity companies require mid-cycle margin normalization, refiners require GRM normalization, pharma companies require product-cycle normalization and capital-goods companies require order-book conversion analysis.

### Hypothesis 3

```text
H3: Public-source research can reach a useful portfolio/interview-grade standard when assumptions, sources and limitations are documented clearly, but it cannot be considered fully institutional-grade without audited data reconciliation and market-data validation.
```

### Hypothesis 4

```text
H4: A reproducible Python/Excel workflow improves the consistency and auditability of equity research outputs.
```

---

## 8. Proposed abstract

```text
This paper develops a public-source fundamental valuation framework for Indian listed equities and applies it to ten companies across autos, pharma, metals, refining, agrochemicals, industrial packaging and capital goods. The study moves beyond simple return and ratio analysis by integrating FCFF DCF modelling, WACC construction, peer-comparison design, scenario analysis, sensitivity analysis, risk matrices, source logs and assumption tracking. The central contribution is methodological: the paper demonstrates how sector-specific normalization can improve valuation discipline by preventing over-extrapolation of recent earnings, commodity-cycle margins, refining spreads, product-cycle profits and one-off gains.

The framework is implemented through a combination of company-level research notes, numerical DCF summaries, Python scripts and Excel dashboards. The results show that valuation logic must differ materially by sector: commodity companies require mid-cycle margin assumptions, refiners require normalized GRM analysis, pharma companies require pipeline and product-cycle adjustments, auto suppliers require customer-concentration analysis, and capital-goods companies require order-book and execution-risk analysis. The paper also introduces a data-quality classification that separates Public-Source Complete v1 research from fully institutional-grade research, highlighting the need for audited annual-report reconciliation, live market data, peer numerical tables and beta regression before final valuation use. The study contributes a practical, reproducible and transparent framework for early-stage equity research and finance portfolio development in the Indian market.
```

---

## 9. Keywords

```text
Equity Valuation; Indian Stock Market; DCF; WACC; Fundamental Analysis; Equity Research; Public-Source Research; Financial Modelling; Peer Comparison; Risk Analysis; Python; Excel Dashboard
```

---

## 10. Proposed paper structure

### 1. Introduction

- Background of Indian equity research
- Problem with simple screening and ratio-only analysis
- Need for transparent assumption-based valuation
- Research objectives
- Contribution of the paper

### 2. Literature and Conceptual Background

- Fundamental analysis
- DCF valuation
- WACC and cost of capital
- Peer valuation and relative multiples
- Risk and sensitivity analysis
- Public-source research limitations

### 3. Data and Sample Selection

- Ten Indian listed companies
- Sector coverage
- Public data sources used
- Research classification
- Limitations of public-source data

### 4. Methodology

- FCFF DCF framework
- WACC framework
- Terminal value logic
- Scenario analysis
- Sensitivity framework
- Peer comparison methodology
- Risk-matrix design
- Python/Excel implementation

### 5. Company-Level Application

- Summary of each company
- Business model
- Sector normalization logic
- Key DCF assumptions
- Main valuation risk

### 6. Cross-Company Findings

- Sector-specific valuation differences
- Common modelling mistakes avoided
- Role of normalization
- Public-source data limitations
- Usefulness of assumption/source logs

### 7. Discussion

- What the framework adds
- Why valuation is not one-size-fits-all
- Strengths and weaknesses
- Practical use for analysts, students and early-career finance professionals

### 8. Limitations

- No audited FY26 reconciliation yet
- No final live market-data lock
- Peer numerical table pending
- Beta regression pending review
- Not investment advice

### 9. Conclusion

- Summary of contribution
- Final classification
- Future research directions

### 10. Appendix

- Company dashboard
- DCF assumption tables
- Peer framework
- Risk matrix
- Python/Excel workflow
- AI disclosure statement

---

## 11. Data and sample design

### Sample size

```text
10 Indian listed companies
```

### Companies

1. Hero MotoCorp
2. Natco Pharma
3. NALCO
4. Hindustan Zinc
5. CPCL
6. Sharda Cropchem
7. Fiem Industries
8. Time Technoplast
9. Force Motors
10. Triveni Turbine

### Sector logic

The companies were selected to cover multiple business models:

- auto and auto components
- pharma
- metals and commodities
- refining
- agrochemicals
- industrial packaging
- capital goods

This makes the research useful because each sector requires different valuation logic.

---

## 12. Methodology formula set

### FCFF

```text
FCFF = EBIT × (1 - Tax Rate) + Depreciation and Amortization - Capital Expenditure - Change in Net Working Capital
```

### Cost of equity

```text
Cost of Equity = Risk-free Rate + Beta × Equity Risk Premium + Company-Specific Risk Premium
```

### WACC

```text
WACC = Equity Weight × Cost of Equity + Debt Weight × After-tax Cost of Debt
```

### Terminal value

```text
Terminal Value = Final Year FCFF × (1 + Terminal Growth) / (WACC - Terminal Growth)
```

---

## 13. Expected findings

The expected findings are methodological rather than investment recommendations.

1. DCF assumptions must be sector-specific.
2. Commodity companies require mid-cycle normalization.
3. Refiners require GRM normalization.
4. Pharma companies require product-cycle and pipeline normalization.
5. Auto-component companies require customer-concentration analysis.
6. Capital-goods companies require order-book and execution-risk analysis.
7. Public-source valuation is useful but must disclose its limitations.
8. Python/Excel automation improves consistency and auditability.

---

## 14. Original contribution

This paper contributes:

- a practical public-source valuation framework
- sector-specific normalization logic for Indian equities
- a 10-company case-study application
- a data-quality classification system
- reproducible Python/Excel dashboard workflow
- a transparent distinction between public-source research and institutional-grade research

---

## 15. Limitations section

The paper should clearly state:

```text
This study is not intended to provide investment recommendations. The valuation outputs are preliminary and depend on public-source assumptions. Final institutional-grade valuation would require audited FY26 annual-report reconciliation, verified share counts, net debt/cash reconciliation, live market prices, date-consistent peer numerical tables, beta regression review and independent model validation.
```

---

## 16. AI disclosure statement

Suggested disclosure:

```text
The authors used AI tools to assist with drafting, structuring, documentation, wording refinement and code-generation support. The authors remain responsible for the research design, interpretation, assumptions, data verification, final manuscript content and all conclusions. AI-generated content was reviewed and edited by the authors before submission.
```

---

## 17. SSRN submission-readiness checklist

Before upload:

- final title in English
- author names, affiliations and emails
- full-text PDF
- abstract in English
- keywords
- date written
- AI disclosure statement
- references section
- methodology section
- limitations section
- appendix with project outputs
- no claim of investment advice
- no claim of fully audited institutional-grade research

---

## 18. Recommended final positioning

The paper should be positioned as:

```text
A methodological public-source equity research framework and case-study application.
```

It should not be positioned as:

```text
A final buy/sell recommendation paper.
```

---

## 19. Best next writing step

The next step is to draft the full manuscript in this order:

1. Abstract
2. Introduction
3. Research questions and hypotheses
4. Methodology
5. Data and sample
6. Company application summary
7. Findings and discussion
8. Limitations
9. Conclusion
10. References and appendix

---

## 20. Final recommended title

```text
From Screening to Intrinsic Value: A Public-Source Fundamental Valuation Framework for Indian Equities
```
