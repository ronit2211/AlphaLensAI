import pandas as pd
from pathlib import Path
from sqlalchemy import text

from database.mysql_connection import engine

raw_path = Path("data/raw")


with engine.connect() as conn:

    company_lookup = pd.read_sql(
        text(
            """
            SELECT company_id, ticker
            FROM companies
            """
        ),
        conn
    )

    ticker_to_id = dict(
        zip(
            company_lookup["ticker"],
            company_lookup["company_id"]
        )
    )

    for csv_file in raw_path.glob("*.csv"):

        ticker = csv_file.stem.replace("_", ".")

        if ticker not in ticker_to_id:
            print(f"Skipping {ticker}")
            continue

        company_id = ticker_to_id[ticker]

        df = pd.read_csv(csv_file)

        if "Date" not in df.columns:
            continue

        df = df.rename(
            columns={
                "Date": "trade_date",
                "Open": "open_price",
                "High": "high_price",
                "Low": "low_price",
                "Close": "close_price",
                "Volume": "volume"
            }
        )

        df["company_id"] = company_id

        df = df[
            [
                "company_id",
                "trade_date",
                "open_price",
                "high_price",
                "low_price",
                "close_price",
                "volume"
            ]
        ]

        df.to_sql(
            "stock_prices",
            con=engine,
            if_exists="append",
            index=False
        )

        print(f"Loaded {ticker}")

print("All stock prices loaded successfully.")