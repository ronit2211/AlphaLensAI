from screeners.screener import screen_all_stocks
from screeners.ranking import rank_stocks

from ai.gemini_client import get_gemini_response


def generate_watchlist():

    results = screen_all_stocks()

    ranked = rank_stocks(results)

    #error debugged top_stocks = ranked[:5]
    top_stocks = ranked[:5].head(5).to_dict("records")

    stock_summary = ""

    for stock in top_stocks:

        stock_summary += f"""
Ticker: {stock['ticker']}
RSI: {stock['rsi']:.2f}
MACD: {stock['macd']:.2f}
Recommendation: {stock['recommendation']}
Score: {stock['score']}
"""

    prompt = f"""
You are a professional equity research analyst.

Analyze the following top ranked stocks.

{stock_summary}

Create:

1. Today's Watchlist
2. Brief reason for each stock
3. Best opportunity among them
4. Key risks to monitor

Keep the report concise and professional.
"""

    return get_gemini_response(prompt)



def get_watchlist_table():

    results = screen_all_stocks()

    ranked = rank_stocks(results)

    return ranked[
        [
            "ticker",
            "score",
            "rsi",
            "macd",
            "recommendation"
        ]
    ].head(5)