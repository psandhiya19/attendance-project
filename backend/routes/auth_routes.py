from flask import Blueprint, request, jsonify
from models.user_model import authenticate_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST", "OPTIONS"])
def login():
    # Handle preflight request explicitly
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200

    data = request.get_json()

    user = authenticate_user(data["username"], data["password"],data["role"])

    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({
        "user_id": user["user_id"],
        "role": user["role"],
        "student_id": user["student_id"]
    }), 200


