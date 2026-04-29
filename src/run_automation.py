"""One-command automation runner for the Indian Equity Valuation Lab.

Runs the automated workflow for the screener company universe:

1. Batch return analysis for all screener companies except RELIANCE.NS.
2. Batch scenario DCF valuation for companies with complete scenario inputs.

Outputs are written to outputs/valuation_summary/.
"""

from __future__ import annotations

from batch_return_analyzer import run_batch_return_analysis
from scenario_runner import run_batch_scenario_valuation


def main() -> None:
    """Run the automated project workflow."""
    print("Running Indian Equity Valuation Lab automation...")
    print("Step 1: Batch return analysis for screener companies, excluding RELIANCE.NS")
    run_batch_return_analysis()

    print("\nStep 2: Scenario DCF valuation for companies with complete inputs")
    run_batch_scenario_valuation()

    print("\nAutomation complete. Check outputs/valuation_summary/ for result files.")


if __name__ == "__main__":
    main()
