window.onload = function () {
    loadApplications();
};

// ==========================
// Load Applications
// ==========================

async function loadApplications() {

    try {

        const response = await fetch("/applications", {
            credentials: "include"
        });

        if (!response.ok) {
            throw new Error("Failed to fetch applications.");
        }

        const applications = await response.json();

        displayApplications(applications);

        updateStats(applications);

    } catch (error) {

        console.error(error);

    }

}


// ==========================
// Display Cards
// ==========================

function displayApplications(applications) {

    const container = document.getElementById("applicationsContainer");

    const emptyState = document.getElementById("emptyState");

    container.innerHTML = "";

    if (applications.length === 0) {

        container.style.display = "none";

        emptyState.style.display = "block";

        return;
    }

    container.style.display = "grid";

    emptyState.style.display = "none";


    applications.forEach(app => {

        let badgeClass = app.job_status.toLowerCase();

        container.innerHTML += `

        <div class="application-card">

            <div class="company">

                <h3>${app.company_name}</h3>

                <span class="badge ${badgeClass}">
                    ${app.job_status}
                </span>

            </div>

            <div class="info">

                <p><strong>Role :</strong> ${app.job_role}</p>

                <p><strong>Location :</strong> ${app.job_location}</p>

                <p><strong>Salary :</strong> ${app.salary}</p>

                <p><strong>Applied :</strong> ${app.applied_date}</p>

                <a
                    href="${app.website}"
                    target="_blank"
                    class="website">

                    Visit Company

                </a>

            </div>

            <select
                class="status-select"
                id="status-${app.app_id}">

                <option value="Applied"
                    ${app.job_status=="Applied"?"selected":""}>
                    Applied
                </option>

                <option value="Interview"
                    ${app.job_status=="Interview"?"selected":""}>
                    Interview
                </option>

                <option value="Selected"
                    ${app.job_status=="Selected"?"selected":""}>
                    Selected
                </option>

                <option value="Rejected"
                    ${app.job_status=="Rejected"?"selected":""}>
                    Rejected
                </option>

            </select>

            <div class="buttons">

                <button
                    class="update-btn"
                    onclick="updateStatus(${app.app_id})">

                    Update

                </button>

                <button
                    class="delete-btn"
                    onclick="deleteApplication(${app.app_id})">

                    Delete

                </button>

            </div>

        </div>

        `;

    });

}



// ==========================
// Statistics
// ==========================

function updateStats(applications) {

    let applied = 0;
    let interview = 0;
    let selected = 0;
    let rejected = 0;

    applications.forEach(app => {

        switch (app.job_status.toLowerCase()) {

            case "applied":
                applied++;
                break;

            case "interview":
                interview++;
                break;

            case "selected":
                selected++;
                break;

            case "rejected":
                rejected++;
                break;
        }

    });

    document.getElementById("totalJobs").innerText = applications.length;

    document.getElementById("appliedJobs").innerText = applied;

    document.getElementById("interviewJobs").innerText = interview;

    document.getElementById("selectedJobs").innerText = selected;

    document.getElementById("rejectedJobs").innerText = rejected;

}



// ==========================
// Update Status
// ==========================

async function updateStatus(appId) {

    const status = document.getElementById(`status-${appId}`).value;

    try {

        const response = await fetch(`/applications/${appId}`, {

            method: "PATCH",

            headers: {

                "Content-Type": "application/json"

            },

            credentials: "include",

            body: JSON.stringify({

                job_status: status

            })

        });

        if (!response.ok) {

            alert("Failed to update status.");

            return;
        }

        loadApplications();

    }

    catch (error) {

        console.error(error);

    }

}



// ==========================
// Delete Application
// ==========================

async function deleteApplication(appId) {

    const confirmDelete = confirm("Delete this application?");

    if (!confirmDelete)
        return;

    try {

        const response = await fetch(`/applications/${appId}`, {

            method: "DELETE",

            credentials: "include"

        });

        if (!response.ok) {

            alert("Delete failed.");

            return;

        }

        loadApplications();

    }

    catch (error) {

        console.error(error);

    }

}