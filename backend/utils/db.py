import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sandhiya@2006",
        database="attendance_db",
        port=3306
    )