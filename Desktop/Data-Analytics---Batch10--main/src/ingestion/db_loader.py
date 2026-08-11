import os
import pandas as pd
from sqlalchemy import create_engine

def run_production_ingestion(file_relative_path: str):
    DB_USER = "postgres"
    DB_PASS = "postgres123"  # Make sure this matches your local PG installer password
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "zaalima_analytics"
    
    db_uri = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(db_uri)
    
    print("⏳ Reading team Excel file from localized path...")
    if not os.path.exists(file_relative_path):
        raise FileNotFoundError(f"❌ Excel file not found at {file_relative_path}!")
        
    df = pd.read_excel(file_relative_path, engine="openpyxl")
    df.columns = [col.lower().strip() for col in df.columns]
    
    print("🧼 Standardizing type mismatches and handling missing values...")
    if 'totalcharges' in df.columns:
        df['totalcharges'] = pd.to_numeric(df['totalcharges'], errors='coerce')
        df['totalcharges'] = df['totalcharges'].fillna(0.0)
    
    print(f"🚀 Streaming {len(df)} records directly to PostgreSQL server...")
    df.to_sql(name="raw_customer_churn", con=engine, if_exists="replace", index=False)
    print("✅ Ingestion successfully completed! PostgreSQL database is online.")

if __name__ == "__main__":
    # Make sure your teammate's Excel file is in your local data/ folder and named correctly here
    TARGET_FILE = os.path.join("data", "Telco_customer_churn.xlsx") 
    run_production_ingestion(TARGET_FILE)
