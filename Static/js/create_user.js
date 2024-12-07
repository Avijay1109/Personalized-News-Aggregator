// JavaScript for handling the "Create User" functionality

document.addEventListener('DOMContentLoaded', function () {
    const createUserForm = document.getElementById('create-user-form');
    const createUserMessage = document.getElementById('create-user-message');

    if (createUserForm) {
        createUserForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent the form from refreshing the page

            // Gather form data
            const formData = new FormData(createUserForm);
            const userData = {
                Name: formData.get('name'),
                Email: formData.get('email'),
                Password: formData.get('password')
            };

            // Make a POST request to create the user
            fetch('/api/users', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(userData)
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    // Display success message
                    createUserMessage.innerHTML = `<p class="success">User created successfully! User ID: ${data.user.User_ID}</p>`;
                    createUserForm.reset(); // Clear the form
                })
                .catch(error => {
                    console.error('Error creating user:', error);
                    createUserMessage.innerHTML = '<p class="error">Error creating user. Please try again later.</p>';
                });
        });
    }
});

