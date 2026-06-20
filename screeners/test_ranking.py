from screeners.screener import screen_all_stocks
from screeners.ranking import rank_stocks

results = screen_all_stocks()

ranked = rank_stocks(results)

print(
    ranked[
        [
            "ticker",
            "score",
            "rsi",
            "macd",
            "signal"
        ]
    ]
)