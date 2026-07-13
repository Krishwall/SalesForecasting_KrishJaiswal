import pandas as pd
import streamlit as st

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/train.csv",
        encoding="latin1"
    )

    df["Order Date"] = pd.to_datetime(df["Order Date"],format="%d/%m/%Y")

    return df
