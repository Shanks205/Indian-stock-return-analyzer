# From Screening to Intrinsic Value: A Public-Source DCF Valuation Framework for Indian Equities

**Working Paper, Version 1.4**  
**Date written:** April 2026  
**Framework valuation date:** 29 April 2026  
**Paper type:** Working Paper  

**Himanshu Dabi**  
Independent Researcher, India  
MSc in International Management  
Email: dabihithim@gmail.com  

**Hitesh Dabi**  
Independent Researcher, India  
MSc in International Management  
Email: hiteshdabi@ymail.com  

**Corresponding author:** Himanshu Dabi, dabihithim@gmail.com  

## Abstract

This working paper develops a reproducible public-source valuation framework for Indian listed equities. It begins with fundamental screening and Piotroski-style quality checks, organizes the sample through a barbell research design, and applies a free cash flow to the firm (FCFF) discounted cash flow (DCF) framework across ten Indian companies. The objective is not to issue investment recommendations, but to demonstrate how public company disclosures can be converted into transparent valuation assumptions, risk matrices, and sector-specific normalization rules.

The main finding is that a single generic valuation template is insufficient across sectors. Metals companies require mid-cycle commodity assumptions, refiners require normalized gross refining margin analysis, pharmaceutical companies require product-cycle and pipeline adjustments, auto and auto-component companies require customer and platform-risk analysis, and capital-goods companies require order-book and execution-risk analysis. The paper contributes a practical framework for moving from stock screening to intrinsic-value research while maintaining clear data-quality boundaries. Final per-share valuation conclusions are deliberately excluded from this version until audited annual-report reconciliation, verified share counts, date-consistent market prices, and beta regression review are completed.

**Keywords:** Indian equities; equity valuation; discounted cash flow; DCF; fundamental analysis; valuation methodology; public-source data; corporate finance; equity research; sector normalization; emerging markets; financial modelling.

**JEL Classification:** G11, G12, G17, G32.

## Author Note

Both authors are independent researchers based in India and hold an MSc in International Management. The associated project repository is available at: https://github.com/Shanks205/Indian-stock-return-analyzer

## Funding Statement

This research received no external funding.

## Conflict of Interest Statement

The authors declare no conflict of interest. The authors do not currently hold positions in any of the companies included in the study as of the finalization of this working paper version. This paper does not provide investment advice, financial advice, or buy/sell recommendations for any company discussed in the study.

## Data Availability Statement

The research framework, company notes, dashboards, and supporting code are available in the project GitHub repository. The company-level financial data are based on publicly available company filings, investor presentations, exchange disclosures, and public market sources.

## Acknowledgments

The authors thank open-source financial data providers and public company disclosures that made this research possible.

## AI Use Statement

The authors used AI tools for language refinement, editing support, document organization, and code scaffolding. The research design, sample selection, valuation assumptions, numerical outputs, data verification, analysis, interpretation, and conclusions were independently constructed, reviewed, and approved by the authors, who take full responsibility for the manuscript. AI tools were not used as authors and were not treated as sources of independent research judgment.

## 1. Introduction

Equity research is often introduced through stock returns, price charts, valuation multiples, or simple screening filters. These tools are useful, but they do not by themselves establish intrinsic value. A low price-to-earnings ratio may reflect a cyclical earnings peak, while a high multiple may reflect stronger future cash-flow durability. A serious valuation process requires a link between business model, financial statements, industry context, cash-flow generation, reinvestment needs, and the cost of capital.

This working paper develops a public-source valuation framework for Indian equities. The study is designed as a methodological and applied case-study paper. It does not attempt to prove that the selected companies are mispriced, nor does it issue buy or sell recommendations. Instead, it demonstrates how a structured research workflow can move from fundamental screening to company-specific DCF assumptions, risk analysis, peer frameworks, and reproducible Python/Excel outputs.

The sample contains ten Indian listed companies: Hero MotoCorp, Natco Pharma, NALCO, Hindustan Zinc, CPCL, Sharda Cropchem, Fiem Industries, Time Technoplast, Force Motors, and Triveni Turbine. These companies were selected to create business-model diversity across autos, pharmaceuticals, metals, refining, agrochemicals, industrial packaging, auto components, and capital goods. The selection is intentionally practical rather than statistically random.

The paper's central contribution is a reproducible public-source valuation methodology with sector-specific normalization rules. This contribution is important because common valuation errors often come from applying a generic DCF template without adjusting for sector economics. For example, aluminium and zinc producers require mid-cycle commodity assumptions, refiners require GRM normalization, pharmaceutical companies require product-cycle analysis, and capital-goods companies require order-book conversion analysis.

