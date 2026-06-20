from database.data_access import get_price_history

from analytics.indicators import (
    calculate_daily_returns,
    calculate_sma
)
from analytics.indicators import (
    calculate_daily_returns,
    calculate_sma,
    calculate_volatility
)
from analytics.indicators import (
    calculate_daily_returns,
    calculate_sma,
    calculate_volatility,
    calculate_rsi
)

from analytics.indicators import (
    calculate_daily_returns,
    calculate_sma,
    calculate_volatility,
    calculate_rsi,
    calculate_macd
)

prices = get_price_history("AAPL")

prices = calculate_daily_returns(prices)

prices = calculate_sma(prices, 20)

prices = calculate_sma(prices, 50)

prices = calculate_daily_returns(prices)

prices = calculate_sma(prices, 20)

prices = calculate_sma(prices, 50)

prices = calculate_volatility(prices, 20)

prices = calculate_rsi(prices, 14)

prices = calculate_macd(prices)

print(
    prices[
        [
            "trade_date",
            "close_price",
            "macd",
            "signal",
            "histogram"
        ]
    ].tail()
)