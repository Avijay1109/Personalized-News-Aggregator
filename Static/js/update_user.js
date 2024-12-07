// JavaScript for handling the "Update User" functionality

document.addEventListener('DOMContentLoaded', function () {
    const updateUserForm = document.getElementById('update-user-form');
    const updateUserMessage = document.getElementById('update-user-message');

    if (updateUserForm) {
        updateUserForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent the form from refreshing the page

            // Gather form data
            const formData = new FormData(updateUserForm);
            const userId = formData.get('user_id');
            const updatedData = {
                Name: formData.get('name')
            };

            // Make a PUT request to update the user
            fetch(`/api/users/${userId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(updatedData)
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    // Display success message
                    updateUserMessage.innerHTML = `<p class="success">User updated successfully! New Name: ${data.user.Name}</p>`;
                    updateUserForm.reset(); // Clear the form
                })
                .catch(error => {
                    console.error('Error updating user:', error);
                    updateUserMessage.innerHTML = '<p class="error">Error updating user. Please try again later.</p>';
                });
        });
    }
});

