import os
import pandas as pd
from sqlalchemy import create_engine, text

def run_production_ingestion(file_relative_path: str):
    DB_USER = "postgres"
    
    # 1. FIXED: Strict environment check without a plain-text fallback
    DB_PASS = os.getenv("DB_PASSWORD")
    if not DB_PASS:
        raise ValueError("❌ Critical Security Error: 'DB_PASSWORD' environment variable is not configured!")
        
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
    
    # 2. FIXED: Cross-reference existing IDs to prevent duplicates on rerun
    print("🛡️ Checking database for existing customer keys to prevent duplicates...")
    try:
        with engine.connect() as conn:
            existing_ids = pd.read_sql_query(text("SELECT customerid FROM raw_customer_churn"), conn)
            df = df[~df['customerid'].isin(existing_ids['customerid'])]
    except Exception:
        print("ℹ️ Target table not found. Performing fresh initialization...")

    if df.empty:
        print("✅ No new records to ingest. Database is already up to date!")
        return

    print(f"🚀 Streaming {len(df)} new records directly to PostgreSQL server...")
    df.to_sql(name="raw_customer_churn", con=engine, if_exists="append", index=False)
    print("✅ Ingestion successfully completed! PostgreSQL database is online.")
