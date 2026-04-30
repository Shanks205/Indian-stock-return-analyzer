# From Screening to Intrinsic Value: A Public-Source Fundamental Valuation Framework for Indian Equities

**Himanshu Dabi**  
Independent Researcher, India  
MSc in International Management  
Email: dabihithim@gmail.com

**Hitesh Dabi**  
Independent Researcher, India  
MSc in International Management  
Email: hithimdabi206@gmail.com

**Corresponding author:** Himanshu Dabi, dabihithim@gmail.com  
**Date written:** April 2026  
**Paper type:** Working Paper

## Abstract

This paper develops a public-source fundamental valuation framework for Indian listed equities and applies it to ten companies across autos, pharmaceuticals, metals, refining, agrochemicals, industrial packaging, auto components, and capital goods. The study moves beyond simple return, ratio, and screening-based analysis by integrating free cash flow to the firm (FCFF) discounted cash flow (DCF) modelling, weighted average cost of capital (WACC) construction, peer-comparison design, scenario analysis, sensitivity analysis, risk matrices, source logs, assumption tracking, and Python/Excel automation. The central contribution is methodological: the paper demonstrates how sector-specific normalization can improve valuation discipline by preventing over-extrapolation of recent earnings, commodity-cycle margins, refining spreads, product-cycle profits, and one-off gains.

The framework is implemented through company-level research notes, numerical DCF summaries, Python scripts, and Excel dashboards. The results show that valuation logic must differ materially by business model. Commodity companies require mid-cycle margin assumptions; refiners require normalized gross refining margin (GRM) analysis; pharma companies require pipeline and product-cycle adjustments; auto suppliers require customer-concentration analysis; and capital-goods companies require order-book and execution-risk analysis. The paper also introduces a data-quality classification that separates "Public-Source Complete v1" research from fully institutional-grade research, highlighting the need for audited annual-report reconciliation, live market data, peer numerical tables, and beta regression before final valuation use. The study contributes a practical, reproducible, and transparent framework for early-stage equity research and finance portfolio development in the Indian market.

**Keywords:** Equity valuation; Indian equities; DCF; WACC; fundamental analysis; equity research; public-source research; financial modelling; peer comparison; risk analysis; Python; Excel dashboard.

## Author Note

Both authors are independent researchers based in India and hold an MSc in International Management. The authors developed this work as a finance research and valuation-methodology project. The associated project repository is available at: https://github.com/Shanks205/Indian-stock-return-analyzer

## Funding Statement

This research received no external funding.

## Conflict of Interest and Personal Holding Disclosure

The authors declare no external conflict of interest. One author has held shares of Fiem Industries for more than six months. This personal holding is disclosed for transparency. The paper does not provide investment advice, financial advice, or buy/sell recommendations for Fiem Industries or any other company discussed in the study.

## Data Availability Statement

The research framework, company notes, dashboards, and supporting code are available in the project GitHub repository. The company-level financial data are based on publicly available company filings, investor presentations, exchange disclosures, and public market sources.

## Acknowledgments

The authors thank open-source financial data providers and public company disclosures that made this research possible.

## AI Disclosure Statement

The authors used AI tools to assist with drafting, structuring, documentation, wording refinement, and code-generation support. The authors remain responsible for the research design, interpretation, assumptions, data verification, final manuscript content, and all conclusions. AI-generated content was reviewed and edited by the authors before submission. AI tools were not listed as authors and are not cited as authors.

## 1. Introduction

Equity research is often introduced through stock returns, price charts, valuation multiples, and simple screening filters. These tools are useful, but they are not sufficient to understand intrinsic value. A low price-to-earnings ratio does not automatically indicate undervaluation, and a strong recent quarter does not automatically represent sustainable earnings power. Valuation requires a structured link between business model, financial statements, industry context, risk, cash flow generation, and cost of capital.

