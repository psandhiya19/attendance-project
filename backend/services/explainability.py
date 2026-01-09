def generate_risk_reasons(
    trend_score,
    consecutive_abs_score,
    subject_abs_score,
    recovery_score,
    consistency_score
):
    reasons = []

    if trend_score < 40:
        reasons.append("Attendance shows a continuous declining trend")

    if consecutive_abs_score >= 60:
        reasons.append("Frequent consecutive absences detected")

    if subject_abs_score >= 50:
        reasons.append("High absence rate in core subjects")

    if recovery_score < 40:
        reasons.append("Poor attendance recovery after previous absences")

    if consistency_score >= 60:
        reasons.append("Irregular attendance pattern observed")

    if not reasons:
        reasons.append("Attendance pattern is stable")

    return reasons
