import yfinance as yf
import pandas as pd
from pathlib import Path

from config.config import (
    STOCKS,
    DATA_PERIOD,
    DATA_INTERVAL
)

from etl.utils import setup_logger


logger = setup_logger()


raw_data_path = Path("data/raw")
raw_data_path.mkdir(parents=True, exist_ok=True)

metadata_path = Path("data/metadata")
metadata_path.mkdir(parents=True, exist_ok=True)


def fetch_stock_data(ticker):

    try:

        logger.info(f"Fetching data for {ticker}")

        df = yf.download(
            ticker,
            period=DATA_PERIOD,
            interval=DATA_INTERVAL,
            auto_adjust=True
        )

        if df.empty:
            logger.warning(f"No data found for {ticker}")
            return

        # Flatten columns
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df.reset_index(inplace=True)

        df["Ticker"] = ticker

        filename = ticker.replace(".", "_") + ".csv"

        df.to_csv(
            raw_data_path / filename,
            index=False
        )

        logger.info(f"Saved {filename}")

        fetch_metadata(ticker)

    except Exception as e:
        logger.error(
            f"Failed for {ticker}: {str(e)}"
        )


def fetch_metadata(ticker):

    try:

        stock = yf.Ticker(ticker)

        info = stock.info

        metadata = {
            "Ticker": ticker,
            "Company_Name": info.get("longName"),
            "Sector": info.get("sector"),
            "Industry": info.get("industry"),
            "Country": info.get("country"),
            "Currency": info.get("currency"),
            "Market_Cap": info.get("marketCap")
        }

        metadata_df = pd.DataFrame([metadata])

        filename = (
            ticker.replace(".", "_")
            + "_metadata.csv"
        )

        metadata_df.to_csv(
            metadata_path / filename,
            index=False
        )

        logger.info(
            f"Metadata saved for {ticker}"
        )

    except Exception as e:

        logger.error(
            f"Metadata failed for {ticker}: {str(e)}"
        )


def main():

    logger.info(
        "Stock ingestion started"
    )

    for ticker in STOCKS:

        fetch_stock_data(ticker)

    logger.info(
        "Stock ingestion completed"
    )


if __name__ == "__main__":
    main()