# Literature Review and Methodology Foundation

This document explains how selected investing, valuation, and portfolio-management books influence the Indian Equity Valuation Lab.

The purpose is not to copy book content, but to convert important ideas into a practical analyst workflow for screening, valuation, risk analysis, and future research-paper development.

## 1. Valuation foundation

### Main reference

- Aswath Damodaran — *Investment Valuation*

### Key ideas used in this project

Damodaran's valuation framework supports the idea that valuation should be connected to expected cash flows, growth, and risk. A stock should not be bought merely because someone else may pay a higher price later. The project therefore uses intrinsic valuation as the core framework.

Important principles incorporated:

- Value is linked to expected future cash flows.
- DCF valuation, relative valuation, and contingent-claim valuation are different approaches.
- FCFF should be discounted at WACC.
- FCFE should be discounted at cost of equity.
- Cash-flow and discount-rate mismatches can create misleading valuations.
- Valuation is not perfectly objective because assumptions introduce judgment.
- Valuations must be updated when new company, sector, or macro information arrives.
- DCF is easier for stable cash-flow companies and harder for cyclicals, distressed firms, financial firms, and companies undergoing restructuring.
- Relative valuation should be used as a cross-check, not as a replacement for intrinsic analysis.

### Project application

Every company DCF should include:

- model choice: FCFF, FCFE, bank valuation, cyclical normalized valuation, or relative valuation
- historical cash-flow analysis
- WACC build-up
- terminal value discipline
- sensitivity analysis
- relative valuation cross-check
- explicit explanation of assumptions

## 2. Stochastic DCF and valuation uncertainty

### Main reference

- Lutz Kruschwitz and Andreas Löffler — *Stochastic Discounted Cash Flow*

### Key ideas used in this project

This book provides a theoretical foundation for DCF under uncertainty. The project will not immediately implement the full stochastic valuation framework, but it will incorporate the idea that valuation depends on uncertain future cash flows and uncertain discount rates.

Important principles incorporated:

- DCF should recognize uncertainty rather than pretending that a single point estimate is exact.
- WACC, APV, and flow-to-equity are related valuation approaches but require consistent assumptions.
- Financing policy, tax treatment, and leverage assumptions can affect valuation.
- Scenario analysis and sensitivity analysis are practical ways to approximate uncertainty.

### Project application

The project will include:

- bear, base, and bull scenarios
- WACC stress testing
- terminal-growth sensitivity
- Monte Carlo simulation as a later enhancement
- explicit uncertainty rating for every valuation

## 3. Business-quality and growth-stock analysis

### Main references

- Philip A. Fisher — *Common Stocks and Uncommon Profits*
- Basant Maheshwari — *The Thoughtful Investor*

### Key ideas used in this project

Fisher-style investing emphasizes deep qualitative research, growth quality, management quality, and the importance of understanding a business beyond its reported numbers. Basant Maheshwari's work is especially relevant for Indian equities because it discusses growth, ROE, P/E expansion and contraction, sector cycles, and Indian market behavior.

Important principles incorporated:

- A high-quality company should have a long growth runway.
- Management quality matters.
- Market-share expansion and competitive advantage matter.
- Growth should be supported by business economics, not only by narrative.
- P/E expansion and contraction can strongly affect investor returns.
- Indian stocks require attention to sector cycles, promoter behavior, balance-sheet quality, and cash conversion.
- Price and value are different.

### Project application

Every company report should include a qualitative checklist:

- business model strength
- competitive moat
- market-share opportunity
- management quality
- reinvestment runway
- margin expansion potential
- customer concentration
- supplier concentration
- working-capital discipline
- accounting-quality red flags
- P/E expansion or contraction risk

## 4. Portfolio construction, diversification, and risk control

### Main references

- Daniel P. Palomar — *Portfolio Optimization: Theory and Application*
- Burton G. Malkiel — *A Random Walk Down Wall Street*

### Key ideas used in this project

Palomar's work supports a quantitative portfolio construction layer, including risk measures, robust portfolio methods, backtesting, drawdown, risk parity, index tracking, and advanced optimization. Malkiel's work adds an important reality check: many investors overestimate their ability to beat the market, and diversification, low costs, and disciplined long-term investing matter.

Important principles incorporated:

- Portfolio risk is not only about individual stock risk; correlations matter.
- Backtests can be misleading if they suffer from overfitting, look-ahead bias, survivorship bias, or data mining.
- Drawdown and downside risk should be tracked, not only volatility.
- Active stock selection should be compared against a passive benchmark.
- Rebalancing can reduce portfolio risk.
- A concentrated portfolio requires high conviction and strong research discipline.

### Project application

The future portfolio module should include:

- Nifty 50, Nifty 500, and midcap benchmark comparison
- portfolio return and volatility
- Sharpe ratio
- maximum drawdown
- downside risk
- beta
- Jensen's alpha
- correlation matrix
- position-size rules
- barbell allocation rules
- risk-parity or equal-weight comparison

## 5. Framework used in this project

The project combines the books into a practical workflow:

```text
Screening
→ Accounting quality check
→ Business-quality analysis
→ DCF valuation
→ Relative valuation cross-check
→ Scenario and sensitivity analysis
→ Margin-of-safety decision
→ Portfolio-fit score
→ Benchmark and risk comparison
```

## 6. Company-type model selection

| Company type | Preferred valuation approach |
|---|---|
| Stable non-financial company | FCFF DCF |
| Low-debt growth company | FCFF DCF + relative valuation |
| Bank / financial company | P/B, ROE, residual income, dividend discount model |
| Commodity / cyclical company | Normalized FCFF DCF + cycle analysis |
| Distressed company | Special situation / liquidation / probability-weighted scenarios |
| Very high-growth company | Extended DCF + scenario analysis + high MOS requirement |

## 7. Research-paper direction

The literature supports a future working paper with the following possible title:

**From Screening to Intrinsic Value: A Practical Fundamental Research Framework for Indian Stocks**

Possible research contribution:

- Build a repeatable Indian equity valuation framework.
- Combine Piotroski F-Score with DCF-implied margin of safety.
- Compare value and growth buckets in a barbell structure.
- Evaluate whether accounting quality and margin of safety improve portfolio selection.
- Add risk-adjusted performance comparison against Indian benchmarks.

## 8. Practical rule for this project

More books should not delay execution. The current literature base is sufficient for the first version.

The project should now focus on implementation:

1. Fill company data.
2. Run standardized valuations.
3. Build scenario analysis.
4. Create valuation summary outputs.
5. Write company research notes.
6. Build a final dashboard.
7. Convert the best insights into a research-paper draft.

## Disclaimer

This project is for education, research, and portfolio demonstration only. It does not provide investment advice or buy/sell recommendations.
