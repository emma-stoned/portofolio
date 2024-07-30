document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("contact-form");

    form.addEventListener("submit", function (event) {
      const name = document.getElementById("subject").value.trim();
      const email = document.getElementById("email").value.trim();
      const message = document.getElementById("message").value.trim();

      if (!name || !email || !message) {
        event.preventDefault(); // Prevent form submission
        alert("Please fill out all fields.");
      }
    });
  });