from database.data_access import get_all_companies

from ai.watchlist import get_watchlist_table


def get_sector_stocks(sector):

    companies = get_all_companies()

    return companies[
        companies["sector"] == sector
    ]


def rank_sector(sector):

    watchlist = get_watchlist_table()

    companies = get_sector_stocks(sector)

    sector_tickers = companies["ticker"].tolist()

    ranked = watchlist[
        watchlist["ticker"].isin(sector_tickers)
    ]

    print(sector)
    print(len(sector_tickers))
    print(len(ranked))

    return ranked.sort_values(
        by="score",
        ascending=False
    )


def get_all_sector_rankings():

    companies = get_all_companies()

    sectors = sorted(
        companies["sector"].dropna().unique()
    )

    rankings = {}

    for sector in sectors:

        rankings[sector] = rank_sector(
            sector
        )

    return rankings