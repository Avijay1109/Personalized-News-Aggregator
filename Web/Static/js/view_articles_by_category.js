// JavaScript for handling the "View Articles by Category" functionality

document.addEventListener('DOMContentLoaded', function () {
    const categoryForm = document.getElementById('category-form');
    const articlesContainer = document.getElementById('articles-by-category-container');

    if (categoryForm) {
        categoryForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent form submission from refreshing the page

            // Gather the selected category
            const formData = new FormData(categoryForm);
            const category = formData.get('category');

            // Make a request to fetch articles by category
            fetch(`/api/articles/by-category-name?category=${encodeURIComponent(category)}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(articles => {
                    // Clear previous content
                    articlesContainer.innerHTML = '';

                    if (articles.length === 0) {
                        articlesContainer.innerHTML = '<p>No articles found for the selected category.</p>';
                        return;
                    }

                    // Create a list of articles
                    const articlesList = document.createElement('ul');
                    articles.forEach(article => {
                        const articleItem = document.createElement('li');
                        articleItem.innerHTML = `<strong>Title:</strong> ${article.Title}<br>
                                                  <strong>Author:</strong> ${article.Authors}<br>
                                                  <strong>Date:</strong> ${article.Date}<br>
                                                  <strong>URL:</strong> <a href="${article.URL}" target="_blank">Read more</a>`;
                        articlesList.appendChild(articleItem);
                    });

                    articlesContainer.appendChild(articlesList);
                })
                .catch(error => {
                    console.error('Error fetching articles by category:', error);
                    articlesContainer.innerHTML = '<p>Error fetching articles. Please try again later.</p>';
                });
        });
    }
});

