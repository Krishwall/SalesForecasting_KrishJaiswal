import streamlit as st
import plotly.graph_objects as go

from utils.data_loader import load_data
from utils.anomaly import detect_anomalies

st.set_page_config(
    page_title="Anomaly Report",
    layout="wide"
)

st.title("🚨 Sales Anomaly Report")

df = load_data()

weekly = detect_anomalies(df)
fig = go.Figure()

# Weekly Sales

fig.add_trace(

    go.Scatter(

        x=weekly.index,

        y=weekly["Sales"],

        mode="lines",

        name="Weekly Sales"

    )

)

# Isolation Forest

iso = weekly[
    weekly["IF_Anomaly"]==1
]

fig.add_trace(

    go.Scatter(

        x=iso.index,

        y=iso["Sales"],

        mode="markers",

        marker=dict(

            color="red",

            size=10

        ),

        name="Isolation Forest"

    )

)

# Z Score

z = weekly[
    weekly["Z_Anomaly"]==1
]

fig.add_trace(

    go.Scatter(

        x=z.index,

        y=z["Sales"],

        mode="markers",

        marker=dict(

            color="green",

            size=10,

            symbol="x"

        ),

        name="Rolling Z Score"

    )

)

fig.update_layout(

    title="Weekly Sales Anomalies",

    xaxis_title="Week",

    yaxis_title="Sales"

)

st.plotly_chart(

    fig,

    use_container_width=True

)
st.subheader("Detected Anomalies")

anomalies = weekly[
    (weekly["IF_Anomaly"]==1) |
    (weekly["Z_Anomaly"]==1)
][
    [
        "Sales",
        "IF_Anomaly",
        "Z_Anomaly"
    ]
]

st.dataframe(
    anomalies,
    use_container_width=True
)
left,right = st.columns(2)

left.metric(

    "Isolation Forest",

    int(weekly["IF_Anomaly"].sum())

)

right.metric(

    "Rolling Z Score",

    int(weekly["Z_Anomaly"].sum())

)