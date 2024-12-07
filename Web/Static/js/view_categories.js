// JavaScript for handling the "View Categories" functionality

document.addEventListener('DOMContentLoaded', function () {
    const categoriesContainer = document.getElementById('categories-container');

    if (categoriesContainer) {
        // Fetch all categories
        fetch('/api/categories')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(categories => {
                // Clear previous content
                categoriesContainer.innerHTML = '';

                if (categories.length === 0) {
                    categoriesContainer.innerHTML = '<p>No categories available at the moment.</p>';
                    return;
                }

                // Create a list of categories
                const categoriesList = document.createElement('ul');
                categories.forEach(category => {
                    const categoryItem = document.createElement('li');
                    categoryItem.innerHTML = `<strong>Category:</strong> ${category.Category}<br>
                                               <strong>Description:</strong> ${category.Description}`;
                    categoriesList.appendChild(categoryItem);
                });

                categoriesContainer.appendChild(categoriesList);
            })
            .catch(error => {
                console.error('Error fetching categories:', error);
                categoriesContainer.innerHTML = '<p>Error fetching categories. Please try again later.</p>';
            });
    }
});

