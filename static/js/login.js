// ===========================================
// Elements
// ===========================================

const form = document.getElementById("loginForm");

const username = document.getElementById("username");
const userpassword = document.getElementById("userpassword");

const usernameError = document.getElementById("usernameError");
const passwordError = document.getElementById("passwordError");

const loginBtn = document.getElementById("loginBtn");

const serverMessage = document.getElementById("serverMessage");

const togglePassword = document.getElementById("togglePassword");


// ===========================================
// Utility Functions
// ===========================================

function showError(input, element, message){

    input.classList.remove("input-success");

    input.classList.add("input-error");

    element.textContent = message;

}

function showSuccess(input, element){

    input.classList.remove("input-error");

    input.classList.add("input-success");

    element.textContent = "";

}

function clearErrors(){

    usernameError.textContent = "";

    passwordError.textContent = "";

    serverMessage.textContent = "";

    username.classList.remove(
        "input-error",
        "input-success"
    );

    userpassword.classList.remove(
        "input-error",
        "input-success"
    );

}


// ===========================================
// Show / Hide Password
// ===========================================

togglePassword.addEventListener("click",()=>{

    if(userpassword.type==="password"){

        userpassword.type="text";

        togglePassword.textContent="🙈";

    }

    else{

        userpassword.type="password";

        togglePassword.textContent="👁";

    }

});

// ===========================================
// Username Validation
// ===========================================

function validateUsername(){

    const value = username.value.trim();

    const regex = /^[A-Za-z_][A-Za-z0-9_]*$/;

    if(value === ""){

        showError(
            username,
            usernameError,
            "Username is required."
        );

        return false;

    }

    if(value.length < 3){

        showError(
            username,
            usernameError,
            "Username must be at least 3 characters."
        );

        return false;

    }

    if(value.length > 70){

        showError(
            username,
            usernameError,
            "Username cannot exceed 70 characters."
        );

        return false;

    }

    if(!regex.test(value)){

        showError(
            username,
            usernameError,
            "Invalid username."
        );

        return false;

    }

    showSuccess(
        username,
        usernameError
    );

    return true;

}



// ===========================================
// Password Validation
// ===========================================

function validatePassword(){

    const value = userpassword.value;

    if(value === ""){

        showError(
            userpassword,
            passwordError,
            "Password is required."
        );

        return false;

    }

    if(value.length < 8){

        showError(
            userpassword,
            passwordError,
            "Password must contain at least 8 characters."
        );

        return false;

    }

    showSuccess(
        userpassword,
        passwordError
    );

    return true;

}



// ===========================================
// Live Validation
// ===========================================

username.addEventListener(
    "input",
    validateUsername
);

userpassword.addEventListener(
    "input",
    validatePassword
);


// ===========================================
// Login Form Submit
// ===========================================


loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    loginBtn.disabled = true;
    loginBtn.textContent = "Logging in...";

    try {
        const data = {
            username: username.value,
            userpassword: userpassword.value
        };

        const response = await fetch("/login/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            credentials: "include",
            body: JSON.stringify(data)
        });

        const result = await response.json();

        console.log("Response:", result);
        console.log("Role:", result.role);

        // Login Successful
        if (response.ok) {

            if (result.role === "admin") {
                window.location.href = "/admin";
            } else {
                window.location.href = "/Search_job";
            }

            return;
        }

        // Login Failed
        if (response.status === 422) {

        result.detail.forEach(err => {

        const field = err.loc[1];

        if (field === "username") {
            showError(
                username,
                usernameError,
                err.msg
            );
        }

        if (field === "userpassword") {
            showError(
                userpassword,
                passwordError,
                err.msg
            );
        }

    });

     return;
}
        if (response.status === 401 || response.status === 404) {

            const error = result.detail;

            switch (error.field) {

                case "username":
                    showError(
                        username,
                        usernameError,
                        error.message
                    );
                    break;

                case "userpassword":
                    showError(
                        userpassword,
                        passwordError,
                        error.message
                    );
                    break;

                default:
                    serverMessage.style.color = "red";
                    serverMessage.textContent = error.message;
            }

        } else {

            serverMessage.style.color = "red";
            serverMessage.textContent =
                result.detail || "Login failed.";

        }

    } catch (error) {

        console.error(error);

        serverMessage.style.color = "red";
        serverMessage.textContent = "Unable to connect to server.";

    } finally {

        loginBtn.disabled = false;
        loginBtn.textContent = "Login";

    }
});

