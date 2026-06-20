from sqlalchemy import text

from database.mysql_connection import engine

create_companies_table = """
CREATE TABLE IF NOT EXISTS companies (
    company_id INT AUTO_INCREMENT PRIMARY KEY,

    ticker VARCHAR(20) UNIQUE NOT NULL,

    company_name VARCHAR(255),

    sector VARCHAR(255),

    industry VARCHAR(255),

    country VARCHAR(100),

    currency VARCHAR(20),

    market_cap BIGINT
);
"""

create_stock_prices_table = """
CREATE TABLE IF NOT EXISTS stock_prices (
    price_id INT AUTO_INCREMENT PRIMARY KEY,

    company_id INT NOT NULL,

    trade_date DATE NOT NULL,

    open_price FLOAT,

    high_price FLOAT,

    low_price FLOAT,

    close_price FLOAT,

    volume BIGINT,

    FOREIGN KEY (company_id)
    REFERENCES companies(company_id)
);
"""

with engine.connect() as conn:

    conn.execute(text(create_companies_table))

    conn.execute(text(create_stock_prices_table))

    conn.commit()

print("Tables created successfully.")