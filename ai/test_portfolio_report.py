from portfolio.portfolio import (
    build_returns_dataframe,
    calculate_portfolio_return,
    calculate_portfolio_volatility,
    calculate_sharpe_ratio
)

from ai.portfolio_report import (
    generate_portfolio_report
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


returns_df = build_returns_dataframe(
    tickers
)

portfolio_return = calculate_portfolio_return(
    returns_df,
    weights
)

portfolio_volatility = calculate_portfolio_volatility(
    returns_df,
    weights
)

sharpe_ratio = calculate_sharpe_ratio(
    portfolio_return,
    portfolio_volatility
)

report = generate_portfolio_report(
    portfolio_return,
    portfolio_volatility,
    sharpe_ratio
)

print(report)