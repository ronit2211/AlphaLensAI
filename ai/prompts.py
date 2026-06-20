def build_stock_analysis_prompt(metrics):

    prompt = f"""
You are a professional financial analyst.

Analyze the following stock.

Ticker:
{metrics['ticker']}

Current Price:
{metrics['close_price']:.2f}

RSI:
{metrics['rsi']:.2f}

MACD:
{metrics['macd']:.2f}

Signal:
{metrics['signal']:.2f}

SMA20:
{metrics['sma_20']:.2f}

SMA50:
{metrics['sma_50']:.2f}

Recommendation:
{metrics['recommendation']}

Please provide:

1. Trend Analysis

2. Momentum Analysis

3. Risk Assessment

4. Investment Outlook

Keep the explanation concise and professional.
"""

    return prompt