# Institutional-Style Research Layer

## Project classification

This repository is being upgraded from a stock-return analyzer into an Indian Equity Valuation Lab with an institutional-style research structure.

The goal is to make each company valuation suitable for:

- GitHub portfolio demonstration
- interview discussion
- equity research learning
- investment banking / valuation case-study practice
- future research-paper development

This project is **not** a compliance-approved investment research product and does not provide buy/sell recommendations.

---

## Research version labels

### Final Research v1 — Institutional-Style Preliminary Valuation

This label means the company file includes:

- business overview
- industry context
- investment thesis
- growth drivers
- financial performance review
- DCF assumption logic
- WACC framework
- peer comparison framework
- scenario analysis
- sensitivity-analysis framework
- risk matrix
- data-quality status
- source log
- final research conclusion

### Fully institutional-grade published research

This label should **not** be used unless the model has been reconciled with:

- audited annual reports
- latest quarterly filings
- verified market price and share count
- official peer numerical tables
- beta and WACC calculations
- debt, cash, and working-capital reconciliation
- compliance-style review

---

## Standard company research structure

Every company folder should include:

```text
company_name/
├── company_research_note.md
├── assumptions_log.md
├── source_log.md
├── dcf_model.xlsx
└── charts/
```

---

## Standard research-note sections

1. Executive summary
2. Business overview
3. Industry context
4. Investment thesis
5. Growth drivers
6. Financial performance review
7. DCF assumption justification
8. WACC framework
9. Peer valuation framework
10. Scenario analysis
11. Sensitivity analysis
12. Risk matrix
13. Data-quality status
14. Final conclusion

---

## Standard DCF discipline

The DCF should be interpreted as a valuation range, not a single precise truth.

The key model drivers are:

- revenue CAGR
- EBITDA / EBIT margin
- tax rate
- depreciation and amortization
- capital expenditure
- change in net working capital
- terminal growth
- WACC
- share count
- net debt / net cash

---

## Required sensitivity tables

At minimum, each DCF should include:

```text
Fair Value per Share sensitivity:
Rows = WACC
Columns = Terminal Growth
```

A second useful table:

```text
Fair Value sensitivity:
Rows = EBITDA Margin
Columns = Revenue CAGR
```

---

## Final project disclaimer

This repository is for education, research, modelling practice, and portfolio demonstration only. Nothing in this repository should be interpreted as financial advice, investment advice, or a buy/sell recommendation. All valuation outputs depend heavily on assumptions and must be independently verified before real investment use.
