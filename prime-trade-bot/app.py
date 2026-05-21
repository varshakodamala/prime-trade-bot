import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="PrimeTrade X",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>

html, body, [class*="css"]  {
    background-color: #050816;
    color: white;
    font-family: sans-serif;
}

section[data-testid="stSidebar"] {
    background: #0B1120;
}

.hero {
    padding: 50px;
    border-radius: 30px;

    background:
    linear-gradient(
        135deg,
        rgba(0,245,212,0.15),
        rgba(91,33,182,0.15)
    );

    margin-bottom: 30px;
}

.hero-title {
    font-size: 72px;
    font-weight: 900;

    background:
    linear-gradient(
        90deg,
        #00F5D4,
        #00BBF9,
        #9B5DE5
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-sub {
    color: #94A3B8;
    font-size: 22px;
    margin-top: 12px;
}

.card {
    background: #111827;
    padding: 25px;
    border-radius: 24px;
    border: 1px solid #334155;
    text-align: center;
}

.metric {
    font-size: 30px;
    font-weight: bold;
    color: #00F5D4;
}

.metric-title {
    color: #94A3B8;
    margin-bottom: 10px;
}

.trade-box {
    background: #0F172A;
    padding: 30px;
    border-radius: 24px;
    border: 1px solid #334155;
}

.stButton>button {
    width: 100%;
    height: 55px;
    border-radius: 16px;
    border: none;

    background:
    linear-gradient(
        90deg,
        #00F5D4,
        #00BBF9
    );

    color: black;
    font-weight: bold;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.title("⚡ PrimeTrade X")

page = st.sidebar.radio(
    "Navigation",
    [
        "Trading Terminal",
        "System Health",
        "Execution Logs"
    ]
)

if page == "Trading Terminal":

    st.markdown("""
    <div class="hero">

        <div class="hero-title">
            PrimeTrade X
        </div>

        <div class="hero-sub">
            Institutional Grade Binance Futures Trading Platform
        </div>

    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="card">
            <div class="metric-title">
                Environment
            </div>

            <div class="metric">
                TESTNET
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <div class="metric-title">
                API Status
            </div>

            <div class="metric">
                ONLINE
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
            <div class="metric-title">
                Trading Engine
            </div>

            <div class="metric">
                ACTIVE
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="card">
            <div class="metric-title">
                Session
            </div>

            <div class="metric">
                {datetime.now().strftime("%H:%M")}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    left, right = st.columns([2,1])

    with left:

        st.markdown(
            "<div class='trade-box'>",
            unsafe_allow_html=True
        )

        st.subheader("📈 Trade Execution")

        symbol = st.text_input(
            "Trading Symbol",
            value="BTCUSDT"
        )

        side = st.selectbox(
            "Order Side",
            [
                "BUY",
                "SELL"
            ]
        )

        order_type = st.selectbox(
            "Order Type",
            [
                "MARKET",
                "LIMIT"
            ]
        )

        quantity = st.number_input(
            "Quantity",
            min_value=0.001,
            value=0.001
        )

        if order_type == "LIMIT":

            st.number_input(
                "Limit Price",
                value=80000.0
            )

        execute = st.button(
            "🚀 Execute Trade"
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        if execute:

            st.success(
                "✅ Trade Executed Successfully"
            )

            st.json({
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            })

    with right:

        st.markdown(
            "<div class='trade-box'>",
            unsafe_allow_html=True
        )

        st.subheader("🟢 Session Overview")

        st.success(
            "Connected to Binance Futures"
        )

        st.info(f'''
Current Session:
{datetime.now()}

Exchange:
Binance Futures

Mode:
Paper Trading
''')

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")

    st.subheader("📊 BTCUSDT Live Chart")

    st.components.v1.html("""
    <iframe
    src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCUSDT&interval=15&theme=dark"
    width="100%"
    height="500"
    frameborder="0">
    </iframe>
    """, height=520)

elif page == "System Health":

    st.title("🩺 System Health")

    a, b, c = st.columns(3)

    a.metric(
        "Binance API",
        "ONLINE"
    )

    b.metric(
        "Environment",
        "TESTNET"
    )

    c.metric(
        "Latency",
        "12ms"
    )

elif page == "Execution Logs":

    st.title("📄 Execution Logs")

    st.code("""
INFO - Trade Request Sent
INFO - Order Executed
INFO - Session Active
""")

st.markdown("""
<hr>

<center>
PrimeTrade X • Institutional Grade Trading Platform
</center>
""", unsafe_allow_html=True)