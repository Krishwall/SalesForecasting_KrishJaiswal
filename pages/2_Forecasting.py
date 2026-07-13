import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data
from utils.forecasting import forecast_xgb

st.set_page_config(page_title="Forecast Explorer", layout="wide")

st.title("📈 Forecast Explorer")

df = load_data()
forecast_type = st.radio(

    "Forecast By",

    ["Category", "Region"],

    horizontal=True

)
if forecast_type == "Category":

    options = sorted(df["Category"].unique())

    selected = st.selectbox(
        "Category",
        options
    )

    series = (

        df[df["Category"] == selected]

        .groupby("Order Date")["Sales"]

        .sum()

        .resample("MS")

        .sum()

    )

else:

    options = sorted(df["Region"].unique())

    selected = st.selectbox(
        "Region",
        options
    )

    series = (

        df[df["Region"] == selected]

        .groupby("Order Date")["Sales"]

        .sum()

        .resample("MS")

        .sum()

    )

months = st.slider(

    "Forecast Horizon",

    min_value=1,

    max_value=3,

    value=3

)
if st.button("Generate Forecast"):

    forecast, mae, rmse = forecast_xgb(

        series,

        months

    )
    fig = px.line(

        x=forecast.index,

        y=forecast.values,

        markers=True,

        labels={

            "x":"Month",

            "y":"Forecasted Sales"

        },

        title="Sales Forecast"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )
    col1, col2 = st.columns(2)

    col1.metric(

        "MAE",

        f"{mae:.2f}"

    )

    col2.metric(

        "RMSE",

        f"{rmse:.2f}"

    )
