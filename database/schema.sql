CREATE DATABASE attendance_db;
USE attendance_db;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    year INT
);

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    subject VARCHAR(50),
    date DATE,
    status ENUM('Present','Absent'),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(100),
    role ENUM('student','faculty'),
    student_id INT
);
