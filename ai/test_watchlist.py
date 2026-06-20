from ai.watchlist import generate_watchlist

report = generate_watchlist()

print(report)

from screeners.screener import screen_all_stocks
from screeners.ranking import rank_stocks

results = screen_all_stocks()

ranked = rank_stocks(results)

print(type(ranked))
print(ranked)