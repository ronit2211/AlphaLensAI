#first version without any AI, just a simple rule-based system for now
'''def generate_stock_report(metrics):

    report = f"""
Stock: {metrics['ticker']}

Current Price: {metrics['close_price']:.2f}

RSI: {metrics['rsi']:.2f}

MACD: {metrics['macd']:.2f}

Signal: {metrics['signal']:.2f}

Recommendation: {metrics['recommendation']}
"""

    return report'''
#Module 8.2 — Intelligent Stock Explanation
'''def generate_stock_report(metrics):

    reasons = []

    if metrics["rsi"] < 40:
        reasons.append(
            "RSI is below 40 indicating weakness."
        )

    elif metrics["rsi"] > 70:
        reasons.append(
            "RSI is above 70 indicating overbought conditions."
        )

    if metrics["macd"] > metrics["signal"]:
        reasons.append(
            "MACD is above signal line indicating bullish momentum."
        )
    else:
        reasons.append(
            "MACD is below signal line indicating bearish momentum."
        )

    report = f"""
Stock: {metrics['ticker']}

Current Price: {metrics['close_price']:.2f}

RSI: {metrics['rsi']:.2f}

MACD: {metrics['macd']:.2f}

Signal: {metrics['signal']:.2f}

Recommendation: {metrics['recommendation']}

Reasoning:
"""

    for reason in reasons:
        report += f"\n• {reason}"

    return report'''

#Module 8.3 — AI Analyst V2
def generate_stock_report(metrics):

    reasons = []

    if metrics["rsi"] < 40:
        reasons.append(
            "RSI is below 40, suggesting the stock is approaching oversold territory."
        )

    elif metrics["rsi"] > 70:
        reasons.append(
            "RSI is above 70, indicating potentially overbought conditions."
        )

    if metrics["macd"] > metrics["signal"]:
        reasons.append(
            "MACD is above its signal line, indicating positive momentum."
        )
    else:
        reasons.append(
            "MACD remains below its signal line, indicating weak short-term momentum."
        )

    if metrics["close_price"] > metrics["sma_50"]:
        reasons.append(
            "Price remains above the 50-day moving average, suggesting the long-term trend is still positive."
        )
    else:
        reasons.append(
            "Price is trading below the 50-day moving average, indicating a weak long-term trend."
        )

    report = f"""
===========================
AlphaLensAI Stock Report
===========================

Ticker: {metrics['ticker']}

Current Price: {metrics['close_price']:.2f}

Recommendation: {metrics['recommendation']}

Analysis:
"""

    for reason in reasons:
        report += f"\n• {reason}"

    report += """

Conclusion:
"""

    if metrics["recommendation"] == "BUY":

        report += """
The stock currently satisfies the screening criteria and may deserve further investigation.
"""

    else:

        report += """
The stock does not currently satisfy all screening conditions. Monitoring for trend improvement is advised.
"""

    return report