const studentId = localStorage.getItem("student_id");

fetch(`http://127.0.0.1:5000/risk/${studentId}`)
    .then(res => res.json())
    .then(data => {
        // Risk Level
        document.getElementById("riskLevel").innerText = data.risk_level;

        // Risk Score
        document.getElementById("riskScore").innerText = data.risk_score;

        // Risk Explanation
        const list = document.getElementById("riskReasons");
        list.innerHTML = "";
        data.reasons.forEach(reason => {
            const li = document.createElement("li");
            li.innerText = reason;
            list.appendChild(li);
        });
    })
    .catch(err => {
        console.error(err);
    });

    function showSection(section) {
    document.querySelectorAll(".section").forEach(s => s.style.display = "none");

    document.getElementById(section + "Section").style.display = "block";

    const titles = {
        dashboard: "Student Dashboard",
        attendance: "Attendance",
        risk: "Risk Analysis",
        profile: "Profile"
    };

    document.getElementById("pageTitle").innerText = titles[section];
}
function loadAttendance() {
    const studentId = localStorage.getItem("student_id");

    fetch(`http://127.0.0.1:5000/attendance/${studentId}`)
        .then(res => res.json())
        .then(data => {
            const table = document.getElementById("attendanceTable");
            table.innerHTML = "";

            const subjectStats = {};

            data.forEach(r => {
                if (!subjectStats[r.subject]) {
                    subjectStats[r.subject] = { total: 0, present: 0 };
                }
                subjectStats[r.subject].total++;
                if (r.status === "Present") subjectStats[r.subject].present++;

              const tr = document.createElement("tr");
tr.innerHTML = `
    <td>${r.date}</td>
    <td>${r.subject}</td>
    <td>${r.status}</td>
    <td>-</td>
`;
table.appendChild(tr);

            });

            // Fill percentage per subject
            document.querySelectorAll("#attendanceTable tr").forEach(tr => {
                const subject = tr.children[1].innerText;
                const s = subjectStats[subject];
                tr.children[3].innerText =
                    ((s.present / s.total) * 100).toFixed(1) + "%";
            });
        });
}

function loadRiskAnalysis() {
    const studentId = localStorage.getItem("student_id");

    fetch(`http://127.0.0.1:5000/attendance/${studentId}`)
        .then(res => res.json())
        .then(data => {
            const subjectMap = {};

            data.forEach(r => {
                const sub = r.subject || "General";
                if (!subjectMap[sub]) subjectMap[sub] = { total: 0, absent: 0 };
                subjectMap[sub].total++;
                if (r.status === "Absent") subjectMap[sub].absent++;
            });

            const list = document.getElementById("subjectRiskList");
            list.innerHTML = "";

            Object.keys(subjectMap).forEach(sub => {
                const percent = (subjectMap[sub].absent / subjectMap[sub].total) * 100;

                if (percent > 30) {
                    const li = document.createElement("li");
                    li.innerText = `⚠ ${sub}: ${percent.toFixed(1)}% absence`;
                    list.appendChild(li);
                }
            });

            if (list.innerHTML === "") {
                list.innerHTML = "<li>No subject at risk 🎉</li>";
            }
        });
}
function loadProfile() {
    const studentId = localStorage.getItem("student_id");

    fetch(`http://127.0.0.1:5000/student/${studentId}`)
        .then(res => res.json())
        .then(data => {
            document.getElementById("pName").innerText = data.name;
            document.getElementById("pDept").innerText = data.department;
            document.getElementById("pYear").innerText = data.year;
            document.getElementById("pReg").innerText = "REG" + studentId;
        });
}

function loadDashboard() {
    showSection("dashboard");
    loadRisk();      // already working
      // chart must be loaded here
}