This paper develops and applies a public-source fundamental valuation framework for Indian listed companies. The framework is designed for early-career analysts, finance students, and independent researchers who want to move beyond basic stock screening toward a disciplined research workflow. The paper applies the framework to ten Indian listed companies across autos, pharma, metals, refining, agrochemicals, industrial packaging, auto components, and capital goods. The selected companies are Hero MotoCorp, Natco Pharma, National Aluminium Company (NALCO), Hindustan Zinc, Chennai Petroleum Corporation (CPCL), Sharda Cropchem, Fiem Industries, Time Technoplast, Force Motors, and Triveni Turbine.

The purpose of the study is not to provide buy, sell, or hold recommendations. Instead, the purpose is methodological. The paper asks how a structured public-source valuation process can improve transparency, assumption discipline, and sector-specific judgement in Indian equity research. The project behind the paper includes company research notes, assumptions logs, source logs, peer frameworks, risk matrices, numerical DCF summaries, completion audits, a consolidated valuation dashboard, a ten-company Excel DCF workbook pack, a beta regression pipeline, and a peer-table refresh template.

The paper deliberately uses the classification "Public-Source Complete v1." This means that the research is complete for educational, portfolio, and interview-discussion purposes, but it is not presented as fully institutional-grade published research. A fully institutional-grade version would require audited FY26 annual-report reconciliation, verified share counts, net debt and cash reconciliation, date-consistent market prices, peer numerical tables, regression beta review, and independent model validation.

The central argument of this paper is that valuation is not one-size-fits-all. A mature two-wheeler company, a complex generics pharma company, an aluminium producer, a refiner, an agrochemical registration-led business, an auto-component supplier, a polymer packaging company, an auto manufacturer, and a turbine capital-goods company all require different normalization logic. A useful valuation framework must therefore combine common modelling discipline with sector-specific judgement.

## 2. Research Problem, Objectives, Questions, and Hypotheses

### 2.1 Research Problem

Most beginner-level equity analysis projects focus on stock returns, charts, valuation multiples, or simple screening criteria. These approaches often fail to connect business-model differences with intrinsic valuation assumptions. A company may look cheap on a historical earnings multiple because its earnings are at a cyclical peak, or it may look expensive because current reported earnings understate future normalized cash flows. Without a structured framework, analysts may over-extrapolate recent performance, ignore working-capital risk, or apply peer multiples mechanically across companies with different business models.

The research problem can be stated as follows:

**How can a disciplined public-source valuation framework be designed to evaluate Indian listed companies across sectors while avoiding over-extrapolation of recent earnings, commodity cycles, one-off gains, and sector-specific margin peaks?**

### 2.2 Main Research Objective

The main objective is to develop and demonstrate a public-source, reproducible equity valuation framework for Indian listed companies using FCFF DCF, WACC construction, peer-comparison design, risk matrices, source logs, and sector-specific normalization.

### 2.3 Specific Research Objectives

1. To build a structured public-source valuation framework for Indian equities.
2. To apply the framework to ten Indian listed companies across different sectors.
3. To examine how DCF assumptions differ by sector and business model.
4. To identify the key valuation risks for each sector.
5. To design a reproducible Python/Excel workflow for valuation documentation and dashboarding.
6. To distinguish complete public-source research from institutional-grade audited research.

### 2.4 Research Questions

The main research question is:

**Can a structured public-source valuation framework improve the quality and transparency of Indian equity research compared with simple return or ratio-based analysis?**

Supporting research questions are:

1. How should DCF assumptions be normalized across different Indian sectors?
2. What are the main sector-specific valuation risks in Indian equities?
3. How can WACC and company-specific risk premiums be documented transparently in a public-source research project?
4. How can peer comparison be used as a valuation sanity check without replacing intrinsic valuation?
5. What data limitations remain when using public sources instead of audited institutional databases?
6. How can Python and Excel automation improve reproducibility in equity research documentation?

### 2.5 Hypotheses

**H1:** A structured DCF-based framework with explicit assumption logs produces more transparent valuation outputs than simple ratio or return-based analysis.

