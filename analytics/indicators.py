import pandas as pd


def calculate_daily_returns(df):

    df = df.copy()

    df["daily_return"] = (
        df["close_price"].pct_change() * 100
    )

    return df

def calculate_sma(df, window):

    df = df.copy()

    df[f"sma_{window}"] = (
        df["close_price"]
        .rolling(window=window)
        .mean()
    )

    return df

def calculate_volatility(df, window=20):

    df = df.copy()

    if "daily_return" not in df.columns:
        df = calculate_daily_returns(df)

    df[f"volatility_{window}"] = (
        df["daily_return"]
        .rolling(window=window)
        .std()
    )

    return df

def calculate_rsi(df, window=14):

    df = df.copy()

    delta = df["close_price"].diff()

    gains = delta.where(delta > 0, 0)

    losses = -delta.where(delta < 0, 0)

    avg_gain = gains.rolling(window=window).mean()

    avg_loss = losses.rolling(window=window).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (100 / (1 + rs))

    df[f"rsi_{window}"] = rsi

    return df

def calculate_macd(df):

    df = df.copy()

    ema_12 = df["close_price"].ewm(
        span=12,
        adjust=False
    ).mean()

    ema_26 = df["close_price"].ewm(
        span=26,
        adjust=False
    ).mean()

    macd = ema_12 - ema_26

    signal = macd.ewm(
        span=9,
        adjust=False
    ).mean()

    histogram = macd - signal

    df["macd"] = macd

    df["signal"] = signal

    df["histogram"] = histogram

    return df