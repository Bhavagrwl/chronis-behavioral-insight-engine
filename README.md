# Behavioral Insight Engine

## Overview

This project analyzes behavioral data and generates:

- Behavioral trends
- Confidence scores
- Evidence-backed insights
- Behavioral anomalies

The solution focuses on explainability and robustness.

---

## Project Structure

```text
src/
├── loader.py
├── pattern_detector.py
├── anomaly_detector.py
├── insight_generator.py
└── main.py

tests/
├── test_patterns.py
├── test_insights.py
└── test_anomalies.py
```

## Installation

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python src/main.py
```

---

## Run Tests

```bash
pytest
```

---

## Output

The application generates:

```text
Insights
Confidence Scores
Evidence
Anomalies
```

and saves structured insights to:

```text
insights.json
```
