from flask import Blueprint, jsonify
from utils.db import get_db_connection

student_bp = Blueprint("student", __name__)

@student_bp.route("/student/<int:student_id>")
def get_student(student_id):
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute(
        "SELECT student_id, name, department, year FROM students WHERE student_id = %s",
        (student_id,)
    )
    data = cur.fetchone()

    cur.close()
    conn.close()

    return jsonify(data)
@student_bp.route("/students")
def get_all_students():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("""
        SELECT student_id, name
        FROM students
        ORDER BY student_id
    """)

    data = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(data)
