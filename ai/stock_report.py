from ai.gemini_client import get_gemini_response

def generate_stock_report(metrics):

    prompt = f"""
You are a professional financial analyst.

Analyze the following stock.

Ticker: {metrics["ticker"]}

Current Price: {metrics["close_price"]:.2f}

RSI: {metrics["rsi"]:.2f}

MACD: {metrics["macd"]:.2f}

Signal: {metrics["signal"]:.2f}

Recommendation: {metrics["recommendation"]}

Provide:

1. Trend Analysis
2. Momentum Analysis
3. Risk Assessment
4. Investment Outlook

Keep it concise and professional.
"""

    return get_gemini_response(prompt)