**H2:** Sector-specific normalization materially changes the interpretation of company valuation quality.

**H3:** Public-source research can reach a useful portfolio and interview-grade standard when assumptions, sources, and limitations are documented clearly, but it cannot be considered fully institutional-grade without audited data reconciliation and market-data validation.

**H4:** A reproducible Python/Excel workflow improves the consistency and auditability of equity research outputs.

## 3. Literature and Conceptual Background

The paper is grounded in several established areas of finance: fundamental analysis, discounted cash flow valuation, cost of capital estimation, relative valuation, and financial statement analysis. Classic portfolio and valuation literature emphasizes that value is driven by expected cash flows, risk, and growth. Discounted cash flow valuation links future cash flows to present value by discounting them at an appropriate rate. Relative valuation compares companies using market multiples, but such comparisons are meaningful only when peers share similar business models, risk profiles, growth prospects, and accounting quality.

Markowitz's portfolio theory established the importance of risk and return trade-offs in security selection and portfolio construction. Sharpe's capital asset pricing model provided a framework for relating expected return to systematic risk. Later work on multifactor models expanded the understanding of risk drivers. In company valuation practice, DCF analysis remains central because it forces explicit assumptions regarding growth, margin, reinvestment, and risk. However, DCF outputs are highly sensitive to input assumptions, particularly terminal value, WACC, margin, and growth.

Financial statement analysis literature emphasizes that accounting earnings and cash flows are not identical. Earnings quality, working-capital behaviour, reinvestment requirements, depreciation, capital expenditure, and one-off items must all be understood before drawing conclusions. Piotroski's F-Score highlights the usefulness of combining profitability, leverage, liquidity, and operating efficiency indicators to evaluate financial strength, especially in value contexts.

This paper does not seek to replace existing valuation theory. Instead, it operationalizes established valuation ideas into a public-source workflow for Indian equities. The contribution is practical and methodological: it shows how a research process can combine DCF, WACC, peer comparison, source logs, assumption logs, sector-specific normalization, and Excel/Python automation in a transparent manner.

## 4. Data and Sample Selection

### 4.1 Sample

The study applies the framework to ten Indian listed companies:

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

### 4.2 Sector Coverage

The companies were selected to create diversity across business models rather than to represent a statistically random sample. The sample includes autos, pharmaceuticals, metals, refining, agrochemicals, industrial packaging, auto components, and capital goods. This design allows the framework to demonstrate how valuation assumptions change across sectors.

### 4.3 Data Sources

The project relies on public information such as annual reports, quarterly result disclosures, investor presentations, exchange filings, company communications, and public market references. The current version is classified as Public-Source Complete v1. This classification signals that the company research packs are complete in structure and public-source interpretation, but final numerical values require audited data reconciliation.

### 4.4 Data-Quality Classification

The paper uses the following classification:

**Public-Source Complete v1 - audited-data refresh pending.**

This classification means that the research pack contains a complete business overview, thesis, risk matrix, DCF assumption framework, WACC framework, peer framework, source log, assumptions log, numerical summary, and completion audit. It does not mean that the paper contains final institutional-grade valuations. Future refresh items include audited FY26 annual reports, verified share counts, net debt and cash reconciliation, date-consistent peer tables, regression beta calculations, and final valuation-range updates.

## 5. Methodology

### 5.1 Overview

The methodology combines intrinsic valuation, relative valuation, risk analysis, and reproducible documentation. The workflow begins with business understanding, then moves to industry context, growth drivers, financial performance, DCF assumptions, WACC, peer framework, scenarios, sensitivity analysis, risk matrix, source log, and completion audit.

### 5.2 FCFF DCF Framework

The paper uses free cash flow to the firm (FCFF) as the main intrinsic valuation framework for non-financial companies:

**FCFF = EBIT x (1 - Tax Rate) + Depreciation and Amortization - Capital Expenditure - Change in Net Working Capital**

