// ==============================
// Sidebar Menu Buttons
// ==============================

const menuButtons = document.querySelectorAll(".menu-btn");

// ==============================
// Pages
// ==============================

const pages = {
    dashboard: document.getElementById("dashboard-page"),
    users: document.getElementById("users-page"),
    applications: document.getElementById("applications-page")
};

// ==============================
// Hide All Pages
// ==============================

function hidePages() {

    Object.values(pages).forEach(page => {
        page.style.display = "none";
    });

}

// ==============================
// Show Selected Page
// ==============================

function showPage(pageName) {

    hidePages();

    pages[pageName].style.display = "block";

}

// ==============================
// Active Sidebar Button
// ==============================

function setActive(button) {

    menuButtons.forEach(btn => {
        btn.classList.remove("active");
    });

    button.classList.add("active");

}

// ==============================
// Dashboard
// ==============================

async function loadDashboard() {

    try {

        const response = await fetch("/admin/dashboard");

        const data = await response.json();

        document.getElementById("totalUsers").textContent = data.total_users;
        document.getElementById("totalApplications").textContent = data.total_applications;
        document.getElementById("todayApplications").textContent = data.today_applications;
        
        const tbody =
            document.getElementById("recentApplications");

        tbody.innerHTML = "";

        data.recent_applications.forEach(app => {

            tbody.innerHTML += `
                <tr>
                    <td>${app.username}</td>
                    <td>${app.company}</td>
                    <td>${app.status}</td>
                    <td>${app.date}</td>
                </tr>
            `;

        });


    }
    catch (error) {

        console.error(error);

    }

}

// ==============================
// Users
// ==============================

async function loadUsers() {

    try {

        const response = await fetch("/admin/users");

        const users = await response.json();

        const tbody = document.getElementById("usersTable");

        tbody.innerHTML = "";

        users.forEach(user => {

            tbody.innerHTML += `
                <tr>
                    <td>${user.id}</td>
                    <td>${user.username}</td>
                    <td>${user.email}</td>
                    <td>${user.total_applications}</td>
                    <td>
                        <button class="delete-btn"
                            onclick="deleteUser(${user.id})">
                            Delete
                        </button>
                    </td>
                </tr>
            `;

        });

    }
    catch (error) {

        console.error(error);

    }

}

// ==============================
// Applications
// ==============================

async function loadApplications() {

    try {

        const response = await fetch("/admin/applications");

        const applications = await response.json();

        const tbody = document.getElementById("applicationsTable");

        tbody.innerHTML = "";

        applications.forEach(application => {

            tbody.innerHTML += `
                <tr>
                    <td>${application.username}</td>
                    <td>${application.company}</td>
                    <td>${application.status}</td>
                    <td>${application.date}</td>
                </tr>
            `;

        });

    }
    catch (error) {

        console.error(error);

    }

}

// ==============================
// Delete User
// ==============================

async function deleteUser(id) {

    const confirmDelete = confirm("Are you sure you want to delete this user?");

    if (!confirmDelete)
        return;

    try {

        const response = await fetch(`/admin/users/${id}`, {

            method: "DELETE"

        });

        if (response.ok) {

            alert("User deleted successfully.");

            loadUsers();

        }
        else {

            alert("Unable to delete user.");

        }

    }
    catch (error) {

        console.error(error);

    }

}

// ==============================
// Menu Click Events
// ==============================

menuButtons.forEach(button => {

    button.addEventListener("click", () => {

        const page = button.dataset.page;

        showPage(page);

        setActive(button);

        if (page === "dashboard") {

            loadDashboard();

        }

        if (page === "users") {

            loadUsers();

        }

        if (page === "applications") {

            loadApplications();

        }

    });

});

// ==============================
// Default Page
// ==============================
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
showPage("dashboard");

loadDashboard();