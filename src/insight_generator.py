METRIC_NAMES = {
    "steps": "Physical activity",
    "sleep_hours": "Sleep duration",
    "screen_time_hours": "Screen time",
    "deep_work_hours": "Deep work",
    "exercise_minutes": "Exercise activity"
}


def calculate_confidence(trend):

    abs_trend = abs(trend)

    if abs_trend < 0.5:
        return 0

    elif abs_trend < 1:
        return 0.6

    elif abs_trend < 2:
        return 0.8

    return 0.95


def generate_insight(pattern):

    metric = pattern["metric"]

    readable_name = METRIC_NAMES[metric]

    trend = pattern["normalized_slope"]

    confidence = calculate_confidence(trend)

    if confidence == 0:

        return {
            "insight":
                f"Insufficient evidence for a meaningful trend in {readable_name}.",

            "confidence": 0,

            "evidence":
                f"Trend magnitude was only {trend:.2f}%."
        }

    direction = "increasing" if trend > 0 else "decreasing"

    return {
        "insight":
            f"{readable_name} shows a {direction} trend.",

        "confidence":
            confidence,

        "evidence": (
            f"Average daily value changed from "
            f"{pattern['start_avg']} to {pattern['end_avg']}. "
            f"The overall trend across the 30-day observation period was "
            f"{direction}."
        )
    }