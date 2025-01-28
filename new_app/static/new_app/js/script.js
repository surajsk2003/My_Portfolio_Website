document.addEventListener("DOMContentLoaded", function () {
    const submitButton = document.getElementById("submitMessage");
    const responseMessage = document.getElementById("responseMessage");

    submitButton.addEventListener("click", function () {
        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const message = document.getElementById("message").value.trim();

        if (!name || !email || !message) {
            displayResponse("Please fill in all fields.", "error");
            return;
        }

        fetch("/receive-message/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: JSON.stringify({ name, email, message }),
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.status === "success") {
                    displayResponse("Message sent successfully!", "success");
                } else {
                    displayResponse("Failed to send message. Please try again.", "error");
                }
            })
            .catch((error) => {
                console.error("Error:", error);
                displayResponse("An error occurred. Please try again later.", "error");
            });
    });

    function displayResponse(message, type) {
        responseMessage.textContent = message;
        responseMessage.className = `response-message ${type}`;
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split("; ");
            for (let cookie of cookies) {
                if (cookie.startsWith(name + "=")) {
                    cookieValue = decodeURIComponent(cookie.split("=")[1]);
                    break;
                }
            }
        }
        return cookieValue;
    }
});
