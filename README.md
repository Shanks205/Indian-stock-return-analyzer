# Indian Equity Valuation Lab

A Python, Excel and research-documentation project for building institutional-style public-source equity research on Indian listed companies.

This repository started as a beginner-friendly Indian stock return analyzer and has now been expanded into a complete 10-company equity valuation lab covering DCF logic, WACC frameworks, peer comparison, risk matrices, source logs, assumption logs, Excel dashboards and consolidated valuation tracking.

> This project is for education, research practice and portfolio demonstration only. It is not investment advice or a buy/sell recommendation.

---

## SSRN Working Paper

This repository supports our SSRN working paper:

**From Screening to Intrinsic Value: A Public-Source DCF Valuation Framework for Indian Equities**

The paper develops a reproducible public-source valuation framework for Indian listed equities using stock screening, Piotroski-style quality checks, FCFF DCF, WACC construction, peer comparison, sector-specific normalization, and Python/Excel automation.

**SSRN:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6681723

---

## Final project status

```text
Final Status: Public-Source Complete v1
Coverage: 10 Indian listed companies
Research type: Institutional-style preliminary valuation research
Project stage: Complete for GitHub portfolio / interview discussion
Future stage: audited FY26 refresh and validation
```

The project is complete at the intended professional portfolio level.

It is not labelled as fully institutional-grade published research because final institutional publication would still require audited FY26 annual-report reconciliation, live market data, date-consistent peer numerical tables, verified beta regressions, independent model review and compliance-style review.

---

## Completed company coverage

| # | Company | Sector / Theme | Status |
|---:|---|---|---|
| 1 | Hero MotoCorp | Auto / Two-wheelers | Public-Source Complete v1 |
| 2 | Natco Pharma | Pharma / Complex generics | Public-Source Complete v1 |
| 3 | NALCO | Metals / Aluminium | Public-Source Complete v1 |
| 4 | Hindustan Zinc | Metals / Zinc-Silver | Public-Source Complete v1 |
| 5 | CPCL | Oil & Gas / Refining | Public-Source Complete v1 |
| 6 | Sharda Cropchem | Agrochemicals | Public-Source Complete v1 |
| 7 | Fiem Industries | Auto Components | Public-Source Complete v1 |
| 8 | Time Technoplast | Industrial Packaging / Polymers | Public-Source Complete v1 |
| 9 | Force Motors | Auto / Vans & Engines | Public-Source Complete v1 |
| 10 | Triveni Turbine | Capital Goods / Turbines | Public-Source Complete v1 |

---

## What has been completed

Each company now has:

- institutional-style research note
- assumptions log
- source log
- peer framework
- numerical refresh summary
- research completion audit
- consolidated tracker entry

The project also includes:

- consolidated valuation dashboard
- 10-company Excel DCF workbook pack
- consolidated Excel dashboard generator
- company DCF workbook-pack generator
- beta regression pipeline
- peer-table refresh template
- final project completion report
- final audit checklist
- career presentation pack

---

## Key project files

| File | Purpose |
|---|---|
| `docs/final_project_completion_report.md` | Final project completion report |
| `docs/final_audit_checklist.md` | Final audit checklist confirming completion status |
| `docs/career_presentation_pack.md` | Resume bullets, GitHub description, LinkedIn post and interview pitch |
| `docs/institutional_research_layer.md` | Defines the research standard and classification system |
| `outputs/valuation_summary/consolidated_research_tracker.md` | Tracks completion status of all company research packs |
| `outputs/valuation_summary/consolidated_valuation_dashboard.md` | Summarizes all 10 companies in one dashboard |
| `scripts/build_consolidated_valuation_dashboard.py` | Builds the consolidated Excel dashboard workbook |
| `scripts/build_company_dcf_workbook_pack.py` | Builds the 10-company Excel DCF workbook pack |
| `scripts/beta_regression_pipeline.py` | Calculates reproducible beta estimates for WACC refresh |
| `scripts/peer_table_template_builder.py` | Creates a date-consistent peer-table refresh template |
| `src/dcf_model.py` | Reusable DCF valuation skeleton |
| `src/piotroski_score.py` | Piotroski F-Score module |

---

## Project objective

The objective is to build a repeatable analyst-style framework for evaluating Indian equities.

```text
Stock universe
→ Fundamental screening
→ Financial performance review
→ DCF valuation logic
→ WACC framework
→ Scenario and sensitivity analysis
→ Peer comparison
→ Risk matrix
→ Source and assumption logs
→ Research completion audit
→ Consolidated valuation dashboard
→ Final audit and project completion report
→ Career presentation pack
```

The project demonstrates how a structured valuation framework can improve equity research quality compared with simple return analysis.

---

## Research classification

The repository uses the following final classification:

```text
Public-Source Complete v1 — audited-data refresh pending
```

This means each company has a complete public-source research pack suitable for:

- GitHub portfolio presentation
- finance interview discussion
- equity research learning
- valuation-methodology demonstration
- future audited-data refresh

It does not mean the research is fully institutional-grade or publication-final.

A fully institutional-grade version would still require:

- audited FY26 annual report reconciliation
- live market price refresh
- share-count verification
- net debt / cash reconciliation
- peer numerical table validation
- beta regression review
- WACC refinement
- independent model review

---

## Research pack structure

Each company folder follows the same structure:

```text
models/company_dcf_models/company_name/
├── company_research_note.md
├── assumptions_log.md
├── source_log.md
├── peer_framework_v1.md
└── research_completion_audit.md
```

Each company also has a numerical summary in:

```text
outputs/valuation_summary/company_name_numerical_refresh_v1.md
```

---

## How to run the current code

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

Run the original return analyzer:

```bash
python src/main.py
```

Run the Piotroski module demo:

```bash
python src/piotroski_score.py
```

Run the DCF module demo:

```bash
python src/dcf_model.py
```

Build the Hero MotoCorp Excel DCF workbook:

```bash
python scripts/build_hero_motocorp_dcf_model.py
```

Build the consolidated Excel dashboard:

```bash
python scripts/build_consolidated_valuation_dashboard.py
```

Build the 10-company Excel DCF workbook pack:

```bash
python scripts/build_company_dcf_workbook_pack.py
```

Build the beta regression workbook:

```bash
python scripts/beta_regression_pipeline.py
```

Build the peer-table refresh template:

```bash
python scripts/peer_table_template_builder.py
```

---

## Skills demonstrated

This project demonstrates:

- equity research writing
- DCF valuation logic
- WACC construction
- scenario and sensitivity analysis
- peer-comparison design
- public-source research discipline
- financial modelling structure
- Python-based finance tooling
- Excel model generation
- project documentation
- GitHub portfolio presentation

---

## Future refresh work

The project is complete at Public-Source Complete v1 level. Future work should be treated as data refresh and validation, not missing project completion.

Future refresh items:

1. audited FY26 annual report refresh
2. date-consistent peer numerical tables
3. beta regression review and WACC refinement
4. market-price refresh and valuation-range update
5. charts for fair value sensitivity and sector comparison
6. final research-paper style write-up

---

## Suggested portfolio description

```text
Built a 10-company Indian Equity Valuation Lab combining DCF modelling, WACC frameworks, peer analysis, risk matrices, source logs, assumption tracking and Excel/Python automation. The project demonstrates institutional-style public-source equity research and is structured for future audited-data refresh.
```

---

## Disclaimer

This repository is for education, research practice and portfolio demonstration only. It does not provide investment advice, financial advice or buy/sell recommendations. All valuation outputs depend heavily on assumptions and must be independently verified before real investment use.
