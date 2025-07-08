# You can add utility functions here, e.g., normalization or text cleaning
def normalize_score(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)