function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const role = document.getElementById("role").value;

fetch("http://127.0.0.1:5000/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
        username: username,
        password: password,
        role: role
    })
})

    .then(res => res.json())
    .then(data => {
        if (data.error) {
            document.getElementById("error").innerText = data.error;
        } else {
            if (data.role === "student") {
                localStorage.setItem("student_id", data.student_id);
                window.location.href = "student_dashboard.html";
            } else {
                window.location.href = "faculty_dashboard.html";
            }
        }
    })
    .catch(err => {
        document.getElementById("error").innerText = "Server error";
        console.error(err);
    });
}

