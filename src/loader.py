import pandas as pd


def load_data(filepath):
    df = pd.read_csv(filepath)

    print("\n===== FIRST 5 ROWS =====")
    print(df.head())

    print("\n===== NUMBER OF USERS =====")
    print(df["user_id"].nunique())

    print("\n===== DATE RANGE =====")
    print(df["date"].min())
    print(df["date"].max())

    print("\n===== MISSING VALUES =====")
    print(df.isnull().sum())

    print("\n===== AVERAGE METRICS =====")
    print(df.mean(numeric_only=True))

    return df