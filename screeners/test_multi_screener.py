import pandas as pd

from screeners.screener import screen_all_stocks

results = screen_all_stocks()

df = pd.DataFrame(results)

print(
    df[
        [
            "ticker",
            "close_price",
            "rsi",
            "macd",
            "signal",
            "recommendation"
        ]
    ]
)