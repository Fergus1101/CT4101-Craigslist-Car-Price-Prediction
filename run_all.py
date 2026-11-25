"""Run the three project notebooks in order.

Usage (from the project folder, with the virtual environment active):
    python run_all.py

Requires the Kaggle file at data/raw/vehicles.csv (see README, Step 2).
Each notebook is executed top to bottom and its saved outputs are refreshed.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOTEBOOK_DIR = ROOT / "notebooks"
RAW_DATA = ROOT / "data" / "raw" / "vehicles.csv"

NOTEBOOKS = [
    "01_data_sampling.ipynb",
    "02_data_audit.ipynb",
    "03_model_comparison_and_evaluation.ipynb",
]

if not RAW_DATA.exists():
    print("Cannot find data/raw/vehicles.csv.")
    print("Download the dataset from Kaggle first (README, Step 2), then run this again.")
    sys.exit(1)

for name in NOTEBOOKS:
    print(f"\nRunning {name} ... (this can take several minutes)")
    result = subprocess.run(
        [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "notebook", "--execute", "--inplace",
            "--ExecutePreprocessor.timeout=-1",  # no per-cell time limit (model tuning is slow)
            name,
        ],
        cwd=NOTEBOOK_DIR,  # notebooks use paths relative to the notebooks/ folder
    )
    if result.returncode != 0:
        print(f"\n{name} failed. Scroll up for the error message.")
        sys.exit(result.returncode)

print("\nAll three notebooks ran successfully.")