FCFF is used because it values operating cash flows available to all capital providers before financing structure. This is useful when comparing companies with different leverage profiles.

### 5.3 WACC Framework

The discount rate is structured using a WACC framework:

**WACC = Cost of Equity x Equity Weight + After-tax Cost of Debt x Debt Weight**

The cost of equity is estimated conceptually as:

**Cost of Equity = Risk-free Rate + Beta x Equity Risk Premium + Company-Specific Risk Premium**

In the Public-Source Complete v1 stage, beta values are treated as placeholders or provisional assumptions. A beta regression pipeline has been built to support later WACC refinement.

### 5.4 Terminal Value

Terminal value is estimated using the Gordon growth approach:

**Terminal Value = Final Year FCFF x (1 + Terminal Growth) / (WACC - Terminal Growth)**

Terminal growth is kept conservative because terminal value often dominates DCF output. The paper avoids aggressive terminal growth assumptions, especially for cyclical businesses.

### 5.5 Scenario Analysis

Each company is evaluated through bear, base, and bull scenarios. These scenarios do not merely change growth rates mechanically; they are linked to company-specific drivers. For example, CPCL's scenarios are linked to GRM and inventory risk, while Triveni Turbine's scenarios are linked to order inflow, export demand, and margin sustainability.

### 5.6 Sensitivity Analysis

Each company includes a WACC versus terminal growth sensitivity framework. Additional company-specific sensitivities are suggested where relevant, such as commodity margin sensitivity for NALCO, zinc/silver price sensitivity for Hindustan Zinc, GRM sensitivity for CPCL, working-capital sensitivity for Sharda Cropchem, customer concentration risk for Fiem Industries, and order-book conversion for Triveni Turbine.

### 5.7 Peer Framework

Peer comparison is used as a valuation sanity check rather than a substitute for intrinsic valuation. Each company has a peer framework, but the paper avoids mechanically applying peer multiples without considering differences in product mix, cyclicality, leverage, margin structure, and business model.

### 5.8 Python and Excel Implementation

The project includes Python scripts and Excel workbooks. The automation layer includes a consolidated valuation dashboard, a ten-company DCF workbook pack, a beta regression pipeline, and a peer-table refresh template. This improves reproducibility and allows future refreshes to be performed systematically.

## 6. Company-Level Application

### 6.1 Hero MotoCorp

Hero MotoCorp is treated as a mature, high-quality two-wheeler company with recovery potential, premiumization, and electric vehicle optionality. The key modelling challenge is avoiding overpayment for a mature business by assuming that every optionality works. The DCF should reflect two-wheeler demand recovery, margin stability, competition, and EV transition risk.

### 6.2 Natco Pharma

Natco Pharma is treated as a complex generics and niche pharma company with lumpy earnings and pipeline optionality. The key modelling challenge is normalizing product-cycle earnings and separating recurring operating cash flows from one-off or temporary product opportunities. Pipeline optionality should be recognized but not overcapitalized in the base case.

### 6.3 NALCO

NALCO is treated as an integrated aluminium and alumina commodity business. The key modelling challenge is mid-cycle commodity normalization. Strong recent earnings may reflect favourable commodity conditions, but a DCF should not assume peak aluminium or alumina margins forever.

### 6.4 Hindustan Zinc

Hindustan Zinc is treated as a high-margin zinc, lead, and silver producer with dividend relevance and commodity-cycle exposure. The key modelling challenge is separating strong zinc and silver cycles from sustainable mid-cycle mining profitability. Ownership and capital allocation also matter.

### 6.5 CPCL

CPCL is treated as a refining-cycle company. The key modelling challenge is normalized GRM. Refiners can report very strong earnings during favourable refining-margin periods, but GRMs can reverse. Inventory gains and losses also create quarterly volatility.

### 6.6 Sharda Cropchem

