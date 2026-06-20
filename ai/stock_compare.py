from screeners.screener import analyze_stock
from screeners.screener import evaluate_stock

from ai.gemini_client import get_gemini_response


def compare_stocks(ticker1, ticker2):

    stock1 = analyze_stock(ticker1)
    stock1["recommendation"] = evaluate_stock(stock1)

    stock2 = analyze_stock(ticker2)
    stock2["recommendation"] = evaluate_stock(stock2)

    prompt = f"""
You are a professional equity research analyst.

Compare the following two stocks.

Stock 1

Ticker: {stock1["ticker"]}

Price: {stock1["close_price"]:.2f}

RSI: {stock1["rsi"]:.2f}

MACD: {stock1["macd"]:.2f}

Signal: {stock1["signal"]:.2f}

Recommendation: {stock1["recommendation"]}


Stock 2

Ticker: {stock2["ticker"]}

Price: {stock2["close_price"]:.2f}

RSI: {stock2["rsi"]:.2f}

MACD: {stock2["macd"]:.2f}

Signal: {stock2["signal"]:.2f}

Recommendation: {stock2["recommendation"]}


Provide:

1. Trend Comparison
2. Momentum Comparison
3. Risk Comparison
4. Which stock currently appears stronger and why

Keep the response concise and professional.
"""

    return get_gemini_response(prompt)