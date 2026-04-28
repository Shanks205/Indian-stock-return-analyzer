"""Batch DCF valuation runner.

This script reads a valuation-input CSV, runs a standardized FCFF DCF model,
and exports a valuation-summary CSV.

It is designed for the Indian Equity Valuation Lab workflow.

Example:
    python src/valuation_runner.py

Default input:
    data/templates/valuation_inputs_template.csv

Default output:
    outputs/valuation_summary/valuation_summary.csv
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, List, Optional

from dcf_model import DCFInputs, run_dcf


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_PATH = PROJECT_ROOT / "data" / "templates" / "valuation_inputs_template.csv"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "outputs" / "valuation_summary" / "valuation_summary.csv"


def _to_float(value: str) -> Optional[float]:
    """Convert a CSV string to float.

    Empty strings are returned as None so incomplete companies can be skipped.
    """
    if value is None:
        return None
    cleaned = str(value).strip()
    if cleaned == "":
        return None
    return float(cleaned)


def _growth_rates(row: Dict[str, str]) -> List[float]:
    """Read five annual growth rates from one input row."""
    growth_columns = [
        "revenue_growth_y1",
        "revenue_growth_y2",
        "revenue_growth_y3",
        "revenue_growth_y4",
        "revenue_growth_y5",
    ]
    rates: List[float] = []
    for column in growth_columns:
        value = _to_float(row.get(column, ""))
        if value is None:
            raise ValueError(f"Missing growth assumption: {column}")
        rates.append(value)
    return rates


def row_is_ready(row: Dict[str, str]) -> bool:
    """Check whether a company row has enough data for the DCF engine."""
    required_columns = [
        "company_name",
        "current_price",
        "shares_outstanding_cr",
        "net_debt_cr",
        "current_fcff_cr",
        "wacc_base",
        "terminal_growth_base",
        "margin_of_safety_required",
        "revenue_growth_y1",
        "revenue_growth_y2",
        "revenue_growth_y3",
        "revenue_growth_y4",
        "revenue_growth_y5",
    ]
    return all(str(row.get(column, "")).strip() != "" for column in required_columns)


def value_company(row: Dict[str, str]) -> Dict[str, str]:
    """Run DCF for one company row and return output dictionary."""
    company_name = row["company_name"]
    current_price = _to_float(row["current_price"])
    mos_required = _to_float(row["margin_of_safety_required"])

    inputs = DCFInputs(
        company_name=company_name,
        current_fcff=_to_float(row["current_fcff_cr"]),
        growth_rates=_growth_rates(row),
        wacc=_to_float(row["wacc_base"]),
        terminal_growth=_to_float(row["terminal_growth_base"]),
        net_debt=_to_float(row["net_debt_cr"]),
        shares_outstanding=_to_float(row["shares_outstanding_cr"]),
    )

    valuation = run_dcf(inputs)
    intrinsic_value = valuation["intrinsic_value_per_share"]
    upside_downside = (intrinsic_value / current_price) - 1 if current_price else None
    buy_zone_price = intrinsic_value * (1 - mos_required) if mos_required is not None else None

    if upside_downside is None:
        final_view = "Needs market price"
    elif current_price <= buy_zone_price:
        final_view = "Potential MOS candidate"
    elif upside_downside > 0:
        final_view = "Watchlist / no full MOS"
    else:
        final_view = "Overvalued under base case"

    return {
        "ticker": row.get("ticker", ""),
        "company_name": company_name,
        "bucket": row.get("bucket", ""),
        "current_price": f"{current_price:.2f}",
        "intrinsic_value_base": f"{intrinsic_value:.2f}",
        "base_upside_downside": f"{upside_downside:.2%}" if upside_downside is not None else "",
        "mos_required": f"{mos_required:.0%}" if mos_required is not None else "",
        "buy_zone_price": f"{buy_zone_price:.2f}" if buy_zone_price is not None else "",
        "enterprise_value_cr": f"{valuation['enterprise_value']:.2f}",
        "equity_value_cr": f"{valuation['equity_value']:.2f}",
        "pv_forecast_fcff_cr": f"{valuation['pv_forecast_fcff']:.2f}",
        "pv_terminal_value_cr": f"{valuation['pv_terminal_value']:.2f}",
        "final_view": final_view,
        "analyst_notes": row.get("analyst_notes", ""),
    }


def run_batch_valuation(input_path: Path = DEFAULT_INPUT_PATH, output_path: Path = DEFAULT_OUTPUT_PATH) -> None:
    """Read inputs, value ready companies, and export results."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    ready_results: List[Dict[str, str]] = []
    skipped_companies: List[str] = []

    with input_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row_is_ready(row):
                ready_results.append(value_company(row))
            else:
                skipped_companies.append(row.get("company_name", "Unknown"))

    fieldnames = [
        "ticker",
        "company_name",
        "bucket",
        "current_price",
        "intrinsic_value_base",
        "base_upside_downside",
        "mos_required",
        "buy_zone_price",
        "enterprise_value_cr",
        "equity_value_cr",
        "pv_forecast_fcff_cr",
        "pv_terminal_value_cr",
        "final_view",
        "analyst_notes",
    ]

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(ready_results)

    print(f"Valuation complete. Results saved to: {output_path}")
    if skipped_companies:
        print("Skipped companies with incomplete inputs:")
        for company in skipped_companies:
            print(f"- {company}")


if __name__ == "__main__":
    run_batch_valuation()
