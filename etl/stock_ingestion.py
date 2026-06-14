import yfinance as yf
from pathlib import Path

stocks = [
    "AAPL",
    "MSFT",
    "RELIANCE.NS",
    "TCS.NS"
]

raw_data_path = Path("data/raw")
raw_data_path.mkdir(parents=True, exist_ok=True)

for stock in stocks:
    print(f"Fetching {stock}...")

    df = yf.download(
        stock,
        period="1y",
        interval="1d",
        auto_adjust=True
    )

    filename = stock.replace(".", "_") + ".csv"

    df.to_csv(raw_data_path / filename)

    print(f"Saved {filename}")

print("Stock ingestion completed.")