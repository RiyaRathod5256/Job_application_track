// ===========================================
// Elements
// ===========================================

const form = document.getElementById("registerForm");

const username = document.getElementById("username");
const useremail = document.getElementById("useremail");
const userphonenumber = document.getElementById("userphonenumber");
const userpassword = document.getElementById("userpassword");
const confirmpassword = document.getElementById("confirmpassword");

const usernameError = document.getElementById("usernameError");
const emailError = document.getElementById("emailError");
const phoneError = document.getElementById("phoneError");
const passwordError = document.getElementById("passwordError");
const confirmError = document.getElementById("confirmError");

const registerBtn = document.getElementById("registerBtn");

const serverMessage = document.getElementById("serverMessage");

const strengthBar = document.getElementById("strengthBar");
const strengthText = document.getElementById("strengthText");


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

function clearAllBackendErrors(){

    usernameError.textContent = "";
    emailError.textContent = "";
    phoneError.textContent = "";
    passwordError.textContent = "";
    confirmError.textContent = "";

    serverMessage.textContent = "";

    username.classList.remove("input-error");
    useremail.classList.remove("input-error");
    userphonenumber.classList.remove("input-error");
    userpassword.classList.remove("input-error");
    confirmpassword.classList.remove("input-error");

}



// ===========================================
// Username Validation
// ===========================================

