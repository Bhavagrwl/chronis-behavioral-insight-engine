import pandas as pd

from src.pattern_detector import detect_pattern


def test_increasing_steps_trend():

    df = pd.DataFrame({
        "steps": [100, 200, 300, 400, 500]
    })

    result = detect_pattern(df, "steps")

    assert result["normalized_slope"] > 0

def test_decreasing_steps_trend():

    df = pd.DataFrame({
        "steps": [500, 400, 300, 200, 100]
    })

    result = detect_pattern(df, "steps")

    assert result["normalized_slope"] < 0