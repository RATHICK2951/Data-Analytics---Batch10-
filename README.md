# Customer Churn & Lifetime Value (LTV) Analytics — Batch 10

Analytics project combining exploratory data analysis, two trained machine-learning
models, a FastAPI prediction service, and a Power BI dashboard, built on the
Telco Customer Churn dataset (~7,044 customers).

## What this project does

- Predicts which customers are likely to **churn** (`models/churn_model.joblib`,
  a logistic regression model).
- Predicts each customer's **lifetime value (LTV)** and segments customers into
  LTV bands (`ltv_random_forest.joblib`, a random forest regressor, trained by
  `model.py`).
- Serves churn predictions through a FastAPI service (`api/main.py`).
- Feeds a Power BI dashboard (`reports/powerbi/Customer_Churn_Analysis_Dashboard.pbix`)
  from pre-aggregated CSVs in `dashboard/data/` and `reports/`.

## Project structure

```
.
├── api/                  FastAPI churn-prediction service (api/main.py)
├── dashboard/data/       Pre-aggregated CSVs feeding the Power BI dashboard
├── data/                 Raw, cleaned, and model-ready datasets
├── models/               Trained churn classifier (churn_model.joblib)
├── Notebook/              Main data cleaning & feature-engineering notebook
├── reports/               Business-facing outputs: KPIs, charts, model metrics
├── src/ingestion/         Loads Excel data into a PostgreSQL database
├── textsrc/notebooks/     EDA notebook
├── model.py                Trains and saves the LTV random forest model
├── historical_revenue.py   Computes historical revenue per customer
├── ltv_random_forest.joblib          Trained LTV model + preprocessor
├── Telco_Customer_Churn_with_LTV_Added-1.xlsx   Source data for model.py
├── Dockerfile             Container build for the API
└── requirements.txt        Python dependencies
```

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

**Important — scikit-learn version:** `requirements.txt` pins
`scikit-learn==1.6.1` so that `models/churn_model.joblib` loads correctly.
`ltv_random_forest.joblib` was trained under scikit-learn `1.9.0` and does
**not** reliably predict under `1.6.1`. If you need to retrain or run
`model.py` for LTV predictions, do so in a **separate virtual environment**
pinned to `scikit-learn==1.9.0`. The two models cannot currently share one
environment — see the project audit report for details.

## Running things

**Train / regenerate the LTV model:**
```bash
python model.py
```

**Compute historical revenue per customer:**
```bash
python historical_revenue.py
```

**Run the churn prediction API:**
```bash
uvicorn api.main:app --reload
```
Then open `http://127.0.0.1:8000/docs` for interactive API docs.
`POST /predict` expects all 27 customer features used in training (see
`/docs` for the full schema) — not just tenure/charges.

**Run with Docker:**
```bash
docker build -t churn-api .
docker run -p 8000:8000 churn-api
```

**Dashboard:** open `reports/powerbi/Customer_Churn_Analysis_Dashboard.pbix`
in Power BI Desktop and refresh data sources against `dashboard/data/` and
`reports/`.

## Notebooks

- `Notebook/Data cleaning and preprocessing.ipynb` — main cleaning and
  feature-engineering notebook.
- `textsrc/notebooks/Telco_customer_churn_clean.ipynb` — exploratory data
  analysis (EDA).

  > Several other EDA notebooks in the project root
  > (`Telco_customer_churn.ipynb`, `Telco_customer_churn_EDA.ipynb`,
  > `EDA_Telco_customer_churn.ipynb`, `Copy_of_Telco_customer_churn_EDA.ipynb`)
  > are near-duplicates of the one above. Recommend consolidating to a single
  > canonical EDA notebook.

## Known issues / in progress

A full audit report covering every file, dependency, and cross-component
connection is available separately. Open items at time of writing:
- The two trained models require different scikit-learn versions and cannot
  yet run in one shared environment (see Setup above).
- `data/telco_customer_churn_processed_for_modelling_with_target_leakage.csv`
  contains target-leakage columns; confirm it is not used for model training.
