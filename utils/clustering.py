import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


def build_clusters(df):

    # -----------------------------
    # Monthly Sales
    # -----------------------------

    monthly = (
        df.groupby(
            [
                "Sub-Category",
                pd.Grouper(
                    key="Order Date",
                    freq="MS"
                )
            ]
        )["Sales"]
        .sum()
        .reset_index()
    )

    features = []

    for subcat, group in monthly.groupby("Sub-Category"):

        group = group.sort_values("Order Date")

        total_sales = group["Sales"].sum()

        volatility = group["Sales"].std()

        yearly = (
            group.groupby(
                group["Order Date"].dt.year
            )["Sales"]
            .sum()
        )

        if len(yearly) > 1:
            growth = (
                (yearly.iloc[-1] -
                 yearly.iloc[0])
                /
                yearly.iloc[0]
            ) * 100
        else:
            growth = 0

        avg_order = (
            df[df["Sub-Category"] == subcat]
            .groupby("Order ID")["Sales"]
            .sum()
            .mean()
        )

        features.append([
            subcat,
            total_sales,
            growth,
            volatility,
            avg_order
        ])

    feature_df = pd.DataFrame(

        features,

        columns=[
            "Sub-Category",
            "TotalSales",
            "GrowthRate",
            "Volatility",
            "AvgOrderValue"
        ]
    )

    # -----------------------------
    # Scaling
    # -----------------------------

    scaler = StandardScaler()

    X = scaler.fit_transform(
        feature_df.drop(
            "Sub-Category",
            axis=1
        )
    )

    # -----------------------------
    # KMeans
    # -----------------------------

    kmeans = KMeans(
        n_clusters=4,
        random_state=42,
        n_init=10
    )

    feature_df["Cluster"] = (
        kmeans.fit_predict(X)
    )

    # -----------------------------
    # PCA
    # -----------------------------

    pca = PCA(n_components=2)

    X_pca = pca.fit_transform(X)

    feature_df["PC1"] = X_pca[:,0]
    feature_df["PC2"] = X_pca[:,1]

    cluster_names = {

        0:"Growing Demand",

        1:"High Volume, Stable Demand",

        2:"High Value, Rapid Growth",

        3:"Low Volume, Stable Demand"

    }

    feature_df["Segment"] = (
        feature_df["Cluster"]
        .map(cluster_names)
    )

    return feature_df