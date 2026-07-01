import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import yfinance as yf
from sqlalchemy import text

from database.mysql_connection import engine


def update_metadata():

    with engine.connect() as conn:

        companies = conn.execute(
            text("""
                SELECT company_id, ticker
                FROM companies
            """)
        ).fetchall()

        for company_id, ticker in companies:

            try:

                print(f"Updating {ticker}...")

                info = yf.Ticker(ticker).info

                sector = info.get("sector")
                industry = info.get("industry")
                country = info.get("country")
                currency = info.get("currency")
                market_cap = info.get("marketCap")

                conn.execute(
                    text("""
                        UPDATE companies
                        SET
                            sector = :sector,
                            industry = :industry,
                            country = :country,
                            currency = :currency,
                            market_cap = :market_cap
                        WHERE company_id = :company_id
                    """),
                    {
                        "sector": sector,
                        "industry": industry,
                        "country": country,
                        "currency": currency,
                        "market_cap": market_cap,
                        "company_id": company_id
                    }
                )

                conn.commit()

                print(f"Updated {ticker}")

            except Exception as e:

                print(f"Failed {ticker}: {e}")


if __name__ == "__main__":
    update_metadata()