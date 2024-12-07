// JavaScript for handling the "View Users" functionality

document.addEventListener('DOMContentLoaded', function () {
    const viewUsersButton = document.getElementById('view-users-button');
    const usersContainer = document.getElementById('users-container');

    if (viewUsersButton) {
        viewUsersButton.addEventListener('click', function () {
            fetch('/api/users')
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(users => {
                    // Clear previous content
                    usersContainer.innerHTML = '';

                    if (users.length === 0) {
                        usersContainer.innerHTML = '<p>No users found.</p>';
                        return;
                    }

                    // Create a list of users
                    const usersList = document.createElement('ul');
                    users.forEach(user => {
                        const userItem = document.createElement('li');
                        userItem.textContent = `Name: ${user.Name}, Email: ${user.Email}`;
                        usersList.appendChild(userItem);
                    });

                    usersContainer.appendChild(usersList);
                })
                .catch(error => {
                    console.error('Error fetching users:', error);
                    usersContainer.innerHTML = '<p>Error fetching users. Please try again later.</p>';
                });
        });
    }
});


