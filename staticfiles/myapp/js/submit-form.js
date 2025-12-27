document.getElementById("newsletterForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const form = e.target;
    const email = form.querySelector("#newsletter-email").value;
    const successMsg = document.getElementById("newsletter-success");
    const errorMsg = document.getElementById("newsletter-error");

    successMsg.classList.add("hidden");
    errorMsg.classList.add("hidden");

    const response = await fetch(form.action, {
        method: "POST",
        body: new URLSearchParams({ "newsletter-email": email })
    });

    const text = await response.text();

    if (text.includes("✅")) {
        successMsg.classList.remove("hidden");
        form.reset();
    } else {
        errorMsg.classList.remove("hidden");
    }
});

document.getElementById("contactForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const form = e.target;

    // Collect form data
    const formData = new URLSearchParams();
    formData.append("first-name", form.querySelector("#first-name").value.trim());
    formData.append("last-name", form.querySelector("#last-name").value.trim());
    formData.append("email", form.querySelector("#email").value.trim());
    formData.append("subject", form.querySelector("#subject").value.trim());
    formData.append("message", form.querySelector("#message").value.trim());

    // Success & error alert boxes
    const successMsg = document.getElementById("success-message");
    const errorMsg = document.getElementById("error-message");

    // Hide old messages
    successMsg.classList.add("hidden");
    errorMsg.classList.add("hidden");

    try {
        // Send AJAX request
        const response = await fetch(form.action, {
            method: "POST",
            body: formData
        });

        const text = await response.text();

        // Show proper feedback
        if (text.includes("✅")) {
            successMsg.classList.remove("hidden");
            form.reset();

            // Optional: Add fade-out animation after 5s
            setTimeout(() => successMsg.classList.add("hidden"), 5000);
        } else {
            errorMsg.classList.remove("hidden");
            setTimeout(() => errorMsg.classList.add("hidden"), 5000);
        }

    } catch (error) {
        errorMsg.classList.remove("hidden");
        setTimeout(() => errorMsg.classList.add("hidden"), 5000);
    }
});