Sharda Cropchem is treated as an asset-light, registration-led agrochemical company. The key modelling challenge is cash conversion. Revenue and margin recovery must be tested against working capital, receivables, inventory, channel destocking, regulatory approvals, and currency exposure.

### 6.7 Fiem Industries

Fiem Industries is treated as a two-wheeler-linked auto-component company with LED lighting and EV content optionality. The key modelling challenge is customer concentration and margin sustainability. Strong margin performance should be tested against raw material costs, OEM schedules, and two-wheeler production cycles.

### 6.8 Time Technoplast

Time Technoplast is treated as an industrial packaging and value-added polymer products company. The key modelling challenge is whether value-added product growth translates into durable free cash flow after capex, raw material price volatility, and working-capital requirements.

### 6.9 Force Motors

Force Motors is treated as an auto/OEM and engine/aggregate manufacturing company. The key modelling challenge is separating recurring operating performance from exceptional gains and auto-cycle peaks. Traveller, Urbania, specialized mobility, and engine manufacturing provide growth drivers, but capex and cyclicality remain important.

### 6.10 Triveni Turbine

Triveni Turbine is treated as a high-quality capital-goods company with export and order-book momentum. The key modelling challenge is order-book conversion and margin sustainability. High margins and strong order inflow should be normalized rather than extrapolated indefinitely.

## 7. Cross-Company Findings

The first finding is that valuation logic is sector-specific. A generic DCF template is useful, but the assumptions must be adapted to the business model. Commodity companies require mid-cycle margins, refiners require normalized GRMs, pharma companies require product-cycle analysis, auto suppliers require customer-concentration assessment, and capital-goods companies require order-book analysis.

The second finding is that recent strong performance can mislead valuation. Many companies in the sample had strong recent results, but valuation requires separating sustainable earnings power from cyclical or one-off performance. This is especially important for commodity, refining, and auto-cycle businesses.

The third finding is that source and assumption logs improve transparency. By recording assumptions and data-quality limitations, the analyst makes the valuation process more reviewable. This helps avoid hidden assumptions and supports future audited-data refresh.

The fourth finding is that peer comparison is useful only when interpreted carefully. Peer multiples can provide context, but they should not replace business-model analysis. A company may deserve a different valuation multiple because of margin quality, cyclicality, capital intensity, leverage, or growth visibility.

The fifth finding is that Python and Excel automation can make research more reproducible. The project structure allows dashboards, DCF workbooks, beta regression, and peer templates to be refreshed systematically rather than manually recreated.

## 8. Discussion

The framework developed in this paper is most useful for early-stage analysts who need a disciplined path from screening to valuation. It does not eliminate judgement. Instead, it organizes judgement. The analyst still needs to decide what revenue growth, margins, WACC, capex, and working-capital assumptions are reasonable. However, the framework forces these assumptions to be explicit.

The framework also helps prevent a common valuation error: confusing a good company with a good investment. A company can have strong operations but still be expensive if the market already discounts optimistic assumptions. Conversely, a company with temporary weakness may still be attractive if normalized cash flows are higher than current earnings suggest. This paper does not make final recommendations, but it demonstrates how such questions can be approached systematically.

The Public-Source Complete v1 classification is an important part of the framework. It allows the project to be presented honestly as a serious portfolio and research demonstration, while acknowledging that final institutional-grade valuation requires more data verification. This distinction is especially important for SSRN, recruiters, and readers because it avoids overclaiming.

## 9. Limitations

This study has several limitations. First, the sample includes ten companies selected for business-model diversity, not statistical representativeness. Second, the research uses public-source data and preliminary assumptions. Third, audited FY26 annual-report reconciliation has not yet been completed. Fourth, date-consistent peer numerical tables remain a future refresh item. Fifth, beta regression and WACC refinement require further execution and review. Sixth, final market price and valuation ranges should be updated using a consistent valuation date.

The paper does not provide investment advice, financial advice, or buy/sell recommendations. The valuation framework is intended for education, research practice, and portfolio demonstration.

## 10. Conclusion

