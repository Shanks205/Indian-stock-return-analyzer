"""Simple FCFF DCF model utilities for Indian equity valuation.

This module provides a standardized model skeleton. It is not a replacement
for full analyst judgment; assumptions must be supported by annual reports,
quarterly results, concall transcripts, industry research, and macro data.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class DCFInputs:
    company_name: str
    current_fcff: float
    growth_rates: List[float]
    wacc: float
    terminal_growth: float
    net_debt: float
    shares_outstanding: float


def forecast_fcff(current_fcff: float, growth_rates: List[float]) -> List[float]:
    """Forecast FCFF using annual growth-rate assumptions."""
    values = []
    fcff = current_fcff
    for growth in growth_rates:
        fcff *= 1 + growth
        values.append(fcff)
    return values


def discount_cash_flows(cash_flows: List[float], discount_rate: float) -> List[float]:
    """Discount annual cash flows to present value."""
    return [cash_flow / ((1 + discount_rate) ** year) for year, cash_flow in enumerate(cash_flows, start=1)]


def terminal_value(final_fcff: float, wacc: float, terminal_growth: float) -> float:
    """Calculate terminal value using Gordon growth model."""
    if wacc <= terminal_growth:
        raise ValueError("WACC must be greater than terminal growth.")
    return final_fcff * (1 + terminal_growth) / (wacc - terminal_growth)


def run_dcf(inputs: DCFInputs) -> Dict[str, float]:
    """Run a simple FCFF DCF valuation."""
    fcff_forecast = forecast_fcff(inputs.current_fcff, inputs.growth_rates)
    pv_fcff = discount_cash_flows(fcff_forecast, inputs.wacc)

    tv = terminal_value(fcff_forecast[-1], inputs.wacc, inputs.terminal_growth)
    pv_terminal_value = tv / ((1 + inputs.wacc) ** len(fcff_forecast))

    enterprise_value = sum(pv_fcff) + pv_terminal_value
    equity_value = enterprise_value - inputs.net_debt
    intrinsic_value_per_share = equity_value / inputs.shares_outstanding

    return {
        "company_name": inputs.company_name,
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
        "intrinsic_value_per_share": intrinsic_value_per_share,
        "pv_terminal_value": pv_terminal_value,
        "pv_forecast_fcff": sum(pv_fcff),
    }


if __name__ == "__main__":
    example = DCFInputs(
        company_name="Example Company",
        current_fcff=1000,
        growth_rates=[0.10, 0.09, 0.08, 0.07, 0.06],
        wacc=0.12,
        terminal_growth=0.045,
        net_debt=0,
        shares_outstanding=20,
    )
    print(run_dcf(example))
