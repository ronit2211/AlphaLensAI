import pandas as pd
from sqlalchemy import text

from database.mysql_connection import engine


def get_all_companies():

    query = """
    SELECT *
    FROM companies
    """

    return pd.read_sql(
        text(query),
        engine
    )


def get_company_by_ticker(ticker):

    query = """
    SELECT *
    FROM companies
    WHERE ticker = :ticker
    """

    return pd.read_sql(
        text(query),
        engine,
        params={"ticker": ticker}
    )

def get_price_history(ticker):

    query = """
    SELECT
        sp.trade_date,
        sp.open_price,
        sp.high_price,
        sp.low_price,
        sp.close_price,
        sp.volume
    FROM stock_prices sp
    JOIN companies c
        ON sp.company_id = c.company_id
    WHERE c.ticker = :ticker
    ORDER BY sp.trade_date
    """

    return pd.read_sql(
        text(query),
        engine,
        params={"ticker": ticker}
    )
