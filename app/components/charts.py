from plotly.subplots import make_subplots
import plotly.graph_objects as go


def create_price_chart(df):

    fig = make_subplots(
        rows=4,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.03,
        row_heights=[
            0.55,
            0.15,
            0.15,
            0.15
        ]
    )

    # Candlestick

    fig.add_trace(
        go.Candlestick(
            x=df["trade_date"],
            open=df["open_price"],
            high=df["high_price"],
            low=df["low_price"],
            close=df["close_price"],
            name="Price"
        ),
        row=1,
        col=1
    )

    if "sma_20" in df.columns:

        fig.add_trace(
            go.Scatter(
                x=df["trade_date"],
                y=df["sma_20"],
                name="SMA20"
            ),
            row=1,
            col=1
        )

    if "sma_50" in df.columns:

        fig.add_trace(
            go.Scatter(
                x=df["trade_date"],
                y=df["sma_50"],
                name="SMA50"
            ),
            row=1,
            col=1
        )

    # Volume

    fig.add_trace(
        go.Bar(
            x=df["trade_date"],
            y=df["volume"],
            name="Volume"
        ),
        row=2,
        col=1
    )

    # RSI

    if "rsi_14" in df.columns:

        fig.add_trace(
            go.Scatter(
                x=df["trade_date"],
                y=df["rsi_14"],
                name="RSI (14)"
        ),
        row=3,
        col=1
    )

    fig.add_hrect(
        y0=70,
        y1=100,
        opacity=0.1,
        line_dash="dash",
        row=3,
        col=1
    )

    fig.add_hrect(
        y0=0,
        y1=30,
        opacity=0.1,
        line_dash="dash",
        row=3,
        col=1
    )

    # MACD

    fig.add_trace(
        go.Bar(
            x=df["trade_date"],
            y=df["histogram"],
            name="MACD Hist"
        ),
        row=4,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df["trade_date"],
            y=df["macd"],
            name="MACD"
        ),
        row=4,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df["trade_date"],
            y=df["signal"],
            name="Signal"
        ),
        row=4,
        col=1
    )

    fig.update_layout(
        template="plotly_dark",
        height=850,
        hovermode="x unified",
        xaxis_rangeslider_visible=False,
        title="Professional Trading Dashboard"
    )

    return fig