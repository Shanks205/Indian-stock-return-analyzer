# Indian Equity Valuation Lab

A Python, Excel and research-documentation project for building institutional-style public-source equity research on Indian listed companies.

This repository started as a beginner-friendly Indian stock return analyzer and has now been expanded into a complete 10-company equity valuation lab covering DCF logic, WACC frameworks, peer comparison, risk matrices, source logs, assumption logs and consolidated valuation tracking.

> This project is for education, research practice and portfolio demonstration only. It is not investment advice or a buy/sell recommendation.

---

## Project status

```text
Status: Public-Source Complete v1
Coverage: 10 Indian listed companies
Research type: Institutional-style preliminary valuation research
Next phase: audited FY26 refresh + Excel dashboard automation
```

All companies in the current tracker now have:

- research note
- assumptions log
- source log
- peer framework
- numerical refresh summary
- research completion audit
- consolidated tracker entry

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

## Key project files

| File | Purpose |
|---|---|
| `docs/institutional_research_layer.md` | Defines the research standard and classification system |
| `outputs/valuation_summary/consolidated_research_tracker.md` | Tracks completion status of all company research packs |
| `outputs/valuation_summary/consolidated_valuation_dashboard.md` | Summarizes all 10 companies in one dashboard |
| `src/dcf_model.py` | Reusable DCF valuation skeleton |
| `src/piotroski_score.py` | Piotroski F-Score module |
| `scripts/build_hero_motocorp_dcf_model.py` | Example Excel DCF workbook builder |
| `scripts/build_consolidated_valuation_dashboard.py` | Builds the consolidated Excel dashboard workbook |
| `scripts/build_company_dcf_workbook_pack.py` | Builds the 10-company Excel DCF workbook pack |
| `scripts/beta_regression_pipeline.py` | Calculates reproducible beta estimates for WACC refresh |
| `scripts/peer_table_template_builder.py` | Creates a date-consistent peer-table refresh template |

---

## Project objective

The objective is to build a repeatable analyst-style framework for evaluating Indian equities.

The project moves from raw stock analysis to structured equity research:

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
```

The project aims to answer:

> Can a disciplined framework combining accounting quality, intrinsic valuation, source discipline, assumption tracking and risk analysis improve equity research quality compared with simple return analysis?

---

## Research classification

The repository uses the following classification for completed company research:

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
- beta regression
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

## Current project structure

```text
Indian-stock-return-analyzer/
│
├── README.md
├── AGENTS.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── calculations.py
│   ├── charts.py
│   ├── excel_export.py
│   ├── piotroski_score.py
│   └── dcf_model.py
│
├── scripts/
│   ├── build_hero_motocorp_dcf_model.py
│   ├── build_consolidated_valuation_dashboard.py
│   ├── build_company_dcf_workbook_pack.py
│   ├── beta_regression_pipeline.py
│   └── peer_table_template_builder.py
│
├── docs/
│   ├── methodology.md
│   ├── interview_notes.md
│   ├── equity_valuation_lab_blueprint.md
│   ├── valuation_methodology.md
│   ├── research_pipeline.md
│   └── institutional_research_layer.md
│
├── models/
│   └── company_dcf_models/
│       ├── hero_motocorp/
│       ├── natco_pharma/
│       ├── nalco/
│       ├── hindustan_zinc/
│       ├── cpcl/
│       ├── sharda_cropchem/
│       ├── fiem_industries/
│       ├── time_technoplast/
│       ├── force_motors/
│       └── triveni_turbine/
│
├── outputs/
│   ├── charts/
│   └── valuation_summary/
│       ├── consolidated_research_tracker.md
│       ├── consolidated_valuation_dashboard.md
│       ├── company_dcf_workbook_pack_v1.xlsx
│       ├── hero_motocorp_numerical_refresh_v1.md
│       ├── natco_pharma_numerical_refresh_v1.md
│       ├── nalco_numerical_refresh_v1.md
│       ├── hindustan_zinc_numerical_refresh_v1.md
│       ├── cpcl_numerical_refresh_v1.md
│       ├── sharda_cropchem_numerical_refresh_v1.md
│       ├── fiem_industries_numerical_refresh_v1.md
│       ├── time_technoplast_numerical_refresh_v1.md
│       ├── force_motors_numerical_refresh_v1.md
│       └── triveni_turbine_numerical_refresh_v1.md
│
└── paper/
    └── ssrn_working_paper_draft/
```

---

## Valuation methodology

The project uses FCFF DCF valuation for non-financial companies.

### FCFF formula

```text
FCFF = EBIT × (1 - Tax Rate) + Depreciation and Amortization - Capital Expenditure - Change in Net Working Capital
```

### WACC framework

```text
WACC = Cost of Equity × Equity Weight + After-tax Cost of Debt × Debt Weight
```

### Cost of equity framework

```text
Cost of Equity = Risk-free Rate + Beta × Equity Risk Premium + Company-Specific Risk Premium
```

### Terminal value

```text
Terminal Value = Final Year FCFF × (1 + Terminal Growth) / (WACC - Terminal Growth)
```

---

## Analyst checks applied to each company

Each company valuation includes:

- business overview
- industry context
- investment thesis
- growth-driver classification
- financial performance review
- DCF assumption justification
- WACC framework
- peer framework
- scenario analysis
- sensitivity framework
- risk matrix
- source log
- assumptions log
- data-quality status
- research completion audit

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

## Future upgrades

The next phase of this project should include:

1. audited FY26 annual report refresh
2. date-consistent peer numerical tables
3. beta regression review and WACC refinement
4. market-price refresh and valuation-range update
5. charts for fair value sensitivity and sector comparison
6. final research-paper style write-up

---

## Future research-paper direction

Possible working-paper title:

> From Screening to Intrinsic Value: A Practical Fundamental Research Framework for Indian Stocks

Possible research themes:

- DCF-implied undervaluation in Indian equities
- public-source equity research discipline
- Piotroski F-Score as a quality filter before valuation
- margin of safety and portfolio construction
- barbell strategy combining value and growth stocks
- WACC stress testing in Indian equity valuation
- sector-specific normalization across autos, pharma, metals, refining, agrochemicals and capital goods

---

## Disclaimer

This repository is for education, research practice and portfolio demonstration only. It does not provide investment advice, financial advice or buy/sell recommendations. All valuation outputs depend heavily on assumptions and must be independently verified before real investment use.
