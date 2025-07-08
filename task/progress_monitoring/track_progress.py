def track_user_progress(user_data):
    return {
        "mood_trend": "stable" if user_data.get("self_reported_mood") == "good" else "needs attention",
        "sleep_quality": "poor" if user_data.get("sleep_hours", 7) < 6 else "good"
    }