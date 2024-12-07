// JavaScript for displaying user preference statistics

document.addEventListener('DOMContentLoaded', function () {
    const statsContainer = document.getElementById('stats-container');

    // Fetch user preference statistics from the API
    fetch('/api/user-preferences/stats')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Prepare data for rendering the bar chart
            const categories = data.map(stat => stat.Category);
            const counts = data.map(stat => stat.Count);

            // Create a bar chart using Chart.js
            const canvas = document.createElement('canvas');
            canvas.id = 'statsChart';
            statsContainer.appendChild(canvas);

            new Chart(canvas, {
                type: 'bar',
                data: {
                    labels: categories,
                    datasets: [{
                        label: 'Number of Users',
                        data: counts,
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: 'User Preference Statistics'
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        })
        .catch(error => {
            console.error('Error fetching user preference statistics:', error);
            statsContainer.innerHTML = '<p>Error loading statistics. Please try again later.</p>';
        });
});

