import streamlit as st

from app.modules import (
    home,
    stock_analysis,
    stock_comparison,
    watchlist,
    portfolio,
    sector_watchlist
)

st.set_page_config(
    page_title="AlphaLensAI",
    page_icon="📈",
    layout="wide"
)

# ------------------------
# GLOBAL STYLING
# ------------------------

st.markdown("""
<style>

.main {
    padding-top: 0rem;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

[data-testid="metric-container"] {
    background-color: #1f2937;
    border: 1px solid #374151;
    padding: 20px;
    border-radius: 15px;
}

div.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 48px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ------------------------
# HEADER
# ------------------------
st.markdown("""
<style>
.block-container{
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}
</style>
""", unsafe_allow_html=True)

# ------------------------
# SIDEBAR
# ------------------------

st.sidebar.markdown("# 📊 AlphaLensAI")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📈 Stock Analysis",
        "⚖️ Stock Comparison",
        "🔥 AI Watchlist",
        "💼 Portfolio Analytics",
        "📊 Sector Watchlists",
    ]
)

st.sidebar.markdown("---")

st.sidebar.success(
    "🟢 System Online"
)

st.sidebar.info(
"""
AlphaLensAI v1.0

AI + Quant Finance

NIT Silchar
"""
)

# ------------------------
# ROUTER
# ------------------------

if page == "🏠 Home":
    home.render()

elif page == "📈 Stock Analysis":
    stock_analysis.render()

elif page == "⚖️ Stock Comparison":
    stock_comparison.render()

elif page == "🔥 AI Watchlist":
    watchlist.render()

elif page == "💼 Portfolio Analytics":
    portfolio.render()
    
elif page == "📊 Sector Watchlists":
    sector_watchlist.render()