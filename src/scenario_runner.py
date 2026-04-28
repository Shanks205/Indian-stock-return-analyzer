"""Batch scenario DCF runner.

Reads bear/base/bull assumptions from a CSV file and exports a scenario valuation
summary for every company with complete inputs.

Default input:
    data/templates/scenario_inputs_template.csv

Default output:
    outputs/valuation_summary/scenario_valuation_summary.csv
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, List, Optional

from scenario_analysis import ScenarioAssumption, classify_valuation, run_three_case_analysis


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_PATH = PROJECT_ROOT / "data" / "templates" / "scenario_inputs_template.csv"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "outputs" / "valuation_summary" / "scenario_valuation_summary.csv"


def _to_float(value: str) -> Optional[float]:
    if value is None:
        return None
    cleaned = str(value).strip()
    if cleaned == "":
        return None
    return float(cleaned)


def _scenario_growth_rates(row: Dict[str, str], prefix: str) -> List[float]:
    columns = [
        f"{prefix}_growth_y1",
        f"{prefix}_growth_y2",
        f"{prefix}_growth_y3",
        f"{prefix}_growth_y4",
        f"{prefix}_growth_y5",
    ]
    rates: List[float] = []
    for column in columns:
        value = _to_float(row.get(column, ""))
        if value is None:
            raise ValueError(f"Missing {prefix} growth assumption: {column}")
        rates.append(value)
    return rates


def row_is_ready(row: Dict[str, str]) -> bool:
    required = [
        "company_name",
        "current_price",
        "shares_outstanding_cr",
        "net_debt_cr",
        "mos_required",
    ]
    for prefix in ["bear", "base", "bull"]:
        required.extend(
            [
                f"{prefix}_current_fcff_cr",
                f"{prefix}_growth_y1",
                f"{prefix}_growth_y2",
                f"{prefix}_growth_y3",
                f"{prefix}_growth_y4",
                f"{prefix}_growth_y5",
                f"{prefix}_wacc",
                f"{prefix}_terminal_growth",
            ]
        )
    return all(str(row.get(column, "")).strip() != "" for column in required)


def build_scenario(row: Dict[str, str], prefix: str, scenario_name: str) -> ScenarioAssumption:
    return ScenarioAssumption(
        scenario_name=scenario_name,
        current_fcff=_to_float(row[f"{prefix}_current_fcff_cr"]),
        growth_rates=_scenario_growth_rates(row, prefix),
        wacc=_to_float(row[f"{prefix}_wacc"]),
        terminal_growth=_to_float(row[f"{prefix}_terminal_growth"]),
        net_debt=_to_float(row["net_debt_cr"]),
        shares_outstanding=_to_float(row["shares_outstanding_cr"]),
    )


def value_company_scenarios(row: Dict[str, str]) -> List[Dict[str, str]]:
    company_name = row["company_name"]
    current_price = _to_float(row["current_price"])
    mos_required = _to_float(row["mos_required"])

    scenario_results = run_three_case_analysis(
        company_name=company_name,
        bear=build_scenario(row, "bear", "Bear"),
        base=build_scenario(row, "base", "Base"),
        bull=build_scenario(row, "bull", "Bull"),
    )

    output_rows: List[Dict[str, str]] = []
    for result in scenario_results:
        intrinsic_value = float(result["intrinsic_value_per_share"])
        upside_downside = (intrinsic_value / current_price) - 1 if current_price else None
        buy_zone_price = intrinsic_value * (1 - mos_required) if mos_required is not None else None
        final_view = classify_valuation(current_price, intrinsic_value, mos_required)

        output_rows.append(
            {
                "ticker": row.get("ticker", ""),
                "company_name": company_name,
                "bucket": row.get("bucket", ""),
                "scenario": str(result["scenario"]),
                "current_price": f"{current_price:.2f}",
                "intrinsic_value_per_share": f"{intrinsic_value:.2f}",
                "upside_downside": f"{upside_downside:.2%}" if upside_downside is not None else "",
                "mos_required": f"{mos_required:.0%}" if mos_required is not None else "",
                "buy_zone_price": f"{buy_zone_price:.2f}" if buy_zone_price is not None else "",
                "wacc": f"{float(result['wacc']):.2%}",
                "terminal_growth": f"{float(result['terminal_growth']):.2%}",
                "enterprise_value_cr": f"{float(result['enterprise_value']):.2f}",
                "equity_value_cr": f"{float(result['equity_value']):.2f}",
                "pv_forecast_fcff_cr": f"{float(result['pv_forecast_fcff']):.2f}",
                "pv_terminal_value_cr": f"{float(result['pv_terminal_value']):.2f}",
                "final_view": final_view,
                "source_notes": row.get("source_notes", ""),
                "analyst_notes": row.get("analyst_notes", ""),
            }
        )
    return output_rows


def run_batch_scenario_valuation(
    input_path: Path = DEFAULT_INPUT_PATH,
    output_path: Path = DEFAULT_OUTPUT_PATH,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    all_results: List[Dict[str, str]] = []
    skipped: List[str] = []

    with input_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row_is_ready(row):
                all_results.extend(value_company_scenarios(row))
            else:
                skipped.append(row.get("company_name", "Unknown"))

    fieldnames = [
        "ticker",
        "company_name",
        "bucket",
        "scenario",
        "current_price",
        "intrinsic_value_per_share",
        "upside_downside",
        "mos_required",
        "buy_zone_price",
        "wacc",
        "terminal_growth",
        "enterprise_value_cr",
        "equity_value_cr",
        "pv_forecast_fcff_cr",
        "pv_terminal_value_cr",
        "final_view",
        "source_notes",
        "analyst_notes",
    ]

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_results)

    print(f"Scenario valuation complete. Results saved to: {output_path}")
    if skipped:
        print("Skipped companies with incomplete scenario inputs:")
        for company in skipped:
            print(f"- {company}")


if __name__ == "__main__":
    run_batch_scenario_valuation()