## 2. Research Problem and Objectives

Most beginner-level equity projects focus on stock returns, charts, valuation multiples, or mechanical screeners. These approaches are useful for idea generation, but they often fail to connect business-model differences with valuation assumptions. A company may appear cheap because earnings are temporarily inflated, or expensive because near-term earnings understate long-term cash-flow potential.

The research problem can be stated as follows:

**How can a disciplined public-source valuation framework be designed to evaluate Indian listed companies across sectors while avoiding over-extrapolation of recent earnings, commodity cycles, one-off gains, and sector-specific margin peaks?**

The main objective is to develop and demonstrate a public-source, reproducible equity valuation framework for Indian listed companies using fundamental screening, Piotroski-style quality checks, barbell research design, FCFF DCF, WACC construction, peer-comparison design, risk matrices, source logs, and sector-specific normalization.

Specific objectives are:

1. To build a structured public-source valuation framework for Indian equities.
2. To explain how the sample companies were selected through screening and analyst judgement.
3. To apply the framework to ten Indian listed companies across different sectors.
4. To identify how DCF assumptions differ by sector and business model.
5. To produce consolidated framework outputs from a common valuation date.
6. To distinguish public-source working-paper outputs from final institutional-grade valuation outputs.

## 3. Research Questions and Methodological Propositions

The main research question is:

**Can a structured public-source valuation framework improve the transparency and consistency of Indian equity research compared with simple return or ratio-based analysis?**

Supporting research questions and answers are summarized in Table 1.

**Table 1. Research questions and framework answers**

| Research question | Answer from the framework |
|---|---|
| RQ1: Does screening improve research selection? | Yes, as a first-stage narrowing device, but not as a final recommendation rule. Screening improved research discipline by combining valuation, profitability, balance-sheet and cash-flow checks before DCF. |
| RQ2: How should assumptions be normalized? | By sector: commodity margins for metals, GRMs for refining, product-cycle earnings for pharma, working capital for agrochemicals, customer/program risk for autos, and order-book conversion for capital goods. |
| RQ3: How should WACC risk be documented? | By separating risk-free rate, beta/benchmark logic, equity risk premium and company-specific risk premiums, while marking beta regression as a later empirical refinement. |
| RQ4: What role should peer comparison play? | Peer multiples are used as a sanity check only. They are not a replacement for intrinsic valuation because peers differ in mix, cyclicality, leverage and growth visibility. |
| RQ5: What are public-data limits? | Public data supports a disciplined working paper, but audited financial statement reconciliation, verified share counts and date-consistent market prices are needed before final per-share valuation. |
| RQ6: How does automation help? | Python and Excel templates make assumptions, dashboards, DCF outputs, beta regression and peer refresh workflows reproducible and auditable. |

Instead of formal statistical hypotheses, this working paper uses methodological propositions because the study is a framework application rather than a large-sample econometric test.

**Proposition 1:** A structured DCF framework with assumption logs improves transparency relative to ratio-only analysis.

**Proposition 2:** Sector-specific normalization changes the interpretation of company quality and valuation risk.

**Proposition 3:** Screening and Piotroski-style quality checks are useful for research selection, but they do not replace company-level valuation.

**Proposition 4:** Python and Excel automation improve reproducibility by making assumptions, output tables, and refresh workflows auditable.

## 4. Literature and Conceptual Background

The paper draws on established work in fundamental analysis, valuation, portfolio theory, and financial statement analysis. Graham and Dodd (1934) established a disciplined tradition of security analysis based on intrinsic value and margin of safety. Markowitz (1952) emphasized the risk-return trade-off in portfolio selection, while Sharpe (1964) formalized systematic risk in asset pricing. Fama and French (1992, 1993) expanded risk-factor thinking beyond market beta.

DCF valuation remains central in corporate finance because it connects expected cash flows, reinvestment, growth, and risk (Damodaran, 2012; Koller, Goedhart, and Wessels, 2020). Damodaran's country-risk and equity-risk-premium framework is particularly relevant for emerging-market valuation because it supports explicit country and company-specific risk adjustments when estimating the cost of equity. Financial statement analysis emphasizes that earnings quality, accruals, cash conversion, leverage, and operating efficiency matter for interpreting reported performance (Penman, 2013; Sloan, 1996). Piotroski (2000) shows that profitability, leverage/liquidity, and operating efficiency signals can improve the evaluation of value stocks.

