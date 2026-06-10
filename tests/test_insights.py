from src.insight_generator import generate_insight


def test_abstain_when_trend_is_small():

    pattern = {
        "metric": "steps",
        "normalized_slope": 0.2,
        "start_avg": 100,
        "end_avg": 102
    }

    result = generate_insight(pattern)

    assert result["confidence"] == 0

def test_increasing_trend_generates_insight():

    pattern = {
        "metric": "steps",
        "normalized_slope": 1.5,
        "start_avg": 100,
        "end_avg": 150
    }

    result = generate_insight(pattern)

    assert "increasing" in result["insight"].lower()

def test_decreasing_trend_generates_insight():

    pattern = {
        "metric": "steps",
        "normalized_slope": -1.5,
        "start_avg": 150,
        "end_avg": 100
    }

    result = generate_insight(pattern)

    assert "decreasing" in result["insight"].lower()