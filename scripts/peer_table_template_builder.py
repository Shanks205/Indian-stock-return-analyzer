"""Build peer numerical table template for the Indian Equity Valuation Lab.

Purpose:
- create a structured peer-comparison workbook template
- keep peer data date-consistent
- avoid mixing stale data from different dates/sources

This script does not fabricate peer metrics. It creates a clean template that can
be filled from a chosen data source during the audited refresh phase.

Example:
    python scripts/peer_table_template_builder.py
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

OUTPUT_DIR = Path("outputs/valuation_summary")
OUTPUT_FILE = OUTPUT_DIR / "peer_table_refresh_template.xlsx"

PEER_ROWS = [
    ["Hero MotoCorp", "Hero MotoCorp", "Subject company", "HEROMOTOCO.NS"],
    ["Hero MotoCorp", "Bajaj Auto", "Direct two-wheeler peer", "BAJAJ-AUTO.NS"],
    ["Hero MotoCorp", "TVS Motor", "Two-wheeler / EV execution peer", "TVSMOTOR.NS"],
    ["Hero MotoCorp", "Eicher Motors", "Premium motorcycle benchmark", "EICHERMOT.NS"],
    ["Natco Pharma", "Natco Pharma", "Subject company", "NATCOPHARM.NS"],
    ["Natco Pharma", "Divi's Laboratories", "Quality pharma/export benchmark", "DIVISLAB.NS"],
    ["Natco Pharma", "Laurus Labs", "API/formulations volatility peer", "LAURUSLABS.NS"],
    ["Natco Pharma", "Granules India", "Generics/API peer", "GRANULES.NS"],
    ["NALCO", "NALCO", "Subject company", "NATIONALUM.NS"],
    ["NALCO", "Hindalco", "Aluminium peer", "HINDALCO.NS"],
    ["NALCO", "Vedanta", "Diversified metals peer", "VEDL.NS"],
    ["NALCO", "Hindustan Zinc", "Metals/mining cash-generation peer", "HINDZINC.NS"],
    ["Hindustan Zinc", "Hindustan Zinc", "Subject company", "HINDZINC.NS"],
    ["Hindustan Zinc", "Vedanta", "Parent / diversified metals peer", "VEDL.NS"],
    ["Hindustan Zinc", "NALCO", "Commodity PSU reference", "NATIONALUM.NS"],
    ["CPCL", "CPCL", "Subject company", "CHENNPETRO.NS"],
    ["CPCL", "Indian Oil", "Parent / integrated refining peer", "IOC.NS"],
    ["CPCL", "BPCL", "Refining and marketing PSU", "BPCL.NS"],
    ["CPCL", "HPCL", "Refining and marketing PSU", "HINDPETRO.NS"],
    ["CPCL", "MRPL", "Refining-focused peer", "MRPL.NS"],
    ["Sharda Cropchem", "Sharda Cropchem", "Subject company", "SHARDACROP.NS"],
    ["Sharda Cropchem", "UPL", "Global agrochemical reference", "UPL.NS"],
    ["Sharda Cropchem", "PI Industries", "Quality agrochemical / CSM benchmark", "PIIND.NS"],
    ["Sharda Cropchem", "Rallis India", "Indian agrochemical peer", "RALLIS.NS"],
    ["Fiem Industries", "Fiem Industries", "Subject company", "FIEMIND.NS"],
    ["Fiem Industries", "Lumax Industries", "Automotive lighting peer", "LUMAXIND.NS"],
    ["Fiem Industries", "Minda Corporation", "Auto-component / electrical peer", "MINDACORP.NS"],
    ["Fiem Industries", "Uno Minda", "Larger auto-component benchmark", "UNOMINDA.NS"],
    ["Time Technoplast", "Time Technoplast", "Subject company", "TIMETECHNO.NS"],
    ["Time Technoplast", "Mold-Tek Packaging", "Packaging/polymer peer", "MOLDTKPAC.NS"],
    ["Time Technoplast", "EPL", "Packaging peer", "EPL.NS"],
    ["Time Technoplast", "Supreme Industries", "Large plastic-products reference", "SUPREMEIND.NS"],
    ["Force Motors", "Force Motors", "Subject company", "FORCEMOT.NS"],
    ["Force Motors", "Ashok Leyland", "Commercial vehicle reference", "ASHOKLEY.NS"],
    ["Force Motors", "Tata Motors", "Broad auto reference", "TATAMOTORS.NS"],
    ["Force Motors", "Mahindra & Mahindra", "Utility vehicle and auto-cycle reference", "M&M.NS"],
    ["Triveni Turbine", "Triveni Turbine", "Subject company", "TRITURBINE.NS"],
    ["Triveni Turbine", "Thermax", "Energy / industrial equipment peer", "THERMAX.NS"],
    ["Triveni Turbine", "Siemens India", "Large capital-goods reference", "SIEMENS.NS"],
    ["Triveni Turbine", "ABB India", "Capital-goods / electrification reference", "ABB.NS"],
]

COLUMNS = [
    "Subject Company",
    "Peer Company",
    "Peer Type",
    "Ticker",
    "Data Date",
    "Source",
    "Market Cap",
    "Enterprise Value",
    "P/E",
    "EV/EBITDA",
    "Revenue Growth %",
    "EBITDA Margin %",
    "PAT Margin %",
    "ROE %",
    "ROCE %",
    "Net Debt / Equity",
    "Dividend Yield %",
    "Notes",
    "Status",
]


def build_peer_template() -> pd.DataFrame:
    rows = []
    for row in PEER_ROWS:
        rows.append({
            "Subject Company": row[0],
            "Peer Company": row[1],
            "Peer Type": row[2],
            "Ticker": row[3],
            "Data Date": "To update",
            "Source": "To update",
            "Market Cap": None,
            "Enterprise Value": None,
            "P/E": None,
            "EV/EBITDA": None,
            "Revenue Growth %": None,
            "EBITDA Margin %": None,
            "PAT Margin %": None,
            "ROE %": None,
            "ROCE %": None,
            "Net Debt / Equity": None,
            "Dividend Yield %": None,
            "Notes": "Use one consistent data date/source for final comparison",
            "Status": "Pending refresh",
        })
    return pd.DataFrame(rows, columns=COLUMNS)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df = build_peer_template()
    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Peer Refresh Template", index=False)
    print(f"Saved {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
