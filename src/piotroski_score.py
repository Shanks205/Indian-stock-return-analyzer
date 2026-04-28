"""Piotroski F-Score calculation utilities.

This module is part of the Indian Equity Valuation Lab extension.
It is intentionally written in a beginner-friendly way so the logic can be
explained in interviews and later expanded for a research paper.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class PiotroskiInputs:
    """Financial inputs required for one company-year comparison.

    Values should be supplied for the current year and previous year.
    The module does not fetch data automatically; it only scores clean inputs.
    """

    net_income_current: float
    operating_cash_flow_current: float
    total_assets_current: float
    total_assets_previous: float
    long_term_debt_current: float
    long_term_debt_previous: float
    current_ratio_current: float
    current_ratio_previous: float
    shares_outstanding_current: float
    shares_outstanding_previous: float
    gross_margin_current: float
    gross_margin_previous: float
    asset_turnover_current: float
    asset_turnover_previous: float


def calculate_piotroski_score(inputs: PiotroskiInputs) -> Dict[str, int]:
    """Calculate the 9-point Piotroski F-Score.

    Returns a dictionary with every signal and total score.
    """

    roa_current = inputs.net_income_current / inputs.total_assets_current
    roa_previous = inputs.net_income_current / inputs.total_assets_previous

    signals = {
        "positive_net_income": int(inputs.net_income_current > 0),
        "positive_operating_cash_flow": int(inputs.operating_cash_flow_current > 0),
        "improving_roa": int(roa_current > roa_previous),
        "cash_flow_quality": int(inputs.operating_cash_flow_current > inputs.net_income_current),
        "lower_leverage": int(inputs.long_term_debt_current <= inputs.long_term_debt_previous),
        "improving_liquidity": int(inputs.current_ratio_current > inputs.current_ratio_previous),
        "no_equity_dilution": int(inputs.shares_outstanding_current <= inputs.shares_outstanding_previous),
        "improving_gross_margin": int(inputs.gross_margin_current > inputs.gross_margin_previous),
        "improving_asset_turnover": int(inputs.asset_turnover_current > inputs.asset_turnover_previous),
    }
    signals["total_score"] = sum(signals.values())
    return signals


if __name__ == "__main__":
    example = PiotroskiInputs(
        net_income_current=100,
        operating_cash_flow_current=120,
        total_assets_current=1000,
        total_assets_previous=950,
        long_term_debt_current=100,
        long_term_debt_previous=120,
        current_ratio_current=1.8,
        current_ratio_previous=1.5,
        shares_outstanding_current=10,
        shares_outstanding_previous=10,
        gross_margin_current=0.42,
        gross_margin_previous=0.40,
        asset_turnover_current=1.1,
        asset_turnover_previous=1.0,
    )
    print(calculate_piotroski_score(example))
