import pandas as pd

def preprocess_attendance(records):
    """
    records: list of attendance rows from DB
    returns: cleaned DataFrame
    """
    df = pd.DataFrame(records)

    # Convert date column
    df['date'] = pd.to_datetime(df['date'])

    # Encode Present/Absent
    df['status_numeric'] = df['status'].apply(
        lambda x: 1 if x == 'Present' else 0
    )

    return df
