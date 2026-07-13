import pandas as pd
import numpy as np

from sklearn.ensemble import IsolationForest


def detect_anomalies(df):

    weekly = (
        df.groupby("Order Date")["Sales"]
          .sum()
          .resample("W")
          .sum()
          .to_frame()
    )

    # --------------------------
    # Isolation Forest
    # --------------------------

    iso = IsolationForest(
        contamination=0.05,
        random_state=42
    )

    weekly["IF_Anomaly"] = iso.fit_predict(
        weekly[["Sales"]]
    )

    weekly["IF_Anomaly"] = weekly["IF_Anomaly"].map(
        {
            1:0,
            -1:1
        }
    )

    # --------------------------
    # Rolling Z Score
    # --------------------------

    window = 8

    weekly["RollingMean"] = (
        weekly["Sales"]
        .rolling(window)
        .mean()
    )

    weekly["RollingStd"] = (
        weekly["Sales"]
        .rolling(window)
        .std()
    )

    weekly["ZScore"] = (
        (weekly["Sales"]-
         weekly["RollingMean"])
        /
        weekly["RollingStd"]
    )

    weekly["Z_Anomaly"] = (
        weekly["ZScore"]
        .abs()>2
    ).astype(int)

    return weekly