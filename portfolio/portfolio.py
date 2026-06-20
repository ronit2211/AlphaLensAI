import pandas as pd


def calculate_portfolio_return(returns_df, weights):

    portfolio_return = 0

    for ticker, weight in weights.items():

        latest_return = returns_df[ticker].iloc[-1]

        portfolio_return += latest_return * weight

    return portfolio_return

#helper to load returns
from database.data_access import get_price_history
from analytics.indicators import calculate_daily_returns

def build_returns_dataframe(tickers):

    frames = []

    for ticker in tickers:

        prices = get_price_history(ticker)

        prices = calculate_daily_returns(prices)

        temp = prices[["trade_date", "daily_return"]].copy()

        temp.rename(
            columns={"daily_return": ticker},
            inplace=True
        )

        frames.append(temp)

    df = frames[0]

    for frame in frames[1:]:
        df = pd.merge(
            df,
            frame,
            on="trade_date",
            how="inner"
        )

    return df


#module 7.2 
import numpy as np

def calculate_portfolio_volatility(
    returns_df,
    weights
):

    returns_only = returns_df.drop(
        columns=["trade_date"]
    )

    cov_matrix = returns_only.cov()

    weight_vector = np.array(
        list(weights.values())
    )

    portfolio_variance = (
        weight_vector.T
        @ cov_matrix
        @ weight_vector
    )

    portfolio_volatility = np.sqrt(
        portfolio_variance
    )

    return portfolio_volatility

#sharpe ratio calculation risk free rate assumed to be 0 for simplicity
def calculate_sharpe_ratio(
    portfolio_return,
    portfolio_volatility,
    risk_free_rate=0
):

    sharpe_ratio = (
        portfolio_return
        - risk_free_rate
    ) / portfolio_volatility

    return sharpe_ratio