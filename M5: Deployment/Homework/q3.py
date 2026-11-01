import pickle
import pandas as pd

with open("pipeline.bin", "rb") as f:
    pipeline = pickle.load(f)

lead = {
    "lead_source": "paid_ads",
    "industry": "technology",
    "employment_status": "employed",
    "location": "north_america",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0,
    "interaction_count": 4,
    "lead_score": 0.41,
}

# Most sklearn pipelines expect a DataFrame; fall back to a list of dicts
# in case the pipeline starts with a DictVectorizer.
try:
    proba = pipeline.predict_proba(pd.DataFrame([lead]))
except Exception:
    proba = pipeline.predict_proba([lead])

print("classes:", getattr(pipeline, "classes_", None))
print("probabilities:", proba[0])
print("P(conversion) =", round(float(proba[0][1]), 3))