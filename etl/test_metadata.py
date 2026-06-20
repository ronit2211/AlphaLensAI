# etl/test_metadata.py

import yfinance as yf

stock = yf.Ticker("AAPL")

info = stock.info

print("Company:", info.get("longName"))
print("Sector:", info.get("sector"))
print("Market Cap:", info.get("marketCap"))