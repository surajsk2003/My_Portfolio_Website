document.getElementById("contactForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    // Collect form data
    const formData = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        message: document.getElementById("message").value
    };

    // Get the CSRF token for security (assuming you're using Django)
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Get the URL dynamically (use the method you prefer for generating the URL)
    const submitUrl = document.getElementById("contactForm").getAttribute("data-submit-url");

    try {
        // Send the data to the backend
        const response = await fetch(submitUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken
            },
            body: JSON.stringify(formData)
        });

        // Parse the response
        const result = await response.json();

        // Display success or error message below the form
        const responseMessage = document.getElementById("responseMessage");
        if (result.status === "success") {
            responseMessage.textContent = "Message sent successfully!";
            responseMessage.style.color = "green";  // Optional: Change color to green for success
        } else {
            responseMessage.textContent = result.error || "Something went wrong!";
            responseMessage.style.color = "red";  // Optional: Change color to red for error
        }
    } catch (error) {
        // Handle any errors that occur during the fetch request
        console.error("Error submitting form:", error);
        document.getElementById("responseMessage").textContent = "An error occurred, please try again.";
    }
});




// JavaScript for Typing Effect


// live animation

const bgAnimation = document.getElementById('bgAnimation');

const numberOfColorBoxes = 400;

for (let i = 0; i < numberOfColorBoxes; i++) {
    const colorBox = document.createElement('div');
    colorBox.classList.add('colorBox');
    bgAnimation.append(colorBox)
}