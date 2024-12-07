// JavaScript for handling the "View Articles" functionality

document.addEventListener('DOMContentLoaded', function () {
    const articlesContainer = document.getElementById('articles-container');

    if (articlesContainer) {
        // Fetch all articles
        fetch('/api/articles')
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
                    articlesContainer.innerHTML = '<p>No articles available at the moment.</p>';
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
                console.error('Error fetching articles:', error);
                articlesContainer.innerHTML = '<p>Error fetching articles. Please try again later.</p>';
            });
    }
});

