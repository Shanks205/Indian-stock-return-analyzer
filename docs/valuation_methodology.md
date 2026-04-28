# Valuation Methodology

## Overview

This document explains the standardized valuation framework used in the Indian Equity Valuation Lab.

The methodology is designed to resemble the workflow of an investment banking or equity research analyst while remaining practical for a GitHub portfolio project.

## 1. Screening stage

The screening stage identifies companies that may be suitable for deeper valuation.

### Quality and financial health filters

Typical filters include:

- Market capitalization above a minimum liquidity threshold
- Positive operating cash flow
- Low debt-to-equity ratio
- Strong return on capital employed
- Strong return on equity
- Reasonable current ratio
- Low or no promoter pledge
- Positive sales and profit growth

### Value filters

Typical value filters include:

- Price-to-earnings below industry average
- Price-to-book within reasonable range
- EV/EBITDA compared with peers
- PEG ratio below a reasonable threshold
- Margin of safety from intrinsic value

### Growth filters

Typical growth filters include:

- 3-year and 5-year revenue growth
- 3-year and 5-year profit growth
- EPS growth
- expanding operating margins
- sector tailwinds
- market-share expansion

## 2. Piotroski F-Score

Piotroski F-Score is used as an accounting-quality filter. It ranges from 0 to 9.

The score is based on nine signals grouped into three categories:

### Profitability

1. Positive net income
2. Positive operating cash flow
3. Improvement in return on assets
4. Operating cash flow greater than net income

### Leverage, liquidity, and funding

5. Lower leverage than the previous year
6. Higher current ratio than the previous year
7. No equity dilution

### Operating efficiency

8. Higher gross margin than the previous year
9. Higher asset turnover than the previous year

A score of 7 to 9 usually indicates stronger accounting quality.

## 3. DCF framework

The project primarily uses free cash flow to firm valuation for non-financial companies.

### FCFF formula

FCFF = EBIT × (1 - tax rate) + depreciation and amortization - capital expenditure - change in net working capital

### Forecast period

The default forecast period is 5 years.

A 10-year forecast may be used for high-growth companies only when growth visibility is strong.

## 4. WACC framework

WACC is calculated as:

WACC = Cost of Equity × Equity Weight + After-tax Cost of Debt × Debt Weight

### Cost of equity

Cost of Equity = Risk-free Rate + Beta × Equity Risk Premium + Company-specific Risk Premium

### Risk-free rate

For Indian companies, the India 10-year government bond yield is used as the starting point.

### Equity risk premium

The equity risk premium should be based on a long-term market risk premium. Damodaran's datasets can be used as a reference source.

### Beta

Where possible, sector or peer-adjusted beta should be preferred over raw historical beta.

### Company-specific risk premium

This may be added for:

- small-cap companies
- cyclical companies
- companies with weak cash-flow conversion
- companies with governance risk
- companies with high customer concentration
- companies with higher liquidity risk

## 5. Terminal value

The standard approach is the Gordon growth method:

Terminal Value = Final Year FCFF × (1 + g) / (WACC - g)

Terminal growth should usually not exceed long-term nominal GDP growth.

For cyclical companies, terminal assumptions should be conservative.

## 6. Scenario analysis

Each company should have three valuation cases:

- Bear case
- Base case
- Bull case

These cases should vary:

- revenue growth
- EBITDA or EBIT margin
- reinvestment intensity
- WACC
- terminal growth

## 7. Sensitivity analysis

Every DCF should include sensitivity tables for:

- WACC vs terminal growth
- revenue growth vs operating margin
- margin of safety vs current market price

## 8. Risk-regime check

Before accepting the valuation output, the analyst should review:

- interest-rate environment
- inflation regime
- commodity cycle
- sector demand cycle
- valuation multiples in the market
- liquidity conditions
- currency sensitivity
- regulatory risk

## 9. AI attention-bias check

AI tools and online sources may overweight popular companies because they have more available data.

Each analysis should ask:

- Is this company popular because fundamentals are strong or because it receives attention?
- Are overlooked companies being ignored because less data exists?
- Does the valuation rely too much on a popular narrative?
- Are risks underrepresented in easily available online summaries?

## 10. Final decision framework

A company should be classified as:

- Strong DCF candidate
- Watchlist candidate
- Fairly valued
- Overvalued
- Avoid / insufficient data

The final view should combine:

- intrinsic value
- margin of safety
- business quality
- accounting quality
- growth visibility
- balance-sheet strength
- valuation sensitivity
- portfolio fit

## Disclaimer

The methodology is for education and research. It does not provide investment advice.
