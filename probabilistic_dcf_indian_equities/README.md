# From Screening to Probabilistic Intrinsic Value

## A Monte Carlo DCF Framework for Indian Equities

This project develops a probabilistic discounted cash flow valuation framework for Indian listed companies. It extends the earlier public-source DCF valuation project by converting deterministic valuation assumptions into probability distributions using Monte Carlo simulation.

Traditional DCF valuation often produces a single intrinsic value estimate based on fixed assumptions for revenue growth, margins, WACC, capital expenditure, working capital, and terminal growth. This project treats valuation as uncertain and generates a distribution of possible intrinsic values instead of one exact fair value.

## Project Objective

The objective is to build a reproducible Python-based valuation engine that can:

1. document the company selection process,
2. build deterministic FCFF DCF valuations,
3. convert key assumptions into probability distributions,
4. run Monte Carlo simulations,
5. estimate valuation ranges and probability of undervaluation,
6. compare uncertainty across different business models,
7. prepare outputs that can later support an SSRN working paper.

## Research Design

The project uses a 12-company Indian equity sample:

- 6 companies retained from the previous public-source valuation paper for continuity.
- 6 companies added through fresh Screener-style fundamental screening for originality.

The retained companies preserve continuity with the previous project. The newly selected companies improve sector diversity and allow broader testing of probabilistic valuation uncertainty.

## Final 12-Company Sample

| # | Company | Ticker | Source Type | Valuation Archetype |
|---:|---|---|---|---|
| 1 | Hero MotoCorp | HEROMOTOCO.NS | Retained | Mature auto cash-flow recovery |
| 2 | Fiem Industries | FIEMIND.NS | Retained | Auto-component growth |
| 3 | Triveni Turbine | TRITURBINE.NS | Retained | Capital goods / order-book conversion |
| 4 | NALCO | NATIONALUM.NS | Retained | Cyclical commodity |
| 5 | Sharda Cropchem | SHARDACROP.NS | Retained | Working-capital-sensitive agrochemical |
| 6 | Time Technoplast | TIMETECHNO.NS | Retained | Industrial packaging / cash conversion |
| 7 | Bharat Electronics | BEL.NS | New Screen | Defence electronics / order book |
| 8 | Polycab India | POLYCAB.NS | New Screen | Quality compounder / cables and electricals |
| 9 | SJS Enterprises | SJS.NS | New Screen | Auto ancillary / premiumization |
| 10 | Shilchar Technologies | SHILCTECH.NS | New Screen | High-ROCE industrial growth |
| 11 | JB Chemicals and Pharmaceuticals | JBCHEPHARM.NS | New Screen | Stable pharma |
| 12 | Gravita India | GRAVITA.NS | New Screen | Recycling / commodity-linked industrial |

## Project Structure

```text
probabilistic_dcf_indian_equities/
├── README.md
├── requirements.txt
├── data/
│   ├── company_master.csv
│   └── monte_carlo_distribution_template.csv
├── docs/
│   ├── sample_selection_protocol.md
│   └── valuation_methodology.md
├── src/
│   ├── dcf_model.py
│   └── monte_carlo_engine.py
└── companies/
    └── hero_motocorp/
        ├── company_readme.md
        └── assumptions_template.csv
```

## First Company

The first company to be built is **Hero MotoCorp** because it is a mature operating business with clearer DCF logic than highly cyclical or product-cycle-driven companies.

## Planned Workflow

```text
Company selection
→ Historical financial cleaning
→ Base FCFF DCF model
→ WACC and terminal value framework
→ Scenario assumptions
→ Monte Carlo distributions
→ Simulation output
→ Sensitivity analysis
→ Company-level valuation report
→ Consolidated uncertainty comparison
```

## Disclaimer

This project is for education, research practice, and portfolio demonstration only. It does not provide investment advice, financial advice, or buy/sell recommendations. All valuation outputs depend on assumptions and must be independently verified before real investment use.
