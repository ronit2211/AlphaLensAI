import streamlit as st


def render():

    # ----------------------------
    # Hero Section
    # ----------------------------

    st.markdown("""
    # 📈 AlphaLensAI

    ### Institutional-Grade Equity Research & Analytics

    Analyze stocks using quantitative indicators,
    AI-generated research reports,
    portfolio analytics and opportunity ranking.
    """)

    st.markdown("---")

    # ----------------------------
    # Dashboard Metrics
    # ----------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Stocks Covered",
            "4",
            "+1 this week"
        )

    with col2:
        st.metric(
            "Technical Indicators",
            "5",
            "+1 this week"
        )

    with col3:
        st.metric(
            "AI Reports Generated",
            "100+",
            "+20 this week"
        )

    with col4:
        st.metric(
            "Portfolio Modules",
            "3"
        )

    st.markdown("---")

    # ----------------------------
    # Platform Features
    # ----------------------------
    st.subheader("Why AlphaLensAI?")
    st.caption(
    "A unified platform combining technical analysis, screening and AI-powered equity research."
)
    st.subheader("🚀 Platform Features")

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
📈 **AI Stock Analysis**

Technical indicators, trend detection,
Alpha Score and AI-generated reports.
""")

        st.info("""
⚖️ **Stock Comparison**

Compare stocks using RSI, MACD,
Risk and Alpha Score.
""")

        st.info("""
🔥 **AI Watchlist**

Automatically ranks the strongest
opportunities in the market.
""")

    with col2:

        st.info("""
💼 **Portfolio Analytics**

Portfolio return, volatility,
Sharpe Ratio and risk assessment.
""")

        st.info("""
📊 **Quantitative Screening**

Rule-based stock screening
using technical indicators.
""")

        st.info("""
🤖 **Gemini AI Insights**

Natural-language research
reports and commentary.
""")

    st.markdown("---")

    # ----------------------------
    # Market Coverage
    # ----------------------------

    st.subheader("📊 Market Coverage")

    st.dataframe(
        {
            "Ticker": [
                "AAPL",
                "MSFT",
                "RELIANCE.NS",
                "TCS.NS"
            ],
            "Market": [
                "US",
                "US",
                "India",
                "India"
            ],
            "Coverage": [
                "Active",
                "Active",
                "Active",
                "Active"
            ]
        },
        use_container_width=True
    )

    st.markdown("---")

    st.success(
       "✅ AlphaLensAI v1.0 Operational"
        "\nBuilt with:"
        "\n• Python"
        "\n• Streamlit"
        "\n• Pandas"
        "\n• Plotly"
        "\n• Gemini AI"
    )