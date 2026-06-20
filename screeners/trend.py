def detect_trend(metrics):

    if metrics["close_price"] > metrics["sma_20"] > metrics["sma_50"]:
        return "Strong Uptrend"

    elif metrics["close_price"] < metrics["sma_20"] < metrics["sma_50"]:
        return "Strong Downtrend"

    return "Sideways"