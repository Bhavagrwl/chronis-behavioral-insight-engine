import pandas as pd

from src.anomaly_detector import detect_anomalies


def test_detects_large_positive_deviation():

    df = pd.DataFrame({
        "date": ["d1", "d2", "d3", "d4", "d5"],
        "steps": [100, 100, 100, 100, 300]
    })

    anomalies = detect_anomalies(df, "steps")

    assert len(anomalies) > 0

def test_detects_large_negative_deviation():

    df = pd.DataFrame({
        "date": ["d1", "d2", "d3", "d4", "d5"],
        "steps": [100, 100, 100, 100, 10]
    })

    anomalies = detect_anomalies(df, "steps")

    assert len(anomalies) > 0

def test_no_anomalies_for_stable_behavior():

    df = pd.DataFrame({
        "date": ["d1", "d2", "d3", "d4", "d5"],
        "steps": [100, 102, 101, 99, 100]
    })

    anomalies = detect_anomalies(df, "steps")

    assert len(anomalies) == 0