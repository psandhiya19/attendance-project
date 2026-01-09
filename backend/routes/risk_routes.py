from flask import Blueprint, jsonify
from utils.db import get_db_connection

risk_bp = Blueprint("risk", __name__)

@risk_bp.route("/risk/<int:student_id>", methods=["GET"])
def get_risk(student_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Get attendance data
    cursor.execute("""
        SELECT status FROM attendance
        WHERE student_id = %s
    """, (student_id,))
    records = cursor.fetchall()

    total = len(records)
    absent = sum(1 for r in records if r["status"] == "Absent")

    # Default values
    risk_level = "Low Risk"
    risk_score = 20
    reasons = []

    if total == 0:
        risk_level = "No Data"
        risk_score = 0
        reasons.append("No attendance records found")
    else:
        absence_rate = (absent / total) * 100

        if absence_rate > 50:
            risk_level = "High Risk"
            risk_score = 80
            reasons.append("High absence percentage")
        elif absence_rate > 25:
            risk_level = "Medium Risk"
            risk_score = 50
            reasons.append("Moderate absence percentage")
        else:
            reasons.append("Attendance is regular")

    cursor.close()
    conn.close()

    return jsonify({
        "student_id": student_id,
        "risk_level": risk_level,
        "risk_score": risk_score,
        "reasons": reasons
    })
