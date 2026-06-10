import numpy as np


def detect_pattern(df, column):

    x = np.arange(len(df))

    y = df[column].values

    slope = np.polyfit(x, y, 1)[0]

    mean_value = y.mean()

    normalized_slope = (slope / mean_value) * 100

    start_avg = df[column].iloc[:7].mean()

    end_avg = df[column].iloc[-7:].mean()

    return {
        "metric": column,
        "slope": round(float(slope), 4),
        "normalized_slope": round(float(normalized_slope), 4),
        "mean": round(float(mean_value), 2),
        "start_avg": round(float(start_avg), 2),
        "end_avg": round(float(end_avg), 2)
    }