def extract_patterns(user_data):
    patterns = []
    if user_data.get("caffeine_intake", 0) > 3:
        patterns.append("High caffeine intake")
    if user_data.get("social_interactions", 5) < 2:
        patterns.append("Low social interaction")
    if user_data.get("sleep_hours", 7) < 5:
        patterns.append("Sleep deprivation")
    return patterns