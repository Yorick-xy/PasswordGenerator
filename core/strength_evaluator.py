### core/strength_evaluator.py
import string

def evaluate_strength(password):
    score = 0
    if len(password) >= 12:
        score += 40
    elif len(password) >= 8:
        score += 20
    elif len(password) >= 5:
        score += 10

    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 15
    if any(c.isdigit() for c in password):
        score += 15
    if any(c in string.punctuation for c in password):
        score += 20

    score = min(score, 100)

    if score < 30:
        return score, "Faible", "red"
    elif score < 60:
        return score, "Moyen", "orange"
    elif score < 85:
        return score, "Bon", "yellow"
    else:
        return score, "Fort", "lime"