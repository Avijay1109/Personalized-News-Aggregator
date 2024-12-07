// JavaScript for handling the "Delete User Preference" functionality

document.addEventListener('DOMContentLoaded', function () {
    const deletePreferenceForm = document.getElementById('delete-preference-form');
    const userIdInput = document.getElementById('user-id-input');
    const categoryInput = document.getElementById('category-input');
    const messageContainer = document.getElementById('message-container');

    if (deletePreferenceForm) {
        deletePreferenceForm.addEventListener('submit', function (event) {
            event.preventDefault();

            const userId = userIdInput.value.trim();
            const category = categoryInput.value.trim();

            if (!userId || !category) {
                messageContainer.innerHTML = '<p>Please provide both User ID and Category.</p>';
                messageContainer.style.color = 'red';
                return;
            }

            // Send DELETE request to remove user preference
            fetch(`/api/user_preferences/${userId}/${category}`, {
                method: 'DELETE',
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(result => {
                    messageContainer.innerHTML = '<p>User preference deleted successfully!</p>';
                    messageContainer.style.color = 'green';
                })
                .catch(error => {
                    console.error('Error deleting user preference:', error);
                    messageContainer.innerHTML = '<p>Error deleting user preference. Please try again later.</p>';
                    messageContainer.style.color = 'red';
                });
        });
    }
});

