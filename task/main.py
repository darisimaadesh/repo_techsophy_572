from stress_assessment.predict_stress import predict_stress_level
from pattern_recognition.analyze_patterns import extract_patterns
from intervention_matching.recommend_intervention import recommend_intervention
from progress_monitoring.track_progress import track_user_progress
import pandas as pd

# Load data
df = pd.read_csv("data/lifestyle_data.csv")

# Run pipeline
for index, row in df.iterrows():
    user_data = row.to_dict()
    stress_level = predict_stress_level(user_data)
    patterns = extract_patterns(user_data)
    recommendation = recommend_intervention(stress_level, patterns)
    progress = track_user_progress(user_data)

    print(f"User {index + 1}:")
    print(f"  Stress Level: {stress_level}")
    print(f"  Patterns: {patterns}")
    print(f"  Recommendation: {recommendation}")
    print(f"  Progress: {progress}")
    print("--------------------------------------------------")