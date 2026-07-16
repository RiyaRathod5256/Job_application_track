async function searchJobs() {

    const keyword =
        document.getElementById("keyword").value;

    const location =
        document.getElementById("location").value;

    const response =
        await fetch(`/jobs/job_load?keyword=${keyword}&location=${location}`)

    const jobs =
        await response.json();
    console.log(jobs);
    displayJobs(jobs);
}
function displayJobs(jobs){

    const container = document.getElementById("jobs");

    container.innerHTML = "";

    jobs.forEach(job => {

        container.innerHTML += `

        <div class="card">

            <h3>${job.Jobrole}</h3>

            <p><strong>🏢 Company:</strong> ${job.company}</p>

            <p><strong>📍 Location:</strong> ${job.location}</p>

            <p><strong>💼 Type:</strong> ${job.jobtype || "Not Mentioned"}</p>

            <p><strong>💰 Salary:</strong> ${job.salary || "Not Mentioned"}</p>

            <a href="${job.website}" target="_blank">
                Apply Now
            </a>
            <button class="save-btn" onclick='saveJob(${JSON.stringify(job)})'>
                Save Job
            </button>

        </div>

        `;

    });

}
const logoutBtn = document.getElementById("logoutBtn");

logoutBtn.addEventListener("click", async () => {

    try {

        const response = await fetch("/logout", {

            method: "GET",

            credentials: "include"

        });

        if (response.ok) {

            window.location.href = "/";

        }

        else {

            alert("Logout failed.");

        }

    }

    catch (error) {

        console.error(error);

        alert("Unable to connect to server.");

    }

});
async function saveJob(job) {

    try {

        const response = await fetch("/job/save", {

            method: "POST",

            credentials: "include",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(job)

        });

        const data = await response.json();

        if (response.ok) {

            alert(data.message);

            // Optional: Disable button after saving
            const btn = document.getElementById(`save-${job.id}`);

            if (btn) {

                btn.innerText = "Saved ✓";
                btn.disabled = true;

            }

        }

        else {

            alert(data.detail);

        }

    }

    catch(error){

        console.error(error);

        alert("Unable to connect to server.");

    }

}