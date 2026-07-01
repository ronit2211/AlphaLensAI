import streamlit as st

from screeners.sector_watchlist import (
    get_all_sector_rankings
)


def render():

    st.header(
        "📊 Sector Watchlists"
    )

    st.caption(
        "Top opportunities ranked within each sector."
    )

    rankings = get_all_sector_rankings()

    for sector, table in rankings.items():

        st.markdown("---")

        st.subheader(
            f"🏢 {sector}"
        )

        if table.empty:

            st.warning(
                "No stocks found."
            )

            continue

        st.dataframe(
            table.head(5),
            use_container_width=True
        )