For the Indian market context, market-efficiency and microstructure studies suggest that Indian equities must be analysed with attention to liquidity, information efficiency, and market structure. Elangovan, Irudayasamy, and Parayitam (2022) examine Indian market efficiency using broad market indices. Roy and Chakraborty (2020) examine efficiency and dynamic linkages in Indian equity futures markets. Prakash and Sahu (2020) study weak-form efficiency at index and scrip levels in India. These streams support the need for careful public-data interpretation rather than purely mechanical price-based analysis.

## 5. Data, Sample Selection, and Research Design

### 5.1 Sample Construction

The companies were selected through a practical stock-screening process followed by analyst judgement. The screen considered valuation, profitability, growth, balance-sheet strength, cash-flow discipline, liquidity, and Piotroski-style quality indicators. The screening stage was used to narrow the research universe; it was not treated as a mechanical buy/sell system.

Screening dimensions included:

- valuation: P/E, P/B, EV/EBITDA where available, and PEG-style interpretation;
- profitability: ROE, ROCE, operating margin, and net profit margin;
- growth: sales growth, profit growth, and sector growth drivers;
- balance sheet: debt-to-equity, interest coverage, and liquidity profile;
- cash flow: operating cash flow, free cash flow, and working-capital behaviour;
- quality: Piotroski-style profitability, leverage/liquidity, and efficiency checks;
- market sanity: liquidity, market capitalization, and abnormal price/volume behaviour.

### 5.2 Barbell Research Design

The final sample was organized using a barbell research design. The purpose was not portfolio allocation; it was research coverage. The first side includes core value/quality companies where downside discipline and normalized earnings are central. The second side includes growth/satellite companies where operating leverage, product optionality, and execution risk are more important.

**Table 2a. Core value / quality companies and valuation focus**

| Company | Sector | Key analytical focus | Main DCF driver |
|---|---|---|---|
| Hero MotoCorp | Auto / Two-wheelers | Mature demand, premiumisation, EV optionality and competition risk | Two-wheeler recovery and margin stability |
| Natco Pharma | Pharma / Complex generics | Product-cycle normalization, pipeline optionality and regulatory risk | Normalized pipeline-backed earnings |
| NALCO | Metals / Aluminium | Mid-cycle aluminium/alumina margins and commodity-price risk | Alumina/aluminium margins |
| Hindustan Zinc | Metals / Zinc-Silver | Zinc/silver cycle normalization and capital-allocation risk | Normalized mining margin |
| CPCL | Oil & Gas / Refining | Normalized GRM, inventory cycle and refining margin compression | Mid-cycle refining margin |
| Sharda Cropchem | Agrochemicals | Working-capital discipline, receivables, destocking and registration risk | Registration-led recovery and cash conversion |

**Table 2b. Growth / satellite companies and valuation focus**

| Company | Sector | Key analytical focus | Main DCF driver |
|---|---|---|---|
| Fiem Industries | Auto Components | Customer concentration, two-wheeler cycle and margin normalization | LED content and two-wheeler volumes |
| Time Technoplast | Industrial Packaging / Polymers | Value-added mix, raw-material volatility and working-capital risk | Value-added packaging and composite products |
| Force Motors | Auto / Vans & Engines | Exceptional-item normalization, auto-cycle risk and platform concentration | Urbania/Traveller and engine manufacturing |
| Triveni Turbine | Capital Goods / Turbines | Order-book conversion, export growth and margin sustainability | Export orders and aftermarket mix |

### 5.3 Data Sources and Valuation Date

The study uses public company filings, annual reports, quarterly result releases, investor presentations, exchange disclosures, and public market sources. The framework valuation date is **29 April 2026**. The numerical outputs in this working paper are model-implied enterprise-value outputs from common DCF assumptions. Per-share fair values and upside/downside comparisons are not presented in this version because final share counts, net debt/cash, and market prices should be locked from a single verified source before public valuation conclusions are drawn.

## 6. Methodology

### 6.1 FCFF DCF Framework

The paper uses FCFF as the central intrinsic valuation framework:

**FCFF = EBIT x (1 - Tax Rate) + Depreciation and Amortization - Capital Expenditure - Change in Net Working Capital**

FCFF is useful because it values operating cash flows available to all capital providers and allows comparison across different capital structures.

### 6.2 WACC Framework

The discount rate is structured using:

**WACC = Cost of Equity x Equity Weight + After-tax Cost of Debt x Debt Weight**

The cost of equity is organized as:

