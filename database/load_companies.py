import pandas as pd
from pathlib import Path

from sqlalchemy import text

from database.mysql_connection import engine

metadata_folder = Path("data/metadata")

csv_files = metadata_folder.glob("*_metadata.csv")

with engine.connect() as conn:

    for file in csv_files:

        df = pd.read_csv(file)

        for _, row in df.iterrows():

            query = text("""
                INSERT INTO companies
                (
                    ticker,
                    company_name,
                    sector,
                    industry,
                    country,
                    currency,
                    market_cap
                )
                VALUES
                (
                    :ticker,
                    :company_name,
                    :sector,
                    :industry,
                    :country,
                    :currency,
                    :market_cap
                )
            """)

            conn.execute(
                query,
                {
                    "ticker": row["Ticker"],
                    "company_name": row["Company_Name"],
                    "sector": row["Sector"],
                    "industry": row["Industry"],
                    "country": row["Country"],
                    "currency": row["Currency"],
                    "market_cap": int(row["Market_Cap"])
                }
            )

    conn.commit()

print("Companies loaded successfully.")