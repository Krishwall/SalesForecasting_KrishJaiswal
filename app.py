import streamlit as st
import joblib
@st.cache_resource
def load_model():
    return joblib.load("models/xgb_model.pkl")
st.set_page_config(
    page_title="Sales Forecast Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📈 Sales Forecasting Dashboard")

st.markdown("""
Welcome to the **Sales Forecasting Dashboard**.

Use the navigation panel on the left to explore:

- 📊 Sales Overview
- 📈 Forecast Explorer
- 🚨 Anomaly Report
- 📦 Product Demand Segments
""")

st.info("Select a page from the sidebar.")