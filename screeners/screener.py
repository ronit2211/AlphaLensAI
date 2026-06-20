from database.data_access import get_price_history
from screeners.ranking import (
    calculate_score,
    get_risk
)
from analytics.indicators import (
    calculate_daily_returns,
    calculate_sma,
    calculate_rsi,
    calculate_macd
)


def analyze_stock(ticker):

    prices = get_price_history(ticker)

    prices = calculate_daily_returns(prices)

    prices = calculate_sma(prices, 20)

    prices = calculate_sma(prices, 50)

    prices = calculate_rsi(prices)

    prices = calculate_macd(prices)

    latest = prices.iloc[-1]
    

    return {
        "ticker": ticker,
        "close_price": latest["close_price"],
        "sma_20": latest["sma_20"],
        "sma_50": latest["sma_50"],
        "rsi": latest["rsi_14"],
        "macd": latest["macd"],
        "signal": latest["signal"],
        
    }

#decision engine
def evaluate_stock(metrics):

    buy_candidate = (
        metrics["close_price"] > metrics["sma_50"]
        and metrics["rsi"] < 40
        and metrics["macd"] > metrics["signal"]
    )

    if buy_candidate:
        return "BUY"

    return "WATCH"

from config.config import STOCKS

#module 6.2 for ranking and screening multiple stocks
def screen_all_stocks():

    results = []

    for ticker in STOCKS:

        try:

            metrics = analyze_stock(ticker)

            metrics["recommendation"] = evaluate_stock(metrics)

            metrics["score"] = calculate_score(metrics)

            metrics["risk"] = get_risk(
                metrics["score"]
            )

            results.append(metrics)

        except Exception as e:

            print(f"Error processing {ticker}: {e}")

    return results