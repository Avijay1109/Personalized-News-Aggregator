from flask import Flask, render_template, jsonify
from Console import api_calls

# Initialize Flask app
app = Flask(
    __name__,
    template_folder='Web/Templates', 
    static_folder='Web/Static'
)

# Home Route
@app.route('/')
def index():
    return render_template('index.html')

# Route for Articles
@app.route('/articles')
def articles():
    articles = api_calls.fetch_articles()
    if "error" in articles:
        return jsonify({"error": articles["error"]}), 500
    return render_template('articles.html', articles=articles)

# Route for Categories
@app.route('/categories')
def categories():
    categories = api_calls.fetch_categories()
    if "error" in categories:
        return jsonify({"error": categories["error"]}), 500
    return render_template('categories.html', categories=categories)

# Route for Users
@app.route('/users')
def users():
    users = api_calls.fetch_users()
    if "error" in users:
        return jsonify({"error": users["error"]}), 500
    return render_template('users.html', users=users)

# Route for User Preferences
@app.route('/user_preferences')
def user_preferences():
    name = "Enter a user name here or pass this value dynamically"
    preferences = api_calls.fetch_user_preferences_by_name(name)
    if "error" in preferences:
        return jsonify({"error": preferences["error"]}), 500
    return render_template('user_preferences.html', preferences=preferences)

# Test Route
@app.route('/test')
def test():
    return jsonify({"message": "Flask is running properly!"})

if __name__ == "__main__":
    app.run(debug=True)