This paper developed a public-source fundamental valuation framework for Indian listed equities and applied it to ten companies across multiple sectors. The study shows that a disciplined research workflow can improve transparency by combining DCF modelling, WACC frameworks, peer comparison, scenario analysis, sensitivity analysis, risk matrices, source logs, assumption logs, and Python/Excel automation.

The main contribution is methodological. The paper demonstrates that valuation must be adapted to business model and sector. Commodity companies require mid-cycle margin normalization, refiners require GRM normalization, pharma companies require product-cycle and pipeline analysis, auto suppliers require customer concentration analysis, and capital-goods companies require order-book conversion analysis.

The project is complete at the Public-Source Complete v1 level. Future work should focus on audited FY26 data refresh, share-count verification, net debt/cash reconciliation, beta regression review, date-consistent peer numerical tables, and final valuation-range recalculation.

## References

Damodaran, A. (2012). *Investment Valuation: Tools and Techniques for Determining the Value of Any Asset*. Wiley.

Fama, E. F., and French, K. R. (1993). Common risk factors in the returns on stocks and bonds. *Journal of Financial Economics*, 33(1), 3-56.

Koller, T., Goedhart, M., and Wessels, D. (2020). *Valuation: Measuring and Managing the Value of Companies*. Wiley.

Markowitz, H. (1952). Portfolio selection. *The Journal of Finance*, 7(1), 77-91.

Penman, S. H. (2013). *Financial Statement Analysis and Security Valuation*. McGraw-Hill Education.

Piotroski, J. D. (2000). Value investing: The use of historical financial statement information to separate winners from losers. *Journal of Accounting Research*, 38, 1-41.

Sharpe, W. F. (1964). Capital asset prices: A theory of market equilibrium under conditions of risk. *The Journal of Finance*, 19(3), 425-442.

SSRN Support Center. (2026). What is required to submit a paper to SSRN? Elsevier/SSRN Support.

SSRN Support Center. (2025). SSRN policy on generative AI and AI-assisted technologies. Elsevier/SSRN Support.

## Appendix A. Company Universe and Modelling Focus

| Company | Sector | Main Modelling Focus |
|---|---|---|
| Hero MotoCorp | Auto / Two-wheelers | Mature quality business, premiumization, EV optionality |
| Natco Pharma | Pharma | Product-cycle normalization, pipeline optionality |
| NALCO | Metals | Aluminium/alumina mid-cycle normalization |
| Hindustan Zinc | Metals | Zinc/silver cycle and dividend relevance |
| CPCL | Refining | GRM normalization and inventory risk |
| Sharda Cropchem | Agrochemicals | Registration-led model and working-capital risk |
| Fiem Industries | Auto components | Two-wheeler dependence and customer concentration |
| Time Technoplast | Industrial packaging | Value-added mix, raw materials, working capital |
| Force Motors | Auto/OEM | Exceptional-item normalization and auto-cycle risk |
| Triveni Turbine | Capital goods | Order-book conversion and margin sustainability |

## Appendix B. Data-Quality Classification

**Public-Source Complete v1** means that a company has a completed research note, assumptions log, source log, peer framework, numerical DCF summary, and completion audit based on public-source research. It does not mean audited institutional-grade valuation.

Future refresh requirements include audited FY26 annual reports, verified share counts, net debt and cash reconciliation, beta regression, date-consistent peer tables, current market price refresh, and independent review.

## Appendix C. Reproducibility Files

The project repository contains:

- consolidated research tracker
- consolidated valuation dashboard
- company DCF workbook pack
- company research notes
- assumptions logs
- source logs
- peer frameworks
- numerical refresh summaries
- beta regression pipeline
- peer-table refresh template
- final audit checklist
- career presentation pack

## Appendix D. Disclaimer

This working paper and the associated project are for educational and research purposes only. They do not constitute investment advice, financial advice, or buy/sell recommendations. All outputs depend on assumptions and should be independently verified before real investment use.
