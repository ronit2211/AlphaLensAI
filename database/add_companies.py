import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from sqlalchemy import text
from database.mysql_connection import engine

companies = [

    # Banking
    ("HDFCBANK.NS", "HDFC Bank"),
    ("ICICIBANK.NS", "ICICI Bank"),
    ("SBIN.NS", "State Bank of India"),
    ("AXISBANK.NS", "Axis Bank"),
    ("KOTAKBANK.NS", "Kotak Mahindra Bank"),
    ("INDUSINDBK.NS", "IndusInd Bank"),

    # IT
    ("TCS.NS", "Tata Consultancy Services"),
    ("INFY.NS", "Infosys"),
    ("HCLTECH.NS", "HCL Technologies"),
    ("WIPRO.NS", "Wipro"),
    ("TECHM.NS", "Tech Mahindra"),


    # FMCG
    ("ITC.NS", "ITC"),
    ("HINDUNILVR.NS", "Hindustan Unilever"),
    ("NESTLEIND.NS", "Nestle India"),
    ("BRITANNIA.NS", "Britannia Industries"),
    ("DABUR.NS", "Dabur India"),

    # Energy
    ("RELIANCE.NS", "Reliance Industries"),
    ("ONGC.NS", "Oil and Natural Gas Corporation"),
    ("BPCL.NS", "Bharat Petroleum"),
    ("IOC.NS", "Indian Oil Corporation"),
    ("GAIL.NS", "GAIL India"),

    # Auto
    ("MARUTI.NS", "Maruti Suzuki"),
    ("M&M.NS", "Mahindra & Mahindra"),
    ("BAJAJ-AUTO.NS", "Bajaj Auto"),
    ("EICHERMOT.NS", "Eicher Motors"),
    ("TVSMOTOR.NS", "TVS Motor Company"),

    # Pharma
    ("SUNPHARMA.NS", "Sun Pharmaceutical"),
    ("DRREDDY.NS", "Dr Reddys Laboratories"),
    ("CIPLA.NS", "Cipla"),
    ("DIVISLAB.NS", "Divis Laboratories"),
    ("LUPIN.NS", "Lupin"),

    # Telecom
    ("BHARTIARTL.NS", "Bharti Airtel"),
    ("INDUSTOWER.NS", "Indus Towers"),

    # Infrastructure
    ("LT.NS", "Larsen & Toubro"),
    ("ADANIPORTS.NS", "Adani Ports"),
    ("ULTRACEMCO.NS", "UltraTech Cement"),
    ("SIEMENS.NS", "Siemens India"),

    # Financial Services
    ("BAJFINANCE.NS", "Bajaj Finance"),
    ("BAJAJFINSV.NS", "Bajaj Finserv"),

    # Metals
    ("TATASTEEL.NS", "Tata Steel"),
    ("HINDALCO.NS", "Hindalco Industries"),
    ("JSWSTEEL.NS", "JSW Steel")
]

with engine.connect() as conn:

    for ticker, company_name in companies:

        conn.execute(
            text("""
                INSERT IGNORE INTO companies
                (
                    ticker,
                    company_name
                )
                VALUES
                (
                    :ticker,
                    :company_name
                )
            """),
            {
                "ticker": ticker,
                "company_name": company_name
            }
        )

    conn.commit()

print("Companies added successfully.")