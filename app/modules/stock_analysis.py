import streamlit as st

from screeners.screener import (
    analyze_stock,
    evaluate_stock
)

from screeners.ranking import (
    calculate_score,
    get_risk
)

from screeners.trend import detect_trend

from database.data_access import get_price_history

from analytics.indicators import (
    calculate_sma,
    calculate_rsi,
    calculate_macd
)

from ai.stock_report import generate_stock_report

from app.components.charts import create_price_chart


def render():

    st.header("📈 Stock Analysis")

    col1, col2 = st.columns([4, 1])

    with col1:
        ticker = st.text_input(
            "Ticker",
            value="AAPL"
        )

    with col2:
        analyze_button = st.button(
            "Analyze"
        )

    if analyze_button:

        with st.spinner("Generating AI Analysis..."):

            metrics = analyze_stock(ticker)

            prices = get_price_history(ticker)

            prices = calculate_sma(prices, 20)
            prices = calculate_sma(prices, 50)
            prices = calculate_rsi(prices)
            prices = calculate_macd(prices)

            metrics["recommendation"] = (
                evaluate_stock(metrics)
            )

            # Alpha Score Engine
            metrics["alpha_score"] = calculate_score(metrics)

            metrics["risk_level"] = get_risk(
                metrics["alpha_score"]
            )

            metrics["trend"] = detect_trend(
                metrics
            )

            st.markdown("---")

            if metrics["recommendation"] == "BUY":
                st.success("🟢 Bullish Signal Detected")

            elif metrics["recommendation"] == "SELL":
                st.error("🔴 Bearish Signal Detected")

            else:
                st.warning("🟡 Watchlist Candidate")

            st.subheader(
                f"📊 {ticker} Analysis"
            )

            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                st.metric(
                    "Current Price",
                    f"${metrics['close_price']:.2f}"
                )

            with col2:
                st.metric(
                    "RSI (14)",
                    f"{metrics['rsi']:.2f}"
                )

            with col3:
                st.metric(
                    "MACD",
                    f"{metrics['macd']:.2f}"
                )

            with col4:
                st.metric(
                    "Recommendation",
                    metrics["recommendation"]
                )

            with col5:
                st.metric(
                    "Alpha Score",
                    f"{metrics['alpha_score']}/100"
                )

            st.subheader("📈 Alpha Score")

            st.progress(
                metrics["alpha_score"] / 100
            )

            st.write(
                f"Score: {metrics['alpha_score']}/100"
            )

            st.subheader("📋 Signal Summary")

            st.write(f"""
Recommendation: {metrics['recommendation']}

Trend: {metrics['trend']}

Risk: {metrics['risk_level']}

RSI: {metrics['rsi']:.2f}

MACD: {metrics['macd']:.2f}
""")

            st.info(
                f"Risk Level: {metrics['risk_level']}"
            )

            if metrics["recommendation"] == "BUY":
                st.success("🟢 BUY")

            elif metrics["recommendation"] == "SELL":
                st.error("🔴 SELL")

            else:
                st.warning("🟡 HOLD")

            st.info(
                f"📈 Trend: {metrics['trend']}"
            )

            chart = create_price_chart(
                prices
            )

            st.plotly_chart(
                chart,
                use_container_width=True
            )

            try:
                report = generate_stock_report(
                    metrics
                )

            except Exception:

                report = """
AI analysis currently unavailable.

Technical indicators remain fully operational.
"""

            with st.expander(
                "🤖 AI Analysis Report",
                expanded=True
            ):

                st.markdown(report)

            st.markdown("---")

            st.subheader(
                "📈 Technical Snapshot"
            )

            col1, col2 = st.columns(2)

            with col1:

                if metrics["rsi"] < 30:
                    st.success(
                        "RSI indicates Oversold conditions"
                    )

                elif metrics["rsi"] > 70:
                    st.error(
                        "RSI indicates Overbought conditions"
                    )

                else:
                    st.info(
                        "RSI is Neutral"
                    )

            with col2:

                if metrics["macd"] > metrics["signal"]:
                    st.success(
                        "MACD Bullish Crossover"
                    )

                else:
                    st.error(
                        "MACD Bearish Momentum"
                    )