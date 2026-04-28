"""Scenario analysis utilities for DCF valuation.

This module extends the base DCF engine by supporting bear, base, and bull cases.
It is designed for the Indian Equity Valuation Lab workflow.

The goal is to avoid giving one false-precision intrinsic value. Instead, every
company should be analysed as a range of possible outcomes.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from dcf_model import DCFInputs, run_dcf


@dataclass
class ScenarioAssumption:
    """Assumptions for one valuation scenario."""

    scenario_name: str
    current_fcff: float
    growth_rates: List[float]
    wacc: float
    terminal_growth: float
    net_debt: float
    shares_outstanding: float


def run_scenario(company_name: str, scenario: ScenarioAssumption) -> Dict[str, float | str]:
    """Run a DCF valuation for one scenario."""

    result = run_dcf(
        DCFInputs(
            company_name=company_name,
            current_fcff=scenario.current_fcff,
            growth_rates=scenario.growth_rates,
            wacc=scenario.wacc,
            terminal_growth=scenario.terminal_growth,
            net_debt=scenario.net_debt,
            shares_outstanding=scenario.shares_outstanding,
        )
    )

    return {
        "company_name": company_name,
        "scenario": scenario.scenario_name,
        "intrinsic_value_per_share": result["intrinsic_value_per_share"],
        "enterprise_value": result["enterprise_value"],
        "equity_value": result["equity_value"],
        "pv_forecast_fcff": result["pv_forecast_fcff"],
        "pv_terminal_value": result["pv_terminal_value"],
        "wacc": scenario.wacc,
        "terminal_growth": scenario.terminal_growth,
    }


def run_three_case_analysis(
    company_name: str,
    bear: ScenarioAssumption,
    base: ScenarioAssumption,
    bull: ScenarioAssumption,
) -> List[Dict[str, float | str]]:
    """Run bear, base, and bull case DCF valuations."""

    return [
        run_scenario(company_name, bear),
        run_scenario(company_name, base),
        run_scenario(company_name, bull),
    ]


def classify_valuation(current_price: float, intrinsic_value: float, margin_of_safety: float) -> str:
    """Classify valuation based on intrinsic value and required margin of safety."""

    buy_zone = intrinsic_value * (1 - margin_of_safety)

    if current_price <= buy_zone:
        return "Potential margin-of-safety candidate"
    if current_price < intrinsic_value:
        return "Undervalued but below required MOS"
    if current_price <= intrinsic_value * 1.10:
        return "Fairly valued"
    return "Overvalued under this scenario"


if __name__ == "__main__":
    # Example case only. Replace with real company data before analysis.
    company = "Example Company"
    scenarios = run_three_case_analysis(
        company_name=company,
        bear=ScenarioAssumption(
            scenario_name="Bear",
            current_fcff=1000,
            growth_rates=[0.04, 0.04, 0.035, 0.03, 0.03],
            wacc=0.14,
            terminal_growth=0.035,
            net_debt=0,
            shares_outstanding=20,
        ),
        base=ScenarioAssumption(
            scenario_name="Base",
            current_fcff=1000,
            growth_rates=[0.08, 0.08, 0.07, 0.06, 0.05],
            wacc=0.12,
            terminal_growth=0.045,
            net_debt=0,
            shares_outstanding=20,
        ),
        bull=ScenarioAssumption(
            scenario_name="Bull",
            current_fcff=1000,
            growth_rates=[0.12, 0.11, 0.10, 0.09, 0.08],
            wacc=0.105,
            terminal_growth=0.05,
            net_debt=0,
            shares_outstanding=20,
        ),
    )

    for scenario_result in scenarios:
        print(scenario_result)
