"""Excel export functions for the Indian Stock Return Analyzer."""

from pathlib import Path

import pandas as pd

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def export_metrics_to_excel(metrics: dict[str, float], ticker: str) -> None:
    """Export performance metrics to an Excel file.

    In finance roles, Excel output is useful because analysts often review,
    format, and share results in spreadsheets.
    """
    metrics_table = pd.DataFrame(
        {
            "Metric": list(metrics.keys()),
            "Value": list(metrics.values()),
        }
    )

    output_path = OUTPUT_DIR / f"{ticker}_performance_summary.xlsx"

    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        metrics_table.to_excel(writer, sheet_name="Performance Summary", index=False)

    print(f"Excel summary exported to: {output_path}")
