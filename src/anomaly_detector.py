def detect_anomalies(df, column):

    mean_value = df[column].mean()

    anomalies = []

    for _, row in df.iterrows():

        value = row[column]

        deviation = ((value - mean_value) / mean_value) * 100

        if abs(deviation) >= 50:

            anomalies.append({
                "date": row["date"],
                "metric": column,
                "value": value,
                "deviation_percent": float(round(deviation, 2))
            })

    return anomalies