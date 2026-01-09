from flask import Flask
from flask_cors import CORS

from routes.auth_routes import auth_bp
from routes.risk_routes import risk_bp
from routes.attendance_routes import attendance_bp
from routes.student_routes import student_bp
from routes.faculty_routes import faculty_bp


app = Flask(__name__)

# ✅ ENABLE CORS PROPERLY
CORS(
    app,
    supports_credentials=True,
    resources={r"/*": {"origins": "*"}}
)

app.register_blueprint(auth_bp)
app.register_blueprint(risk_bp)
app.register_blueprint(attendance_bp)
app.register_blueprint(student_bp)
app.register_blueprint(faculty_bp)


@app.route("/")
def home():
    return {"message": "Attendance Dropout Risk System API Running"}



if __name__ == "__main__":
    app.run(debug=True)