**Cost of Equity = Risk-free Rate + Beta x Equity Risk Premium + Company-Specific Risk Premium**

In this working-paper version, WACC values are model assumptions documented for framework consistency. The dispersion in WACC across the sample is driven primarily by differences in business risk, cyclicality, margin durability, capital intensity, and company-specific risk premiums layered above the base equity-risk-premium framework. The WACC framework is consistent with firm-level valuation logic in which operating assets are valued using the blended opportunity cost of capital across capital providers; this connects the DCF framework to the capital-structure literature associated with Modigliani and Miller (1958). For example, CPCL carries a higher WACC because refining earnings are exposed to GRM volatility, crude inventory effects, regulatory risk, and higher operating cyclicality, while Natco Pharma's WACC is lower in the framework because the model treats its balance-sheet profile and asset intensity more conservatively despite product-cycle risk. A beta regression pipeline is included in the repository for later refinement.

### 6.3 Terminal Value

Terminal value is estimated using:

**Terminal Value = Final Year FCFF x (1 + Terminal Growth) / (WACC - Terminal Growth)**

Terminal growth is kept conservative because terminal value can dominate DCF output.

### 6.4 Scenario and Sensitivity Analysis

Each company framework includes bear, base, and bull case logic. In this paper, the consolidated results table reports base-case DCF outputs. The repository contains the workbook structure for WACC and terminal-growth sensitivity analysis.

### 6.5 Peer Framework

Peer comparison is used as a sanity check, not as a substitute for intrinsic valuation. Peer multiples should only be interpreted after adjusting for business mix, cyclicality, leverage, margin structure, and growth visibility.

## 7. Consolidated Framework Outputs

Table 3 reports consolidated base-case DCF framework outputs. These are not target prices and not investment recommendations. They are enterprise-value outputs generated from the public-source assumptions documented in the project.

**Table 3a. Consolidated base-case operating and discount-rate assumptions**  
*Values in INR crore unless stated otherwise.*

| Company | FY26E revenue | FY27 growth | FY27 EBITDA margin | WACC | Terminal growth |
|---|---|---|---|---|---|
| Hero MotoCorp | 46,300 | 8.0% | 15.0% | 12.58% | 4.0% |
| Natco Pharma | 3,790 | -36.7% | 24.4% | 11.31% | 4.0% |
| NALCO | 17,200 | 3.0% | 36.0% | 15.68% | 3.5% |
| Hindustan Zinc | 40,000 | 3.0% | 52.0% | 14.98% | 3.5% |
| CPCL | 75,000 | 2.0% | 6.0% | 16.88% | 3.0% |
| Sharda Cropchem | 4,400 | 8.0% | 17.5% | 14.78% | 3.5% |
| Fiem Industries | 2,750 | 10.0% | 14.0% | 15.13% | 4.0% |
| Time Technoplast | 6,000 | 8.0% | 15.0% | 14.88% | 4.0% |
| Force Motors | 8,800 | 9.0% | 15.5% | 15.83% | 4.0% |
| Triveni Turbine | 2,100 | 14.0% | 23.5% | 14.88% | 4.0% |

*Note: Natco Pharma's -36.7% FY27 revenue growth reflects product-cycle normalization rather than a structural long-term decline assumption.*

**Table 3b. Consolidated base-case DCF framework outputs**  
*Values in INR crore unless stated otherwise.*

| Company | DCF EV | EV/Rev | EV/EBITDA |
|---|---|---|---|
| Hero MotoCorp | 57,844 | 1.25x | 8.33x |
| Natco Pharma | 6,466 | 1.71x | 6.99x |
| NALCO | 20,876 | 1.21x | 3.37x |
| Hindustan Zinc | 96,276 | 2.41x | 4.63x |
| CPCL | 2,645 | 0.04x | 0.59x |
| Sharda Cropchem | 4,639 | 1.05x | 6.02x |
| Fiem Industries | 1,897 | 0.69x | 4.93x |
| Time Technoplast | 4,905 | 0.82x | 5.45x |
| Force Motors | 5,254 | 0.60x | 3.85x |
| Triveni Turbine | 3,541 | 1.69x | 7.18x |

*Notes: EV/Rev = DCF-implied enterprise value divided by FY26E revenue. EV/EBITDA = DCF-implied enterprise value divided by FY26E EBITDA.*

