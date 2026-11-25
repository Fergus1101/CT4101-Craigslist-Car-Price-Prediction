# Predicting Used Vehicle Prices on Craigslist
 
**CT4101 Machine Learning Portfolio Project** · Fergus O'Donoghue · Student ID 23412416
 
## 1. What this project does (in plain English)
 
Can we predict what a used car is listed for on Craigslist, using details such as its age, mileage, brand and fuel type? I compare three models on a 30,000-listing sample of a public Kaggle dataset:
 
| Model | What it is |
|---|---|
| Dummy | Always predicts the median price. This is the baseline to beat. |
| Ridge regression | A simple linear model. |
| Random Forest | A non-linear model made of many decision trees. |
 
**Headline result:** the Random Forest was best. On listings it had never seen, it was off by about **$4,327** on average (MAE) and explained about **74%** of the variation in price (R² = 0.74). Vehicle age and mileage mattered most. It is least reliable for very cheap cars (under $5,000) and very expensive cars (over $40,000).
 
## 2. Option A: just read the results (nothing to install or run)
 
All results are already saved inside the notebooks, and GitHub displays them directly in your browser. Click a notebook below and scroll down.
 
| Notebook | What you will see |
|---|---|
| [`notebooks/01_data_sampling.ipynb`](notebooks/01_data_sampling.ipynb) | Takes a reproducible 30,000-row sample from the 426,880-row dataset. |
| [`notebooks/02_data_audit.ipynb`](notebooks/02_data_audit.ipynb) | Data checks: size, missing values, duplicates, odd prices. |
| [`notebooks/03_model_comparison_and_evaluation.ipynb`](notebooks/03_model_comparison_and_evaluation.ipynb) | **The main notebook.** Preprocessing, the three models, cross-validation, results table, error analysis and feature importance. |
 
If you only have time for one thing, open notebook 03 and read the section headings and the results table.
 
## 3. Option B: re-run everything from scratch
 
The data files are **not** stored on GitHub because they are large, so you need to download the dataset first. Allow about 20-30 minutes, most of which is waiting for the models to train.
 
### What you need before starting
 
- **Python 3.13** (tested with 3.13.15). Download it from <https://www.python.org/downloads/>. On Windows, tick "Add Python to PATH" during installation.
- A free **Kaggle account** (needed to download the dataset).
- About 1.5 GB of free disk space.
### Step 1: Get the code
 
Click the green **Code** button on the GitHub page, then **Download ZIP**, and unzip it. (If you use Git, `git clone` works too.) Open a terminal **inside the unzipped folder**:
 
- **Windows:** open the folder in File Explorer, click the address bar, type `powershell`, and press Enter.
- **Mac:** right-click the folder and choose "New Terminal at Folder".
### Step 2: Download the dataset
 
1. Go to <https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data> and click **Download**. You will get a file called `craigslist-carstrucks-data.zip`.
2. Unzip it. Inside is a file called **`vehicles.csv`**.
3. Create the folders and move the file into place. In your terminal:
   **Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Force data\raw
```
   **Mac / Linux:**
```bash
mkdir -p data/raw
```
4. Move `vehicles.csv` into the `data/raw` folder. The final path must be exactly:
```text
data/raw/vehicles.csv
```
 
### Step 3: Set up Python (one-off)
 
**Windows (PowerShell):**
```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
**Mac / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
You will know it worked when `(.venv)` appears at the start of your terminal line.
 
> If Windows says scripts are disabled, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, answer Y, and repeat the `Activate.ps1` line.
 
### Step 4: Run it. Choose ONE of the two methods
 
**Method 1: one command (easiest).** From the project folder, with `(.venv)` showing:
 
```bash
python run_all.py
```
 
This runs all three notebooks in the correct order and stops with a clear message if something is missing. It takes roughly 10-20 minutes. The saved outputs inside the notebooks are refreshed with the new results.
 
**Method 2: manually in JupyterLab.**
 
```bash
cd notebooks
jupyter lab
```
 
A browser tab opens. Open the notebooks **in numerical order (01, then 02, then 03)**. In each one, choose **Run → Run All Cells** from the menu and wait until it finishes before opening the next. (Notebook 01 creates `data/processed/craigslist_30k_sample.csv`, which notebooks 02 and 03 need.)
 
### Step 5: Check you got the same results
 
Random seeds are fixed (`random_state=42`), so you should see these numbers at the end of notebook 03 (tiny differences are possible if library versions differ):
 
| Model | Test MAE | Test RMSE | Test R² |
|---|---|---|---|
| Dummy | $11,174 | $14,786 | -0.05 |
| Ridge | $7,656 | $10,854 | 0.43 |
| Random Forest | $4,327 | $7,328 | 0.74 |
 
Other checks: the sample has **30,000 rows and 26 columns**, and **26,974 rows** remain after removing prices below $500 or above $100,000.
 
### If something goes wrong
 
| Message or problem | Fix |
|---|---|
| `FileNotFoundError ... vehicles.csv` | The dataset is not at `data/raw/vehicles.csv`. Re-check Step 2 (folder names and spelling). |
| `FileNotFoundError ... craigslist_30k_sample.csv` | Notebook 01 has not been run yet. Run it first (or use `python run_all.py`). |
| `py` / `python` is not recognised | Python is not installed, or "Add to PATH" was not ticked. Reinstall Python. |
| Scripts are disabled (Windows) | See the note under Step 3. |
| `ModuleNotFoundError` | The environment is not active or packages are missing. Repeat Step 3. |
| Training seems slow | Normal. The Random Forest tuning cell (30 model fits) takes several minutes. |
 
## 4. Project structure
 
```text
CT4101-Craigslist-Car-Price-Prediction/
├── notebooks/
│   ├── 01_data_sampling.ipynb
│   ├── 02_data_audit.ipynb
│   └── 03_model_comparison_and_evaluation.ipynb
├── run_all.py            # optional: runs the three notebooks in order
├── requirements.txt      # Python packages and exact versions
├── .gitignore
├── README.md
└── data/                 # NOT on GitHub (see Step 2)
    ├── raw/vehicles.csv
    └── processed/craigslist_30k_sample.csv
```
 
## 5. Dataset
 
**Craigslist Cars and Trucks Data**, Austin Reese, Kaggle: <https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data>. Licence: CC0 (public domain). About 426,880 listings and 26 columns; a reproducible 30,000-row sample is used here. Prices are self-reported **asking** prices from 2021, not final sale prices.
 
## 6. Intended use, limitations and recommendation (short model card)
 
- **Intended use:** a rough guide to a fair asking price for cars listed between $500 and $100,000, not an automated valuation.
- **Evaluation:** 80/20 train/test split, 5-fold cross-validation on the training data only, test set used once at the end. Preprocessing lives inside the model pipelines, so no information leaks from the test set.
- **Main limitation:** errors are largest at the price extremes (median error about 64% for cars under $5,000; MAE about $11,300 above $40,000). Placeholder prices and rare cars are hard to predict from the available features.
- **Other risks:** 2021 data means today's prices will differ (concept drift); missing information such as accident history; regional price differences captured by the `state` feature.
- **Recommendation:** pilot with a human in the loop, such as a price suggestion a seller can override. Do not deploy as an automated valuation. Before wider use, retrain on recent listings and monitor input data and prediction errors.
## 7. Assistance declaration

 
In accordance with module policy, I declare the use of two AI tools. I used Gemini for syntax checking and debugging. I used Claude to review my notebook and writeup and this README. The data preparation, model choices, main modelling workflow, checking of all figures against the notebook output, and final interpretations are my own, and I can explain all submitted code.
 
