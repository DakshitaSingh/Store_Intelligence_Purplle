import streamlit as st
from PIL import Image

from api_client import (
    get_metrics,
    get_funnel,
    get_heatmap,
    get_anomalies,
    get_health,
    get_revenue,
    get_queue
)

from layout_heatmap import (
    layout_heatmap
)

from charts import (
    funnel_chart
)

st.set_page_config(
    page_title="Store Intelligence",
    layout="wide"
)

STORE_ID = "ST1008"

st.title(
    "Store Intelligence Dashboard"
)

# --------------------------------------------------
# API HEALTH
# --------------------------------------------------

health = get_health()

st.success(
    f"API Status: {health['status']}"
)

# --------------------------------------------------
# DATA FETCH
# --------------------------------------------------

metrics = get_metrics(
    STORE_ID
)

revenue = get_revenue(
    STORE_ID
)

queue = get_queue(
    STORE_ID
)

# --------------------------------------------------
# EXECUTIVE KPIs
# --------------------------------------------------

st.divider()

st.subheader(
    "Executive KPIs"
)

k1, k2, k3, k4 = st.columns(4)

k1.metric(
    "Revenue",
    f"₹{revenue['total_revenue']:.0f}"
)

k2.metric(
    "Avg Basket",
    f"₹{revenue['avg_basket']:.0f}"
)

k3.metric(
    "Queue Entries",
    queue["queue_entries"]
)

k4.metric(
    "Avg Wait",
    f"{queue['avg_wait_time_sec']}s"
)

# --------------------------------------------------
# STORE METRICS
# --------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Visitors",
    metrics["unique_visitors"]
)

c2.metric(
    "Transactions",
    metrics["transactions"]
)

c3.metric(
    "Conversion %",
    round(
        metrics["conversion_rate"],
        2
    )
)

c4.metric(
    "Avg Dwell (ms)",
    metrics["avg_dwell_ms"]
)

# --------------------------------------------------
# FUNNEL
# --------------------------------------------------

st.divider()

st.subheader(
    "Conversion Funnel"
)

funnel = get_funnel(
    STORE_ID
)

st.plotly_chart(
    funnel_chart(
        funnel
    ),
    use_container_width=True
)

# --------------------------------------------------
# HEATMAP
# --------------------------------------------------

st.divider()

st.subheader(
    "Store Heatmap"
)

heatmap = get_heatmap(
    STORE_ID
)

st.plotly_chart(
    layout_heatmap(
        heatmap
    ),
    use_container_width=True
)

# --------------------------------------------------
# STORE LAYOUT
# --------------------------------------------------

st.divider()

st.subheader(
    "Store Layout"
)

try:

    image = Image.open(
        "../data/layouts/Store 1 - layout.png"
    )

    st.image(
        image,
        use_container_width=True
    )

except Exception:

    st.warning(
        "Store layout image not found"
    )

# --------------------------------------------------
# STORE HEALTH SUMMARY
# --------------------------------------------------

st.divider()

st.subheader(
    "Store Health Summary"
)

col1, col2 = st.columns(2)

with col1:

    st.write(
        f"Events Ingested: "
        f"{health.get('events_ingested', 0)}"
    )

    st.write(
        f"Transactions Loaded: "
        f"{health.get('transactions_loaded', 0)}"
    )

with col2:

    st.write(
        f"Last Event: "
        f"{health.get('last_event', 'N/A')}"
    )

# --------------------------------------------------
# BUSINESS INSIGHTS
# --------------------------------------------------

st.divider()

st.subheader(
    "Business Insights"
)

left, right = st.columns(2)

with left:

    if metrics[
        "avg_dwell_ms"
    ] > 3000:

        st.success(
            "Customers are spending good time inside the store."
        )

    else:

        st.warning(
            "Low dwell time detected."
        )

with right:

    if metrics[
        "conversion_rate"
    ] < 10:

        st.warning(
            "Low conversion rate."
        )

    else:

        st.success(
            "Healthy conversion performance."
        )

# --------------------------------------------------
# ANOMALIES
# --------------------------------------------------

st.divider()

st.subheader(
    "Anomalies"
)

anomalies = get_anomalies(
    STORE_ID
)

if anomalies:

    st.json(
        anomalies
    )

else:

    st.info(
        "No anomalies detected"
    )