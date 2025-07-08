def recommend_intervention(stress_level, patterns):
    if stress_level == "High":
        return "⚠️ You may be experiencing high stress. Consider speaking with a mental health professional, reduce your workload, and increase sleep and social interaction."
    elif stress_level == "Medium":
        suggestions = []
        if "Sleep deprivation" in patterns:
            suggestions.append("Improve sleep habits.")
        if "High caffeine intake" in patterns:
            suggestions.append("Cut back on caffeine.")
        if "Low social interaction" in patterns:
            suggestions.append("Try to engage in more social activities.")
        return "🟡 Moderate stress. " + " ".join(suggestions if suggestions else ["Keep an eye on daily routines."])
    else:
        if patterns:
            return "✅ Low stress, but note: " + ", ".join(patterns) + ". Try to maintain balance."
        else:
            return "✅ You are in a good state. Maintain current habits and keep monitoring."
