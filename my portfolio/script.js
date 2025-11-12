// ==========================
// Dark Mode Toggle
// ==========================
const toggleBtn = document.getElementById("theme-toggle");
const body = document.body;

// Load saved theme from localStorage
if (localStorage.getItem("theme") === "dark") {
  body.classList.add("dark");
  if (toggleBtn) toggleBtn.textContent = "☀️ Light Mode";
}

// Toggle dark mode on button click
if (toggleBtn) {
  toggleBtn.addEventListener("click", () => {
    body.classList.toggle("dark");
    const isDark = body.classList.contains("dark");
    toggleBtn.textContent = isDark ? "☀️ Light Mode" : "🌙 Dark Mode";
    localStorage.setItem("theme", isDark ? "dark" : "light");
  });
}

// ==========================
// Scroll Animation for Projects
// ==========================
const projects = document.querySelectorAll(".project");

if (projects.length > 0) {
  // Set initial state
  projects.forEach((project) => {
    project.style.opacity = 0;
    project.style.transform = "translateY(30px)";
    project.style.transition = "all 0.6s ease-out";
  });

  // Animate on scroll
  window.addEventListener("scroll", () => {
    projects.forEach((project) => {
      const rect = project.getBoundingClientRect();
      if (rect.top < window.innerHeight - 100) {
        project.style.opacity = 1;
        project.style.transform = "translateY(0)";
      }
    });
  });
}

// ==========================
// Contact Form Submission
// ==========================
const contactForm = document.getElementById("contactForm");

if (contactForm) {
  contactForm.addEventListener("submit", function (e) {
    e.preventDefault(); // Prevent page reload

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    // Show a simple alert
    alert(`Thank you, ${name}! Your message has been received.`);

    // Reset the form fields
    contactForm.reset();
  });
}
