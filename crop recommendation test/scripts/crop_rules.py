# crop_rules.py
import numpy as np

CROPS = {
    "Rice":      {"ph": (5.5, 7.0), "n": (0.06, 1), "p": (10, 80), "k": (50, 150), "temp": (20, 35), "rain": (800, 3000), "organic": (0.8, 5)},
    "Wheat":     {"ph": (6.0, 7.5), "n": (0.03, 0.07), "p": (20, 60), "k": (40, 120), "temp": (10, 25), "rain": (300, 800), "organic": (0.5, 2)},
    "Maize":     {"ph": (5.5, 7.0), "n": (0.04, 1), "p": (15, 70), "k": (40, 140), "temp": (18, 32), "rain": (500, 1200), "organic": (0.5, 3)},
    "Millet":    {"ph": (5.0, 7.0), "n": (0.03, 0.06), "p": (10, 40), "k": (40, 120), "temp": (20, 35), "rain": (400, 900), "organic": (0.5, 2)},
    "Barley":    {"ph": (6.0, 7.5), "n": (0.03, 0.06), "p": (20, 60), "k": (30, 100), "temp": (5, 20), "rain": (200, 700), "organic": (0.4, 2)},
    "Potato":    {"ph": (5.0, 6.5), "n": (0.05, 0.12), "p": (30, 90), "k": (80, 150), "temp": (10, 20), "rain": (500, 900), "organic": (1.2, 5)},
    "Tomato":    {"ph": (5.5, 7.5), "n": (0.04, 0.12), "p": (20, 80), "k": (60, 150), "temp": (20, 30), "rain": (600, 1200), "organic": (1, 5)},
    "Cabbage":   {"ph": (6.0, 7.5), "n": (0.03, 0.08), "p": (20, 60), "k": (40, 120), "temp": (10, 25), "rain": (500, 1000), "organic": (1, 4)},
    "Soybean":   {"ph": (6.0, 7.0), "n": (0.02, 0.05), "p": (20, 60), "k": (40, 120), "temp": (20, 30), "rain": (600, 1000), "organic": (0.8, 3)},
    "Lentil":    {"ph": (6.0, 7.5), "n": (0.02, 0.05), "p": (15, 40), "k": (30, 80), "temp": (10, 25), "rain": (300, 900), "organic": (0.5, 2)},
    "Mustard":   {"ph": (6.0, 7.5), "n": (0.02, 0.06), "p": (15, 50), "k": (30, 100), "temp": (8, 25), "rain": (300, 800), "organic": (0.5, 2)},
    "Onion":     {"ph": (5.5, 7.0), "n": (0.04, 0.10), "p": (20, 60), "k": (40, 120), "temp": (15, 30), "rain": (400, 900), "organic": (1, 4)},
    "Garlic":    {"ph": (5.5, 7.5), "n": (0.03, 0.08), "p": (20, 60), "k": (30, 100), "temp": (10, 25), "rain": (300, 800), "organic": (0.8, 2)},
    "Pea":       {"ph": (6.0, 7.5), "n": (0.02, 0.05), "p": (20, 50), "k": (30, 100), "temp": (8, 25), "rain": (300, 1000), "organic": (0.5, 2)},
}

def score_crop(row, crop_ranges):
    score = 0
    features = {
        "ph": row["ph"],
        "n": row["nitrogen"],
        "p": row["p2o5"],
        "k": row["k"],
        "temp": row["avg_temp"],
        "rain": row["avg_rain"],
        "organic": row["organic"]
    }
    for key, value in features.items():
        low, high = crop_ranges[key]
        if low <= value <= high:
            score += 1  # matches this feature
        else:
            score -= abs(value - np.clip(value, low, high)) / (high - low + 1e-9)
    return score

def recommend_crop(row):
    best_crop = None
    best_score = -9999

    for crop, ranges in CROPS.items():
        crop_score = score_crop(row, ranges)
        if crop_score > best_score:
            best_score = crop_score
            best_crop = crop

    return best_crop