function validateUsername(){

    const value = username.value.trim();

    const regex = /^[A-Za-z_][A-Za-z0-9_]*$/;

    if(value===""){

        showError(
            username,
            usernameError,
            "Username is required."
        );

        return false;

    }

    if(value.length<3){

        showError(
            username,
            usernameError,
            "Minimum 3 characters."
        );

        return false;

    }

    if(value.length>70){

        showError(
            username,
            usernameError,
            "Maximum 70 characters."
        );

        return false;

    }

    if(!regex.test(value)){

        showError(
            username,
            usernameError,
            "Username must start with a letter or '_' and contain only letters, digits and underscore."
        );

        return false;

    }


    // Same validation as backend

    const repeated = /(.)\1{5,}/;

    if(repeated.test(value)){

        showError(
            username,
            usernameError,
            "No character can repeat more than 5 times."
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
// Email Validation
// ===========================================

function validateEmail(){

    const value = useremail.value.trim();

    if(value === ""){

        showError(
            useremail,
            emailError,
            "Email is required."
        );

        return false;

    }

    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if(!regex.test(value)){

        showError(
            useremail,
            emailError,
            "Enter a valid email address."
        );

        return false;

    }

    showSuccess(
        useremail,
        emailError
    );

    return true;

}



// ===========================================
// Phone Number Validation
// ===========================================

function validatePhoneNumber(){

    const value = userphonenumber.value.trim();

    if(value === ""){

        showError(
            userphonenumber,
            phoneError,
            "Phone number is required."
        );

        return false;

    }

    const regex = /^[6-9]\d{9}$/;

    if(!regex.test(value)){

        showError(
            userphonenumber,
            phoneError,
            "Phone number must contain exactly 10 digits and start with 6-9."
        );

        return false;

    }


    // Same validation as backend

    for(const digit of value){

        let count = 0;

        for(const d of value){

            if(d === digit){

                count++;

            }

        }

        if(count > 5){

            showError(
                userphonenumber,
                phoneError,
                "No digit can be repeated more than 5 times."
            );

            return false;

        }

    }


    showSuccess(
        userphonenumber,
        phoneError
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

useremail.addEventListener(
    "input",
    validateEmail
);

userphonenumber.addEventListener(
    "input",
    validatePhoneNumber
);

// ===========================================
// Password Validation
// ===========================================

function validatePassword(){

    const value = userpassword.value;

    let strength = 0;

    if(value.length >= 8) strength++;

    if(/[A-Z]/.test(value)) strength++;

    if(/[a-z]/.test(value)) strength++;

    if(/[0-9]/.test(value)) strength++;

    if(/[!@#$%^&*(),.?":{}|<>]/.test(value)) strength++;


    if(value === ""){

        showError(
            userpassword,
            passwordError,
            "Password is required."
        );

        strengthBar.style.width = "0%";
        strengthText.textContent = "";

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

    if(!/[A-Z]/.test(value)){

        showError(
            userpassword,
            passwordError,
            "Password must contain one uppercase letter."
        );

        return false;

    }

    if(!/[a-z]/.test(value)){

        showError(
            userpassword,
            passwordError,
            "Password must contain one lowercase letter."
        );

        return false;

    }

    if(!/[0-9]/.test(value)){

        showError(
            userpassword,
            passwordError,
            "Password must contain one digit."
        );

        return false;

    }

    if(!/[!@#$%^&*(),.?":{}|<>]/.test(value)){

        showError(
            userpassword,
            passwordError,
            "Password must contain one special character."
        );

        return false;

    }

    showSuccess(
        userpassword,
        passwordError
    );


    // Password Strength

    if(strength <= 2){

        strengthBar.style.width = "30%";
        strengthBar.style.background = "#ef4444";

        strengthText.textContent = "Weak";

    }

    else if(strength <= 4){

        strengthBar.style.width = "70%";
        strengthBar.style.background = "#f59e0b";

        strengthText.textContent = "Medium";

    }

    else{

        strengthBar.style.width = "100%";
        strengthBar.style.background = "#22c55e";

        strengthText.textContent = "Strong";

    }

    return true;

}



// ===========================================
// Confirm Password
// ===========================================

function validateConfirmPassword(){

    if(confirmpassword.value === ""){

        showError(
            confirmpassword,
            confirmError,
            "Please confirm your password."
        );

        return false;

    }

    if(confirmpassword.value !== userpassword.value){

        showError(
            confirmpassword,
            confirmError,
            "Passwords do not match."
        );

        return false;

    }

    showSuccess(
        confirmpassword,
        confirmError
    );

    return true;

}
// ===========================================
// Show / Hide Password
// ===========================================

document
.getElementById("togglePassword")
.addEventListener("click",()=>{

    if(userpassword.type==="password"){

        userpassword.type="text";

    }

    else{

        userpassword.type="password";

    }

});


document
.getElementById("toggleConfirm")
.addEventListener("click",()=>{

    if(confirmpassword.type==="password"){

        confirmpassword.type="text";

    }

    else{

        confirmpassword.type="password";

    }

});

userpassword.addEventListener("input",()=>{

    validatePassword();

    validateConfirmPassword();

});

confirmpassword.addEventListener(

    "input",

    validateConfirmPassword

);

// ===========================================
// Submit Form
// ===========================================

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    clearAllBackendErrors();

    const valid =
        validateUsername() &&
        validateEmail() &&
        validatePhoneNumber() &&
        validatePassword() &&
        validateConfirmPassword();

    if (!valid) {
        return;
    }

    registerBtn.disabled = true;
    registerBtn.textContent = "Creating Account...";

    const user = {

        username: username.value.trim(),

        useremail: useremail.value.trim(),

        userphonenumber: userphonenumber.value.trim(),

        userpassword: userpassword.value,

        confirmpassword: confirmpassword.value

    };

    try {

        const response = await fetch("/register/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(user)

        });

        const result = await response.json();


        // ===============================
        // SUCCESS
        // ===============================

        if (response.ok) {

            serverMessage.style.color = "green";
            serverMessage.textContent = result.msg;

            form.reset();

            strengthBar.style.width = "0%";
            strengthText.textContent = "";

            setTimeout(() => {

                window.location.href = "/login";

            }, 1500);

            return;
        }


        // ===============================
        // BACKEND VALIDATION ERRORS
        // ===============================

        if (response.status === 409) {

            const error = result.detail;

            switch (error.field) {

                case "username":

                    showError(
                        username,
                        usernameError,
                        error.message
                    );

                    break;

                case "useremail":

                    showError(
                        useremail,
                        emailError,
                        error.message
                    );

                    break;

                case "userphonenumber":

                    showError(
                        userphonenumber,
                        phoneError,
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

        }


        // ===============================
        // FASTAPI / PYDANTIC (422)
        // ===============================

        else if (response.status === 422) {

            result.detail.forEach(err => {

                const field = err.loc[1];

                switch(field){

                    case "username":

                        showError(
                            username,
                            usernameError,
                            err.msg
                        );

                        break;

                    case "useremail":

                        showError(
                            useremail,
                            emailError,
                            err.msg
                        );

                        break;

                    case "userphonenumber":

                        showError(
                            userphonenumber,
                            phoneError,
                            err.msg
                        );

                        break;

                    case "userpassword":

                        showError(
                            userpassword,
                            passwordError,
                            err.msg
                        );

                        break;

                    case "confirmpassword":

                        showError(
                            confirmpassword,
                            confirmError,
                            err.msg
                        );

                        break;

                }

            });

        }

        else {

            serverMessage.style.color = "red";
            serverMessage.textContent =
                result.detail || "Registration failed.";

        }

    }

    catch (error) {

        console.error(error);

        serverMessage.style.color = "red";

        serverMessage.textContent =
            "Unable to connect to server.";

    }

    finally {

        registerBtn.disabled = false;

        registerBtn.textContent = "Create Account";

    }

});