import streamlit as st
import pandas as pd
from stress_assessment.predict_stress import predict_stress_level
from pattern_recognition.analyze_patterns import extract_patterns
from intervention_matching.recommend_intervention import recommend_intervention
from progress_monitoring.track_progress import track_user_progress

st.set_page_config(page_title="Mental Health & Stress Monitor", layout="centered")

st.title("🧠 Mental Health & Stress Prevention System")
st.markdown("This tool helps you assess stress levels and get personalized mental wellness recommendations.")

st.sidebar.header("📝 Input Daily Data")

# Collect user inputs
sleep_hours = st.sidebar.slider("Sleep Hours", 0, 12, 7)
work_hours = st.sidebar.slider("Work Hours", 0, 16, 8)
exercise_minutes = st.sidebar.slider("Exercise Minutes", 0, 120, 30)
caffeine_intake = st.sidebar.slider("Caffeine Intake (cups/day)", 0, 10, 2)
social_interactions = st.sidebar.slider("Social Interactions (count)", 0, 10, 5)
self_reported_mood = st.sidebar.selectbox("Mood Today", ["very bad", "bad", "neutral", "good", "very good"])

# When user clicks analyze
if st.button("📊 Analyze Now"):
    user_data = {
        "sleep_hours": sleep_hours,
        "work_hours": work_hours,
        "exercise_minutes": exercise_minutes,
        "caffeine_intake": caffeine_intake,
        "social_interactions": social_interactions,
        "self_reported_mood": self_reported_mood
    }

    stress = predict_stress_level(user_data)
    patterns = extract_patterns(user_data)
    recommendation = recommend_intervention(stress, patterns)
    progress = track_user_progress(user_data)

    st.subheader("📌 MENTAL HEALTH REPORT")
    st.write(f"**Stress Level**: {stress}")
    st.write(f"**Identified Patterns**: {', '.join(patterns) if patterns else 'None'}")
    st.write(f"**Recommendation**: {recommendation}")
    st.write("**Progress Report:**")
    st.json(progress)