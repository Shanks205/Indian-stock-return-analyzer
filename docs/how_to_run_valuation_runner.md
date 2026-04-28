# How to Run the Batch Valuation Runner

This guide explains how to run the first automated DCF valuation workflow.

## Purpose

The batch valuation runner reads company-level valuation assumptions from a CSV file, runs a standardized FCFF DCF model, and exports a valuation summary.

This helps convert the project from one-off Excel models into a repeatable research workflow.

## Input file

Default input file:

```text
data/templates/valuation_inputs_template.csv
```

Each company row should include:

- ticker
- company name
- current price
- shares outstanding
- net debt
- current FCFF
- 5-year growth assumptions
- WACC
- terminal growth
- required margin of safety
- source notes
- analyst notes

Companies with incomplete inputs are skipped automatically.

## Output file

Default output file:

```text
outputs/valuation_summary/valuation_summary.csv
```

The output includes:

- intrinsic value per share
- upside/downside
- required margin of safety
- buy-zone price
- enterprise value
- equity value
- present value of forecast cash flows
- present value of terminal value
- final view

## How to run

From the project root, run:

```bash
python src/valuation_runner.py
```

## Important note

This automation does not replace analyst judgment.

The runner only calculates valuation based on the assumptions provided. The quality of the valuation still depends on:

- annual-report analysis
- quarterly-result analysis
- earnings-call commentary
- industry outlook
- WACC assumptions
- terminal growth assumptions
- margin-of-safety discipline

## Recommended workflow

1. Collect financials and sources.
2. Fill the valuation input CSV.
3. Run the valuation runner.
4. Review the output.
5. Stress-test assumptions.
6. Write an analyst summary.
7. Update the valuation summary dashboard.

## Next improvement

Future versions can add:

- bear/base/bull scenario automation
- WACC sensitivity tables
- terminal-growth sensitivity tables
- charts
- Excel export
- automated source-log generation
