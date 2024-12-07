// JavaScript for handling the "Update User Preference" functionality

document.addEventListener('DOMContentLoaded', function () {
    const updatePreferenceForm = document.getElementById('update-preference-form');
    const userIdInput = document.getElementById('user-id-input');
    const categoryInput = document.getElementById('category-input');
    const messageContainer = document.getElementById('message-container');

    if (updatePreferenceForm) {
        updatePreferenceForm.addEventListener('submit', function (event) {
            event.preventDefault();

            const userId = userIdInput.value.trim();
            const category = categoryInput.value.trim();

            if (!userId || !category) {
                messageContainer.innerHTML = '<p>Please provide both User ID and Category.</p>';
                messageContainer.style.color = 'red';
                return;
            }

            // Send PUT request to update user preference
            fetch(`/api/user_preferences/${userId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ Category: category }),
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(result => {
                    messageContainer.innerHTML = '<p>User preference updated successfully!</p>';
                    messageContainer.style.color = 'green';
                })
                .catch(error => {
                    console.error('Error updating user preference:', error);
                    messageContainer.innerHTML = '<p>Error updating user preference. Please try again later.</p>';
                    messageContainer.style.color = 'red';
                });
        });
    }
});

