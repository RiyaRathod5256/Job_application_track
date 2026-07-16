// ===============================
// Home Page JavaScript
// ===============================

// Wait until the page is fully loaded
document.addEventListener("DOMContentLoaded", () => {

    console.log("Home Page Loaded");

    // -------------------------------
    // Smooth Scroll
    // -------------------------------

    const navLinks = document.querySelectorAll('a[href^="#"]');

    navLinks.forEach(link => {

        link.addEventListener("click", function (e) {

            e.preventDefault();

            const target = document.querySelector(this.getAttribute("href"));

            if (target) {

                target.scrollIntoView({
                    behavior: "smooth"
                });

            }

        });

    });

});


// ====================================
// Sticky Navbar Shadow on Scroll
// ====================================

const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", () => {

    if (window.scrollY > 50) {

        navbar.style.boxShadow = "0 8px 25px rgba(0,0,0,.12)";

    } else {

        navbar.style.boxShadow = "0 2px 10px rgba(0,0,0,.08)";

    }

});


// ====================================
// Hero Button Animation
// ====================================

const primaryButton = document.querySelector(".primary-btn");

if (primaryButton) {

    primaryButton.addEventListener("mouseenter", () => {

        primaryButton.style.transform = "translateY(-3px)";

    });

    primaryButton.addEventListener("mouseleave", () => {

        primaryButton.style.transform = "translateY(0px)";

    });

}


// ====================================
// Register Button Animation
// ====================================

const registerButton = document.querySelector(".register-btn");

if (registerButton) {

    registerButton.addEventListener("mouseenter", () => {

        registerButton.style.transform = "scale(1.05)";

    });

    registerButton.addEventListener("mouseleave", () => {

        registerButton.style.transform = "scale(1)";

    });

}