The table shows that the framework produces materially different valuation profiles across sectors. Hindustan Zinc receives a higher EV/revenue ratio because of structurally high mining margins, while CPCL receives a very low EV/revenue ratio because refining revenue is large relative to normalized margins. CPCL's output should therefore be interpreted through earnings-based multiples rather than revenue multiples: normalized GRM compression, capital intensity, inventory exposure, and a higher WACC structurally reduce DCF value relative to its revenue base. The added EV/EBITDA column helps make this distinction visible and supports the paper's argument that revenue-based comparison is misleading across sectors with very different margin structures. Triveni Turbine and Natco Pharma show higher EV/revenue ratios than many industrial companies because the base assumptions reflect stronger margin quality and lower normalized capital intensity. These outputs are useful as framework results, but not as final per-share valuation conclusions.

## 8. Company-Level Application

Hero MotoCorp is treated as a mature two-wheeler company where the key risk is overcapitalizing premiumisation and EV optionality. Natco Pharma is treated as a complex generics company where product-cycle earnings must be normalized. NALCO and Hindustan Zinc are treated as commodity-linked businesses where mid-cycle margins matter more than recent peak-cycle earnings. CPCL is treated as a refiner where normalized GRM is more important than reported revenue growth.

Sharda Cropchem is treated as an asset-light agrochemical company where cash conversion and receivables are central. Fiem Industries is treated as a two-wheeler-linked auto-component supplier where customer concentration and margin sustainability matter. Time Technoplast is treated as a value-added industrial packaging company where growth must be tested against raw-material and working-capital risk. Force Motors is treated as an auto/OEM and engine manufacturing company where exceptional gains must be separated from recurring operating profit. Triveni Turbine is treated as a capital-goods company where order-book conversion, export growth, and margin durability drive valuation.

## 9. Cross-Company Findings

The first finding is that screening improves research selection but is not sufficient for valuation. The screener helped identify companies with reasonable valuation, profitability, balance-sheet, and quality characteristics, but DCF assumptions still needed company-specific judgement.

The second finding is that sector normalization materially changes interpretation. NALCO and Hindustan Zinc cannot be interpreted using peak commodity margins, CPCL cannot be interpreted using only revenue scale, and Force Motors cannot be interpreted using exceptional gains as recurring earnings.

The third finding is that margin structure drives DCF output more than revenue scale. CPCL has the largest FY26E revenue base in the sample but a low DCF EV/revenue output because refining margins normalize sharply. Its low EV/EBITDA ratio in the base framework also shows how normalized refining economics can produce a materially different valuation interpretation from revenue scale alone. Hindustan Zinc and Triveni Turbine have smaller revenue bases but higher output intensity because normalized margins are stronger.

The fourth finding is that working capital is a valuation risk, not just an accounting item. Sharda Cropchem and Time Technoplast illustrate how accounting profit must be tested against receivables, inventory, and cash conversion.

The fifth finding is that peer comparison is useful but dangerous when used mechanically. Peer sets help create valuation discipline, but a company with different cyclicality, leverage, customer concentration, or margin quality should not be valued by directly copying peer multiples.

The sixth finding is that reproducible documentation improves credibility. Assumption logs, source logs, dashboards, and workbook generators make the framework auditable and reduce the risk of hidden assumptions.

## 10. Discussion

The framework is most useful as a structured path from idea generation to valuation discipline. It does not remove judgement; it organizes judgement. The analyst still must decide which growth, margin, WACC, capex, and working-capital assumptions are reasonable. The contribution is that the framework makes those decisions explicit and reviewable.

The framework also helps prevent a common valuation error: confusing a good company with a good investment. A company can have strong operations but still be expensive if the market already discounts optimistic assumptions. Conversely, a company with temporary weakness may still be attractive if normalized cash flows are higher than current earnings suggest.

## 11. Limitations

This study has several limitations. First, the sample includes ten companies selected through screening and business-model diversity, not statistical random sampling. Second, the research uses public-source data and preliminary assumptions. Third, final per-share valuation outputs are excluded until audited financial statement reconciliation, verified share counts, net debt/cash reconciliation, and date-consistent market prices are available. Fourth, beta regression and peer numerical tables remain future refinements. Fifth, the paper does not test market outperformance or portfolio returns.

The paper does not provide investment advice, financial advice, or buy/sell recommendations. The valuation framework is intended for education and methodological research.

## 12. Conclusion

This paper developed a public-source DCF valuation framework for Indian listed equities and applied it to ten companies selected through stock screening, Piotroski-style quality checks, barbell research design, and business-model diversity. The study shows that a disciplined research workflow can improve valuation transparency by combining DCF modelling, WACC frameworks, peer comparison, scenario analysis, sensitivity analysis, risk matrices, source logs, assumption logs, and Python/Excel automation.

