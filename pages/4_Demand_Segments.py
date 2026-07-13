import streamlit as st
import plotly.express as px

from utils.data_loader import load_data
from utils.clustering import build_clusters

st.set_page_config(
    page_title="Demand Segments",
    layout="wide"
)

st.title("📦 Product Demand Segments")

df = load_data()

feature_df = build_clusters(df)
fig = px.scatter(

    feature_df,

    x="PC1",

    y="PC2",

    color="Segment",

    text="Sub-Category",

    size="TotalSales",

    title="K-Means Product Demand Segments"

)

fig.update_traces(

    textposition="top center"

)

st.plotly_chart(

    fig,

    use_container_width=True

)
st.subheader(
    "Product Demand Segments"
)

st.dataframe(

    feature_df[
        [
            "Sub-Category",
            "Segment",
            "TotalSales",
            "GrowthRate",
            "Volatility",
            "AvgOrderValue"
        ]
    ],

    use_container_width=True

)
strategy = {

    "Growing Demand":
    "Increase inventory gradually while monitoring sales trends.",

    "High Volume, Stable Demand":
    "Maintain higher inventory levels with regular replenishment.",

    "High Value, Rapid Growth":
    "Maintain safety stock and closely monitor demand fluctuations.",

    "Low Volume, Stable Demand":
    "Keep limited inventory and replenish based on demand."

}

st.subheader("Recommended Stocking Strategy")

for segment, recommendation in strategy.items():

    st.markdown(
        f"**{segment}**  \n{recommendation}"
    )
    