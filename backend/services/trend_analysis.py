import numpy as np

def attendance_trend(df):
    """
    Calculates attendance trend slope
    Returns value between 0–100
    """
    if len(df) < 5:
        return 50  # neutral trend if insufficient data

    y = df['status_numeric'].values
    x = np.arange(len(y))

    slope = np.polyfit(x, y, 1)[0]

    # Normalize slope
    if slope > 0:
        return min(100, 50 + slope * 50)
    else:
        return max(0, 50 + slope * 50)
def consecutive_absences(df):
    max_streak = 0
    current_streak = 0

    for status in df['status']:
        if status == 'Absent':
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0

    # Normalize (0–100)
    return min(100, max_streak * 20)
def subject_wise_absence(df, core_subjects):
    subject_scores = []

    for subject in core_subjects:
        sub_df = df[df['subject'] == subject]

        if len(sub_df) == 0:
            continue

        absence_rate = 1 - sub_df['status_numeric'].mean()
        subject_scores.append(absence_rate)

    if not subject_scores:
        return 0

    return int(sum(subject_scores) / len(subject_scores) * 100)
def attendance_consistency(df):
    return int(df['status_numeric'].std() * 100)
def recovery_behavior(df):
    """
    Measures how well attendance recovers after absences
    """
    if len(df) < 10:
        return 50

    recent = df.tail(5)['status_numeric'].mean()
    earlier = df.head(5)['status_numeric'].mean()

    recovery = recent - earlier
    return max(0, min(100, 50 + recovery * 50))
