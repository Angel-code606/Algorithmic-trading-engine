import numpy as np

def calculate_risk_score(age, income_stability, investment_horizon, risk_appetite):
    """
    Returns risk score between 1 (low) to 10 (high)
    """
    score = 0

    # Younger investors → higher risk tolerance
    if age < 30:
        score += 3
    elif age < 45:
        score += 2
    else:
        score += 1

    # Income stability (1–3)
    score += income_stability

    # Investment horizon (years)
    if investment_horizon > 10:
        score += 3
    elif investment_horizon > 5:
        score += 2
    else:
        score += 1

    # Self-declared risk appetite (1–3)
    score += risk_appetite

    return min(score, 10)
