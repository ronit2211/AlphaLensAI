import streamlit as st
import pandas as pd
import plotly.express as px
from database.data_access import (
    get_all_companies,
    get_price_history,
    get_company_info
)


def render():

    st.header("💼 Portfolio Analytics")

    st.caption(
        "Analyze portfolio performance and diversification."
    )

    st.markdown("---")

    # Load all stocks from DB

    companies = get_all_companies()

    portfolio_stocks = sorted(
        companies["ticker"].tolist()
    )

    st.subheader("Add Holdings")

    holding_count = st.number_input(
        "Number of Holdings",
        min_value=0,
        max_value=20,
        value=0
    )

    holdings = {}

    fportfolio_stocks = ["Select Stock"] + sorted(
    companies["ticker"].tolist()
)

    for i in range(holding_count):

        ticker = st.selectbox(
            f"Stock {i+1}",
            portfolio_stocks,
            index=0,
            key=f"ticker_{i}"
        )

        qty = st.number_input(
            f"Quantity {i+1}",
            min_value=0,
            value=0,
            key=f"qty_{i}"
        )

        if ticker != "Select Stock":
            holdings[ticker] = qty

    st.markdown("---")

    portfolio_rows = []

    total_value = 0

    for ticker, qty in holdings.items():

        try:

            prices = get_price_history(ticker)

            latest_price = prices.iloc[-1]["close_price"]

            company = get_company_info(ticker)

            sector = "Unknown"

            if not company.empty:
                sector = company.iloc[0]["sector"]

            value = latest_price * qty

            total_value += value

            portfolio_rows.append(
                {
                    "ticker": ticker,
                    "sector": sector,
                    "qty": qty,
                    "price": round(latest_price, 2),
                    "value": round(value, 2)
                }
            )

        except Exception:
            pass

    if len(portfolio_rows) == 0:
        st.warning("No holdings available.")
        return

    portfolio_df = pd.DataFrame(
        portfolio_rows
    )

    st.subheader("Portfolio Holdings")

    st.dataframe(
        portfolio_df,
        use_container_width=True
    )

    st.metric(
        "Portfolio Value",
        f"₹{total_value:,.2f}"
    )

    st.markdown("---")

    # Sector Allocation

    sector_df = (
        portfolio_df
        .groupby("sector")["value"]
        .sum()
        .reset_index()
    )

    sector_df["allocation"] = (
        sector_df["value"]
        / total_value
        * 100
    )

    st.subheader("Sector Allocation")

    st.dataframe(
        sector_df[
            [
                "sector",
                "allocation"
            ]
        ],
        use_container_width=True
    )
    fig = px.pie(
        sector_df,
        values="allocation",
        names="sector",
        title="Portfolio Sector Allocation"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    largest_sector = sector_df["allocation"].max()

    diversification_score = max(
        0,
        100 - largest_sector
    )

    st.subheader(
        "📊 Diversification Score"
    )

    st.progress(
        diversification_score / 100
    )

    st.write(
        f"Score: {diversification_score:.0f}/100"
    )
    if diversification_score >= 80:
        st.success("🟢 Excellent Diversification")

    elif diversification_score >= 60:
        st.info("🔵 Good Diversification")

    elif diversification_score >= 40:
        st.warning("🟡 Moderate Concentration")

    else:
        st.error("🔴 Highly Concentrated Portfolio")

    top_sector = sector_df.sort_values(
        by="allocation",
        ascending=False
    ).iloc[0]

    st.success(
        f"""
Top Sector: {top_sector['sector']}

Allocation: {top_sector['allocation']:.2f}%
"""
    )