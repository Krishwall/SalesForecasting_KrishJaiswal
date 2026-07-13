import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

def create_features(series):

    df = pd.DataFrame({"Sales": series})

    df["Month"] = df.index.month
    df["Year"] = df.index.year
    df["Quarter"] = df.index.quarter

    df["Lag1"] = df["Sales"].shift(1)
    df["Lag2"] = df["Sales"].shift(2)
    df["Lag3"] = df["Sales"].shift(3)

    df["Rolling3"] = df["Sales"].rolling(3).mean()
    df["Rolling6"] = df["Sales"].rolling(6).mean()

    return df.dropna()
def forecast_xgb(series, months):

    data = create_features(series)

    X = data.drop("Sales", axis=1)
    y = data["Sales"]

    split = int(len(data) * 0.8)

    X_train = X.iloc[:split]
    X_test = X.iloc[split:]

    y_train = y.iloc[:split]
    y_test = y.iloc[split:]

    model = XGBRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=4,
        random_state=42
    )

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, pred)
    rmse = np.sqrt(mean_squared_error(y_test, pred))

    history = series.copy()

    forecasts = []

    for _ in range(months):

        future = pd.DataFrame(index=[history.index[-1] + pd.DateOffset(months=1)])

        future["Month"] = future.index.month
        future["Year"] = future.index.year
        future["Quarter"] = future.index.quarter

        future["Lag1"] = history.iloc[-1]
        future["Lag2"] = history.iloc[-2]
        future["Lag3"] = history.iloc[-3]

        future["Rolling3"] = history.iloc[-3:].mean()
        future["Rolling6"] = history.iloc[-6:].mean()

        value = model.predict(future)[0]

        forecasts.append(value)

        history.loc[future.index[0]] = value

    future_index = pd.date_range(
        history.index[-months],
        periods=months,
        freq="MS"
    )

    forecast = pd.Series(
        forecasts,
        index=future_index
    )

    return forecast, mae, rmse
