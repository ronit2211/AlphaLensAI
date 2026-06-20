import streamlit as st
import pandas as pd
from ai.comparison_report import (
    generate_comparison_report
)
from screeners.ranking import calculate_score, get_risk
from screeners.screener import analyze_stock
from screeners.screener import evaluate_stock
from screeners.trend import detect_trend

def render():

    st.header("⚖️ Stock Comparison")

    col1, col2 = st.columns(2)

    with col1:
        ticker1 = st.text_input(
            "Stock 1",
            value="AAPL"
        )

    with col2:
        ticker2 = st.text_input(
            "Stock 2",
            value="MSFT"
        )

    if st.button("Compare Stocks"):

        stock1 = analyze_stock(
            ticker1
        )


        stock2 = analyze_stock(
            ticker2
        )

        stock1["recommendation"] = evaluate_stock(stock1)
        stock2["recommendation"] = evaluate_stock(stock2)
        stock1["score"] = calculate_score(stock1)
        stock1["risk"] = get_risk(stock1["score"])

        stock2["score"] = calculate_score(stock2)
        stock2["risk"] = get_risk(stock2["score"])


        stock1["trend"] = detect_trend(
            stock1
        )

        stock2["trend"] = detect_trend(
            stock2
        )

        st.markdown("---")

        st.subheader(
            f"⚖️ {ticker1} vs {ticker2}"
        )

        comparison_data = {
            "Metric": [
                "Price",
                "RSI",
                "MACD",
                "Alpha Score",
                "Risk",
                "Trend"
            ],
            ticker1: [
                round(stock1["close_price"], 2),
                round(stock1["rsi"], 2),
                round(stock1["macd"], 2),
                round(stock1["score"], 2),
                stock1["risk"],
                stock1["trend"]
            ],
            ticker2: [
                round(stock2["close_price"], 2),
                round(stock2["rsi"], 2),
                round(stock2["macd"], 2),
                round(stock2["score"], 2),
                stock2["risk"],
                stock2["trend"]
            ]
        }

        comparison_df = pd.DataFrame(comparison_data)

        st.dataframe(
            comparison_df,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("---")

        if stock1["score"] > stock2["score"]:
            winner = ticker1
        elif stock2["score"] > stock1["score"]:
            winner = ticker2
        else:
            winner = "Tie"

        if winner == "Tie":
            st.info("🤝 Both stocks score equally")
        else:
            st.success(f"🏆 Winner: {winner}")

        if winner == "Tie":

            st.info("""
        🤝 Both stocks have similar technical strength.

        Reasons:

        • Similar Alpha Score
        • Comparable RSI setup
        • Similar trend strength
        """)

        else:

            st.info(f"""
        Reasons:

        • Higher Alpha Score
        • Better Technical Setup
        • Stronger Trend

        Winner: {winner}
        """)

        st.markdown("---")

        with st.spinner(
            "Generating AI Comparison..."
        ):

            try:

                report = generate_comparison_report(
                    ticker1,
                    ticker2
                )

            except Exception:

                report = """
            AI comparison currently unavailable.

            Technical comparison, Alpha Scores and trend analysis remain fully operational.
            """

        with st.expander(
            "🤖 AI Comparison Report",
            expanded=True
        ):

            st.markdown(
                report
            )