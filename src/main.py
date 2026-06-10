from loader import load_data
from pattern_detector import detect_pattern
from insight_generator import generate_insight
from anomaly_detector import detect_anomalies
import json
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

data_file = project_root / "data" / "behavioral_data.csv"

output_file = project_root / "insights.json"

df = load_data(data_file)

users = df["user_id"].unique()

metrics = [
    "steps",
    "sleep_hours",
    "screen_time_hours",
    "deep_work_hours",
    "exercise_minutes"
]

all_insights = []

for user in users:

    user_df = df[df["user_id"] == user]

    print(f"\n\n========== {user} ==========")

    for metric in metrics:

        pattern = detect_pattern(user_df, metric)

        insight = generate_insight(pattern)

        print("\n----------------")
        print(metric)
        print(f"\nInsight: {insight['insight']}")
        print(f"Confidence: {insight['confidence']}")
        print(f"Evidence: {insight['evidence']}")

        all_insights.append({
            "user": user,
            "metric": metric,
            "insight": insight["insight"],
            "confidence": insight["confidence"],
            "evidence": insight["evidence"]
        })

    print("\nANOMALIES")

    for metric in metrics:

        anomalies = detect_anomalies(user_df, metric)

        for anomaly in anomalies:
            print(
                f"Date: {anomaly['date']} | "
                f"Metric: {anomaly['metric']} | "
                f"Deviation: {anomaly['deviation_percent']}%"
            )

with open(output_file, "w") as f:
    json.dump(all_insights, f, indent=4)