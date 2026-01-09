from utils.db import get_db_connection

def authenticate_user(username, password, role):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT user_id, role, student_id
        FROM users
        WHERE username = %s AND password = %s AND role = %s
        """,
        (username, password, role)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

