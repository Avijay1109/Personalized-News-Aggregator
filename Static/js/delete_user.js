// JavaScript for handling the "Delete User" functionality

document.addEventListener('DOMContentLoaded', function () {
    const deleteUserForm = document.getElementById('delete-user-form');
    const deleteUserMessage = document.getElementById('delete-user-message');

    if (deleteUserForm) {
        deleteUserForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent the form from refreshing the page

            // Gather form data
            const formData = new FormData(deleteUserForm);
            const userId = formData.get('user_id');

            // Make a DELETE request to remove the user
            fetch(`/api/users/${userId}`, {
                method: 'DELETE'
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    // Display success message
                    deleteUserMessage.innerHTML = `<p class="success">${data.message}</p>`;
                    deleteUserForm.reset(); // Clear the form
                })
                .catch(error => {
                    console.error('Error deleting user:', error);
                    deleteUserMessage.innerHTML = '<p class="error">Error deleting user. Please try again later.</p>';
                });
        });
    }
});

