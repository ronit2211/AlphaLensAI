from portfolio.portfolio import (
    build_returns_dataframe,
    calculate_portfolio_return,
    calculate_portfolio_volatility,
    calculate_sharpe_ratio
)

tickers = [
    "AAPL",
    "MSFT",
    "RELIANCE.NS",
    "TCS.NS"
]

weights = {
    "AAPL": 0.25,
    "MSFT": 0.25,
    "RELIANCE.NS": 0.25,
    "TCS.NS": 0.25
}
#debug check
'''from database.data_access import get_price_history

print("\nStock Data Summary:")

for ticker in tickers:

    prices = get_price_history(ticker)

    print(
        ticker,
        len(prices),
        prices["trade_date"].min(),
        prices["trade_date"].max()
    )'''

returns_df = build_returns_dataframe(tickers)

'''print("\nDataFrame Shape:")
print(returns_df.shape)

print("\nLast 5 Rows:")
print(returns_df.tail())'''
portfolio_return = calculate_portfolio_return(
    returns_df,
    weights
)
portfolio_volatility = (
    calculate_portfolio_volatility(
        returns_df,
        weights
    )
)
sharpe_ratio = calculate_sharpe_ratio(
    portfolio_return,
    portfolio_volatility
)

print("\nPortfolio Return:")
print(portfolio_return)

print("\nPortfolio Volatility:")
print(portfolio_volatility)

print("\nSharpe Ratio:")
print(sharpe_ratio)