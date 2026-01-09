from services.explainability import generate_risk_reasons

def calculate_final_risk(features):
    score = (
        features['trend'] * 0.35 +
        features['consecutive'] * 0.25 +
        features['subject'] * 0.20 +
        features['recovery'] * 0.10 +
        features['consistency'] * 0.10
    )

    if score >= 70:
        risk = "High Risk"
    elif score >= 40:
        risk = "Medium Risk"
    else:
        risk = "Low Risk"

    reasons = generate_risk_reasons(
        features['trend'],
        features['consecutive'],
        features['subject'],
        features['recovery'],
        features['consistency']
    )

    return risk, int(score), reasons
