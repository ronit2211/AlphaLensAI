import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
import yfinance as yf
import pandas as pd
from sqlalchemy import text

from database.mysql_connection import engine
from config.config import STOCKS


def update_market_data():

    with engine.connect() as conn:

        company_lookup = pd.read_sql(
            text("""
                SELECT company_id, ticker
                FROM companies
            """),
            conn
        )

    ticker_to_id = dict(
        zip(
            company_lookup["ticker"],
            company_lookup["company_id"]
        )
    )

    for ticker in STOCKS:

        try:

            print(f"Downloading {ticker}...")

            df = yf.download(
                ticker,
                period="1y",
                interval="1d",
                progress=False
            )
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)

            if df.empty:
                print(f"No data found for {ticker}")
                continue

            df.reset_index(inplace=True)

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

            company_id = ticker_to_id.get(ticker)

            if company_id is None:
                print(f"{ticker} not found in companies table")
                continue

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

            # Remove old data first
            with engine.connect() as conn:

                conn.execute(
                    text("""
                        DELETE FROM stock_prices
                        WHERE company_id = :company_id
                    """),
                    {"company_id": company_id}
                )

                conn.commit()

            # Insert fresh data
            df.to_sql(
                "stock_prices",
                con=engine,
                if_exists="append",
                index=False
            )

            print(f"Updated {ticker}")

        except Exception as e:

            print(f"Error updating {ticker}: {e}")

    print("Market data refresh complete.")


if __name__ == "__main__":
    update_market_data()