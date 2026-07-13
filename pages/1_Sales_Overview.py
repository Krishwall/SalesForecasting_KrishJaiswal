import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data

st.set_page_config(page_title="Sales Overview", layout="wide")

st.title("📊 Sales Overview Dashboard")

df = load_data()

# -----------------------
# Filters
# -----------------------
col1, col2, col3 = st.columns(3)

regions = ["All"] + sorted(df["Region"].unique().tolist())
categories = ["All"] + sorted(df["Category"].unique().tolist())
years = ["All"] + sorted(df["Order Date"].dt.year.unique().tolist())

with col1:
    region = st.selectbox("Region", regions)

with col2:
    category = st.selectbox("Category", categories)

with col3:
    year = st.selectbox("Year", years)

filtered = df.copy()

if region != "All":
    filtered = filtered[filtered["Region"] == region]

if category != "All":
    filtered = filtered[filtered["Category"] == category]

if year != "All":
    filtered = filtered[
        filtered["Order Date"].dt.year == year
    ]

st.divider()
yearly = (
    filtered.groupby(filtered["Order Date"].dt.year)["Sales"]
    .sum()
    .reset_index()
)

yearly.columns = ["Year", "Sales"]

fig = px.bar(
    yearly,
    x="Year",
    y="Sales",
    text_auto=".2s",
    title="Total Sales by Year"
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Sales"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
monthly = (
    filtered.groupby(
        pd.Grouper(
            key="Order Date",
            freq="MS"
        )
    )["Sales"]
    .sum()
    .reset_index()
)

fig = px.line(
    monthly,
    x="Order Date",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

fig.update_layout(
    xaxis_title="Month",
    yaxis_title="Sales"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

left, right = st.columns(2)
region_sales = (
    filtered.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig_region = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    title="Sales by Region"
)

left.plotly_chart(
    fig_region,
    use_container_width=True
)
category_sales = (
    filtered.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig_category = px.pie(
    category_sales,
    names="Category",
    values="Sales",
    title="Sales by Category"
)

right.plotly_chart(
    fig_category,
    use_container_width=True
)
