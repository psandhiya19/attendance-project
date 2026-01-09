// =======================
// LOAD FACULTY OVERVIEW
// =======================
function loadFacultyData() {
    const subject = document.getElementById("subjectSelect").value;

    fetch(`http://127.0.0.1:5000/faculty/${subject}`)
        .then(res => res.json())
        .then(data => {
            const table = document.getElementById("facultyTable");
            table.innerHTML = "";

            data.forEach(s => {
                const risk = s.percentage < 75 ? "⚠ At Risk" : "Safe";

                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td>${s.student_id}</td>
                    <td>${s.name}</td>
                    <td>${s.department}</td>
                    <td>${s.percentage}%</td>
                    <td>${risk}</td>
                `;

                if (s.percentage < 75) {
                    tr.style.backgroundColor = "#ffe6e6";
                }

                table.appendChild(tr);
            });
        });
}

// =======================
// SECTION SWITCHING
// =======================
function showOverview() {
    document.getElementById("overviewSection").style.display = "block";
    document.getElementById("markAttendanceSection").style.display = "none";
}

function showMarkAttendance() {
    document.getElementById("overviewSection").style.display = "none";
    document.getElementById("markAttendanceSection").style.display = "block";
    loadMarkAttendance();
}

// =======================
// LOAD STUDENTS FOR MARK ATTENDANCE
// =======================
function loadMarkAttendance() {
    console.log("loadMarkAttendance() called");

    fetch("http://127.0.0.1:5000/students")
        .then(res => {
            console.log("Response status:", res.status);
            return res.json();
        })
        .then(data => {
            console.log("Students data:", data);

            const table = document.getElementById("markAttendanceTable");
            table.innerHTML = "";

            data.forEach(s => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td>${s.student_id}</td>
                    <td>${s.name}</td>
                    <td>
                        <select class="status">
                            <option value="Present">Present</option>
                            <option value="Absent">Absent</option>
                        </select>
                    </td>
                `;
                table.appendChild(tr);
            });

            console.log("Rows added:", table.querySelectorAll("tr").length);
        })
        .catch(err => {
            console.error("Fetch error:", err);
        });
}


// =======================
// SAVE ATTENDANCE
// =======================
function submitAttendance() {
    const subject = document.getElementById("markSubject").value;
    const rows = document.querySelectorAll("#markAttendanceTable tr");

    if (rows.length === 0) {
        alert("No students loaded");
        return;
    }

    const records = [];

    rows.forEach(row => {
        const student_id = row.children[0].innerText;
        const status = row.querySelector(".status").value;

        records.push({ student_id, status });
    });

    fetch("http://127.0.0.1:5000/attendance", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ subject, records })
    })
    .then(res => res.json())
    .then(() => {
        alert("Attendance saved successfully");
        showOverview();
        loadFacultyData();
    })
    .catch(err => {
        console.error(err);
        alert("Error saving attendance");
    });
}

// =======================
// LOGOUT
// =======================
function logout() {
    localStorage.clear();
    window.location.href = "index.html";
}

// =======================
// INITIAL LOAD
// =======================
window.onload = function () {
    showOverview();
    loadFacultyData();
};

