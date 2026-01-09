function loadChart() {
    const studentId = localStorage.getItem("student_id");

    fetch(`http://127.0.0.1:5000/attendance/${studentId}`)
        .then(res => res.json())
        .then(data => {

            if (!data || data.length === 0) {
                console.log("No attendance data");
                return;
            }

            const ctx = document.getElementById("attendanceChart");
            if (!ctx) {
                console.error("Canvas not found");
                return;
            }

            // group data by subject
            const subjectMap = {};
            data.forEach(d => {
                if (!subjectMap[d.subject]) subjectMap[d.subject] = [];
                subjectMap[d.subject].push({
                    x: d.timestamp,
                    y: d.status === "Present" ? 1 : 0
                });
            });

            const datasets = Object.keys(subjectMap).map(sub => ({
                label: sub,
                data: subjectMap[sub],
                borderWidth: 2,
                fill: false,
                tension: 0.3
            }));

            // destroy old chart if exists
            if (window.attChart) {
                window.attChart.destroy();
            }

            window.attChart = new Chart(ctx, {
                type: "line",
                data: { datasets },
                options: {
                    parsing: false,
                    responsive: true,
                    scales: {
                        y: {
                            ticks: {
                                callback: v => v === 1 ? "Present" : "Absent"
                            }
                        },
                        x: {
                            type: "category"
                        }
                    }
                }
            });
        })
        .catch(err => console.error("Chart error:", err));
}

