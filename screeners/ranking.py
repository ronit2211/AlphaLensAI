import pandas as pd

def calculate_score(metrics):
    score = 50 
    
    # RSI 
    if metrics["rsi"] < 30: 
        score += 20 
    elif metrics["rsi"] < 40: 
        score += 10 
    elif metrics["rsi"] > 70: 
        score -= 20 

    # MACD 
    if metrics["macd"] > metrics["signal"]: 
        score += 15 
    else: 
        score -= 10 

    # Trend 
    if metrics["close_price"] > metrics["sma_20"]: 
        score += 10 

    if metrics["sma_20"] > metrics["sma_50"]: 
        score += 10 

    # Recommendation 
    recommendation = metrics.get(
        "recommendation",
        "WATCH"
    )

    if recommendation == "BUY":
        score += 15
    elif recommendation == "SELL":
        score -= 15

    return max(0, min(score, 100))

def get_risk(score):

    if score >= 80:
        return "Low Risk"

    elif score >= 60:
        return "Medium Risk"

    return "High Risk"


def rank_stocks(results):

    ranked = []

    for stock in results:

        stock["score"] = calculate_score(stock)

        stock["risk"] = get_risk(
            stock["score"]
        )

        ranked.append(stock)

    df = pd.DataFrame(ranked)

    return df.sort_values(
        by="score",
        ascending=False
    )