The main contribution is methodological. The paper demonstrates that valuation must be adapted to business model and sector. Commodity companies require mid-cycle margin normalization, refiners require GRM normalization, pharmaceutical companies require product-cycle and pipeline analysis, auto suppliers require customer concentration analysis, and capital-goods companies require order-book conversion analysis.

Future versions can improve empirical strength by incorporating audited FY26 data, regression-derived betas, date-consistent peer tables, price-to-value comparisons, and a worked company-level DCF example.

## References

Altman, E. I. (1968). Financial ratios, discriminant analysis and the prediction of corporate bankruptcy. *The Journal of Finance*, 23(4), 589-609.

Damodaran, A. (2012). *Investment Valuation: Tools and Techniques for Determining the Value of Any Asset*. Wiley.

Damodaran, A. (2024). *Applied Corporate Finance*. Wiley.

Elangovan, R., Irudayasamy, F. G., and Parayitam, S. (2022). Testing the market efficiency in Indian stock market: Evidence from Bombay Stock Exchange broad market indices. *Journal of Economics, Finance and Administrative Science*, 27(54), 313-327.

Fama, E. F., and French, K. R. (1992). The cross-section of expected stock returns. *The Journal of Finance*, 47(2), 427-465.

Fama, E. F., and French, K. R. (1993). Common risk factors in the returns on stocks and bonds. *Journal of Financial Economics*, 33(1), 3-56.

Graham, B., and Dodd, D. L. (1934). *Security Analysis*. McGraw-Hill.

Koller, T., Goedhart, M., and Wessels, D. (2020). *Valuation: Measuring and Managing the Value of Companies*. Wiley.

Markowitz, H. (1952). Portfolio selection. *The Journal of Finance*, 7(1), 77-91.

Modigliani, F., and Miller, M. H. (1958). The cost of capital, corporation finance and the theory of investment. *The American Economic Review*, 48(3), 261-297.

Penman, S. H. (2013). *Financial Statement Analysis and Security Valuation*. McGraw-Hill Education.

Piotroski, J. D. (2000). Value investing: The use of historical financial statement information to separate winners from losers. *Journal of Accounting Research*, 38, 1-41.

Prakash, A. S., and Sahu, D. (2020). Empirical study of weak form of efficiency in the Indian stock market at index level and scrip level. *Management Insight*, 9(2), 90-101.

Roy, P. S., and Chakraborty, T. (2020). Efficiency of Indian equity futures market: An empirical analysis with reference to National Stock Exchange. *Global Business Review*.

Sharpe, W. F. (1964). Capital asset prices: A theory of market equilibrium under conditions of risk. *The Journal of Finance*, 19(3), 425-442.

Sloan, R. G. (1996). Do stock prices fully reflect information in accruals and cash flows about future earnings? *The Accounting Review*, 71(3), 289-315.

SSRN Support Center. (2025). SSRN policy on generative AI and AI-assisted technologies. Elsevier/SSRN Support.

SSRN Support Center. (2026). What is required to submit a paper to SSRN? Elsevier/SSRN Support.

## Appendix A. Screening and Sample Construction Logic

| Screening Dimension | Examples of Variables Reviewed | Research Purpose |
|---|---|---|
| Valuation | P/E, P/B, EV/EBITDA, PEG-style interpretation | Identify companies requiring deeper valuation review |
| Profitability | ROE, ROCE, operating margin, net margin | Test capital efficiency and business quality |
| Growth | Sales growth, profit growth, sector drivers | Separate structural growth from cyclical growth |
| Balance sheet | Debt-to-equity, interest coverage, liquidity | Avoid financially stressed value traps |
| Cash flow | CFO, FCF, working-capital behaviour | Check whether accounting profits convert into cash |
| Piotroski-style quality | Profitability, leverage/liquidity, operating efficiency | Add quality discipline to screening |
| Market sanity | Liquidity, market capitalization, abnormal price/volume | Avoid extremely illiquid or speculative cases |

## Appendix B. Reproducibility Files

The project repository contains research notes, source logs, assumptions logs, peer frameworks, consolidated dashboards, DCF workbook templates, beta regression pipeline, and peer-table refresh template.

## Appendix C. Disclaimer

This working paper and associated project are for educational and research purposes only. They do not constitute investment advice, financial advice, or buy/sell recommendations. All outputs depend on assumptions and should be independently verified before real investment use.
