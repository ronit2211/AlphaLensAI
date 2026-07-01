import sys
import subprocess

import streamlit as st

from config.config import STOCKS
import plotly.express as px
from ai.watchlist import get_watchlist_table


def render():

    # ==================================================
    # HERO SECTION
    # ==================================================

    st.markdown("""
    # 📈 AlphaLensAI

    ### AI-Powered Quantitative Equity Research Platform

    Analyze stocks using technical indicators,
    sector intelligence,
    portfolio analytics,
    AI-generated insights,
    and opportunity ranking.
    """)


    st.markdown("---")

    # ==================================================
    # DASHBOARD METRICS
    # ==================================================

    try:

        watchlist = get_watchlist_table()

        top_stock = (
            watchlist
            .sort_values(
                by="score",
                ascending=False
            )
            .iloc[0]["ticker"]
        )

        avg_score = round(
            watchlist["score"].mean(),
            0
        )

        sector_count = (
            watchlist["sector"]
            .nunique()
        )

    except Exception:

        top_stock = "N/A"
        avg_score = 0
        sector_count = 0

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Stocks Tracked",
            len(STOCKS)
        )

    with col2:

        st.metric(
            "Sectors Covered",
            sector_count
        )

    with col3:

        st.metric(
            "Top Ranked Stock",
            top_stock
        )

    with col4:

        st.metric(
            "Strong Buy Candidates",
            len(
                watchlist[
                    watchlist["recommendation"]
                    == "BUY"
                ]
            )
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            f"""
    ### 🏆 Best Stock

    {top_stock}
    """
        )

    with col2:
        st.success(
            f"""
    ### 📊 Stocks Covered

    {len(STOCKS)}
    """
        )

    with col3:
        st.warning(
            f"""
    ### 🏭 Sectors

    {sector_count}
    """
        )

    st.markdown("---")

    # ==================================================
    # TOP PICKS BY SECTOR
    # ==================================================
    try:

        sector_leaders = (
            watchlist
            .sort_values(
                by="score",
                ascending=False
            )
            .groupby("sector")
            .first()
            .reset_index()
        )

    except Exception:

        st.info(
            "Sector rankings currently unavailable."
        )

    st.subheader("🏆 Top Picks By Sector")

    cols = st.columns(5)

    for i, (_, row) in enumerate(
        sector_leaders.iterrows()
    ):

        with cols[i % 5]:

            st.success(
                f"""
            ### {row['sector']}

            📈 {row['ticker']}

            ⭐ Alpha Score: {row['score']}/100

            🎯 {row['recommendation']}
            """
            )


    st.markdown("---")

    

    st.subheader("🔥 Top 10 Ranked Stocks")

    st.dataframe(
        watchlist.head(10),
        use_container_width=True
    )

    st.markdown("---")

    # ==================================================
    # PLATFORM FEATURES
    # ==================================================

    st.subheader("🚀 Platform Features")

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            """
📈 Stock Analysis

Technical indicators,
Alpha Score,
trend detection,
AI research reports.
"""
        )

        st.info(
            """
⚖️ Stock Comparison

Compare stocks using
RSI,
MACD,
risk level,
Alpha Score.
"""
        )

        st.info(
            """
🔥 AI Watchlist

Ranks market opportunities
using Alpha Score
and technical indicators.
"""
        )

    with col2:

        st.info(
            """
🏭 Sector Watchlists

Discover the strongest
stocks inside each sector.
"""
        )

        st.info(
            """
💼 Portfolio Analytics

Portfolio valuation,
allocation analysis,
diversification score.
"""
        )

        st.info(
            """
🤖 AI Insights

AI-generated market commentary
and stock research.
"""
        )

    st.markdown("---")

    # ==================================================
    # PLATFORM COVERAGE
    # ==================================================

    st.subheader("📈 Market Universe")

    sector_breakdown = (
        watchlist["sector"]
        .value_counts()
    )

    fig = px.pie(
        values=sector_breakdown.values,
        names=sector_breakdown.index,
        title="Sector Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # ==================================================
    # SYSTEM STATUS
    # ==================================================

    st.success(
        """
✅ AlphaLensAI Operational

Built With

• Python

• Streamlit

• Pandas

• Plotly

• Gemini AI

• MySQL
"""
    )

    # ==================================================
    # DATA REFRESH
    # ==================================================

    if st.button("🔄 Refresh Market Data"):

        with st.spinner(
            "Updating market data..."
        ):

            result = subprocess.run(
                [
                    sys.executable,
                    "database/update_market_data.py"
                ],
                capture_output=True,
                text=True
            )

        if result.returncode == 0:

            st.success(
                "Market data updated successfully."
            )

        else:

            st.error(
                result.stderr
            )