from flask import Blueprint, jsonify
from utils.db import get_db_connection

faculty_bp = Blueprint("faculty", __name__)

@faculty_bp.route("/faculty/<subject>")
def faculty_view(subject):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT 
            s.student_id,
            s.name,
            s.department,
            COALESCE(
                ROUND(SUM(a.status = 'Present') / COUNT(a.status) * 100, 1),
                0
            ) AS percentage
        FROM students s
        LEFT JOIN attendance a
            ON s.student_id = a.student_id
            AND a.subject = %s
        GROUP BY s.student_id, s.name, s.department
        ORDER BY s.student_id
    """

    cursor.execute(query, (subject,))
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)

