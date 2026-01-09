from flask import Blueprint, jsonify
from utils.db import get_db_connection

attendance_bp = Blueprint("attendance", __name__)

@attendance_bp.route("/attendance/<int:student_id>")
def attendance(student_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT 
            date,
            subject,
            status
        FROM attendance
        WHERE student_id = %s
        ORDER BY date
    """

    cursor.execute(query, (student_id,))
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)

from flask import request

@attendance_bp.route("/attendance", methods=["POST"])
def mark_attendance():
    data = request.json
    subject = data["subject"]
    records = data["records"]

    conn = get_db_connection()
    cursor = conn.cursor()

    for r in records:
        cursor.execute("""
            INSERT INTO attendance (student_id, subject, date, status)
            VALUES (%s, %s, CURDATE(), %s)
        """, (r["student_id"], subject, r["status"]))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Attendance saved"})




