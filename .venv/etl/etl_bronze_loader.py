import os
import pandas as pd
import pyodbc
from kaggle.api.kaggle_api_extended import KaggleApi
from datetime import datetime

# Set Kaggle credentials path 
os.environ['KAGGLE_CONFIG_DIR'] = r"C:\Users\sakhe\.kaggle"  

def download_dataset():
    api = KaggleApi()
    api.authenticate()
    print("📥 Downloading dataset from Kaggle...")
    api.dataset_download_files('yasserh/housing-prices-dataset', path='data/incoming', unzip=True)
    print("✅ Download complete.")

def load_csv_to_df():
    print("📄 Loading CSV into DataFrame...")
    df = pd.read_csv('data/incoming/Housing.csv')
    df.columns = [col.strip().lower().replace(" ", "_").replace("-", "") for col in df.columns]

    # Convert 'yes'/'no' and 'true'/'false' to 1/0
    bool_cols = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']
    for col in bool_cols:
        df[col] = df[col].astype(str).str.lower().map({'yes': 1, 'no': 0, 'true': 1, 'false': 0})

    return df

def insert_into_sql(df):
    print("🧩 Inserting data into SQL Server...")
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        r"SERVER=SAKHEKILE\SQLEXPRESS;"
        "DATABASE=USHousingETL;"
        "Trusted_Connection=yes;"
        "Encrypt=no;"
    )

    cursor = conn.cursor()

    insert_sql = """
        INSERT INTO bronze_housing_prices_raw (
            price, area, bedrooms, bathrooms, stories, 
            mainroad, guestroom, basement, hotwaterheating, airconditioning, 
            parking, prefarea, furnishingstatus
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    for _, row in df.iterrows():
        cursor.execute(insert_sql,
            row['price'], row['area'], row['bedrooms'], row['bathrooms'], row['stories'],
            row['mainroad'], row['guestroom'], row['basement'], row['hotwaterheating'],
            row['airconditioning'], row['parking'], row['prefarea'], row['furnishingstatus']
        )

    conn.commit()
    conn.close()
    print(f"✅ {len(df)} records loaded into Bronze table.")

if __name__ == "__main__":
    print(f"🚀 Starting Bronze ETL: {datetime.now()}")
    download_dataset()
    df = load_csv_to_df()
    insert_into_sql(df)
    print(f"🏁 Finished ETL: {datetime.now()}")
