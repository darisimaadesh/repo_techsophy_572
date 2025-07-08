def predict_stress_level(user_data):
    score = 0
    if user_data.get("sleep_hours", 7) < 6:
        score += 2
    if user_data.get("work_hours", 8) > 10:
        score += 3
    if user_data.get("exercise_minutes", 0) < 20:
        score += 2
    if user_data.get("caffeine_intake", 0) > 4:
        score += 1
    if user_data.get("social_interactions", 5) < 2:
        score += 1
    if user_data.get("self_reported_mood", "neutral") in ["bad", "very bad"]:
        score += 3
    return "High" if score >= 7 else "Medium" if score >= 4 else "Low"
