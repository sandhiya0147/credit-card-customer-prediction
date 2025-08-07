import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, fcluster

def train():
    df = pd.read_csv("CC GENERAL.csv")
    df.drop("CUST_ID", axis=1, inplace=True)
    df.fillna(df.mean(), inplace=True)

    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)

    linkage_matrix = linkage(scaled, method="ward")
    labels = fcluster(linkage_matrix, t=5, criterion="maxclust")

    df["Cluster"] = labels
    df.to_csv("clustered_data.csv", index=False)

    with open("scaler.pkl", "wb") as f:
        pickle.dump(scaler, f)
    with open("linkage_matrix.pkl", "wb") as f:
        pickle.dump(linkage_matrix, f)

if __name__ == "__main__":
    train()
