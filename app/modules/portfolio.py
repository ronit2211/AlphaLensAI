import streamlit as st


def render():

    st.header("💼 Portfolio Analytics")

    st.caption(
        "Analyze portfolio performance, risk, and diversification."
    )

    st.markdown("---")

    # ------------------------
    # Metrics
    # ------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Portfolio Return",
            "12.4%",
            "+2.1%"
        )

    with col2:
        st.metric(
            "Volatility",
            "18.2%",
            "-1.3%"
        )

    with col3:
        st.metric(
            "Sharpe Ratio",
            "1.41",
            "+0.12"
        )

    with col4:
        st.metric(
            "Alpha Score",
            "84/100"
        )

    st.markdown("---")

    # ------------------------
    # Risk
    # ------------------------

    st.subheader("⚠️ Risk Assessment")

    risk_level = "Moderate"

    if risk_level == "Low":
        st.success("🟢 Low Risk")

    elif risk_level == "Moderate":
        st.warning("🟡 Moderate Risk")

    else:
        st.error("🔴 High Risk")

    st.markdown("---")

    # ------------------------
    # Portfolio Health
    # ------------------------

    st.subheader("📊 Portfolio Health")

    health_score = 82

    st.progress(
        health_score / 100
    )

    st.write(
        f"Portfolio Health Score: {health_score}/100"
    )

    st.markdown("---")

    # ------------------------
    # Allocation
    # ------------------------

    st.subheader("🏦 Portfolio Allocation")

    allocation = {
        "AAPL": "40%",
        "MSFT": "30%",
        "RELIANCE.NS": "20%",
        "TCS.NS": "10%"
    }

    st.table(allocation)

    st.markdown("---")

    # ------------------------
    # AI Commentary
    # ------------------------

    st.subheader("🤖 AI Portfolio Commentary")

    st.info(
        """
Your portfolio is primarily concentrated in technology stocks.

Strengths:
• Strong growth potential
• High quality companies

Risks:
• Sector concentration
• Limited diversification

Suggested Action:
Consider adding exposure to Banking, Healthcare,
or Consumer sectors.
"""
    )