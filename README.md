# CT4101 Craigslist Car Price Prediction

This project predicts the resale price of used vehicles listed on Craigslist. It
uses supervised machine-learning regression models and investigates the effects
of features such as vehicle age, mileage, manufacturer, condition, fuel type,
and transmission.

## Dataset

The project uses the **Craigslist Cars and Trucks** dataset from Kaggle:

<https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data>

The dataset was published by Austin Reese and is available under the CC0 Public
Domain dedication. The downloaded file is `vehicles.csv`. The full dataset has
approximately 426,880 rows and 26 columns. Milestone 2 works with a reproducible
sample of 30,000 rows selected with `random_state=42`.

## Requirements

- Python **3.13** (the workflow has been tested with Python 3.13.15)
- pip
- JupyterLab

The commands below use PowerShell on Windows. Run them from the repository root
(`CT4101-Craigslist-Car-Price-Prediction`):

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell prevents activation because of its execution policy, either allow
scripts for the current user or invoke the environment's Python directly:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\.venv\Scripts\Activate.ps1
```

## Download the data

Download the dataset from the Kaggle link above and extract it so that the raw
file has exactly this path:

```text
data/raw/vehicles.csv
```

For users with the Kaggle CLI already configured, the equivalent commands are:

```powershell
python -m pip install kaggle
kaggle datasets download -d austinreese/craigslist-carstrucks-data -p data/raw
Expand-Archive .\data\raw\craigslist-carstrucks-data.zip -DestinationPath .\data\raw
```

If extraction creates a nested copy of `vehicles.csv`, move it into
`data/raw/vehicles.csv` and remove the archive before running the notebooks.
The raw and generated CSV files are intentionally excluded from Git because of
their size.

## Milestone 2 workflow

Start JupyterLab from the repository root:

```powershell
.\.venv\Scripts\Activate.ps1
jupyter lab
```

Open and run the notebooks in this exact order. Run every cell in each notebook
from top to bottom before opening the next one:

1. [`notebooks/01_data_sampling.ipynb`](notebooks/01_data_sampling.ipynb)
2. [`notebooks/02_data_audit.ipynb`](notebooks/02_data_audit.ipynb)
3. [`notebooks/03_preprocessing_and_baseline.ipynb`](notebooks/03_preprocessing_and_baseline.ipynb)

The first notebook loads `data/raw/vehicles.csv`, draws 30,000 rows with
`random_state=42`, and writes the sample. The audit notebook checks its shape,
duplicates, missing values, and price quality. The final notebook filters
invalid prices, preprocesses numerical and categorical features, fits the
baseline model, and reports evaluation results and diagnostic plots.

### Running notebooks from the command line

The same workflow can be executed without opening the JupyterLab interface:

```powershell
.\.venv\Scripts\Activate.ps1
jupyter nbconvert --to notebook --execute --inplace .\notebooks\01_data_sampling.ipynb
jupyter nbconvert --to notebook --execute --inplace .\notebooks\02_data_audit.ipynb
jupyter nbconvert --to notebook --execute --inplace .\notebooks\03_preprocessing_and_baseline.ipynb
```

Run these commands from the repository root. The notebooks use paths relative
to `notebooks/`, so changing to another working directory can cause file-not
found errors.

## Expected outputs

After the complete workflow, the following data files should exist:

```text
data/raw/vehicles.csv                         # downloaded source dataset
data/processed/craigslist_30k_sample.csv     # generated 30,000-row sample
```

The sample should contain **30,000 rows and 26 columns**. The audit and baseline
results, tables, and plots are displayed and retained as notebook cell outputs;
the current notebooks do not export separate model, image, or report files.
