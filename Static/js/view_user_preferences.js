// JavaScript for handling the "View User Preferences" functionality

document.addEventListener('DOMContentLoaded', function () {
    const preferencesContainer = document.getElementById('preferences-container');
    const userIdInput = document.getElementById('user-id-input');
    const fetchPreferencesButton = document.getElementById('fetch-preferences-button');

    if (fetchPreferencesButton) {
        fetchPreferencesButton.addEventListener('click', function () {
            const userId = userIdInput.value.trim();

            if (!userId) {
                preferencesContainer.innerHTML = '<p>Please enter a valid User ID.</p>';
                return;
            }

            // Fetch user preferences by User ID
            fetch(`/api/user_preferences/${userId}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(preferences => {
                    // Clear previous content
                    preferencesContainer.innerHTML = '';

                    if (preferences.length === 0) {
                        preferencesContainer.innerHTML = '<p>No preferences found for this user.</p>';
                        return;
                    }

                    // Create a list of user preferences
                    const preferencesList = document.createElement('ul');
                    preferences.forEach(pref => {
                        const preferenceItem = document.createElement('li');
                        preferenceItem.innerHTML = `<strong>Category:</strong> ${pref.Category}<br>
                                                     <strong>Category ID:</strong> ${pref.Category_ID}`;
                        preferencesList.appendChild(preferenceItem);
                    });

                    preferencesContainer.appendChild(preferencesList);
                })
                .catch(error => {
                    console.error('Error fetching user preferences:', error);
                    preferencesContainer.innerHTML = '<p>Error fetching user preferences. Please try again later.</p>';
                });
        });
    }
});

