from flask import Flask, render_template, request, redirect, url_for, jsonify
import api_calls

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Articles Routes
@app.route('/articles')
def view_articles():
    articles = api_calls.fetch_articles()
    return render_template('articles.html', articles=articles)

@app.route('/articles/by-category', methods=['GET', 'POST'])
def view_articles_by_category():
    if request.method == 'POST':
        category = request.form.get('category')
        articles = api_calls.fetch_articles_by_category(category)
        return render_template('articles_by_category.html', articles=articles, category=category)
    return render_template('articles_by_category.html', articles=None)

# Categories Route
@app.route('/categories')
def view_categories():
    categories = api_calls.fetch_categories()
    return render_template('categories.html', categories=categories)

# Users Routes
@app.route('/users')
def view_users():
    users = api_calls.fetch_users()
    return render_template('users.html', users=users)

@app.route('/users/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        response = api_calls.create_user(name, email, password)
        return render_template('create_user.html', response=response)
    return render_template('create_user.html')

@app.route('/users/update', methods=['GET', 'POST'])
def update_user():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        new_name = request.form.get('new_name')
        response = api_calls.update_user(user_id, new_name)
        return render_template('update_user.html', response=response)
    return render_template('update_user.html')

@app.route('/users/delete', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        response = api_calls.delete_user(user_id)
        return render_template('delete_user.html', response=response)
    return render_template('delete_user.html')

# User Preferences Routes
@app.route('/user-preferences', methods=['GET', 'POST'])
def view_user_preferences():
    if request.method == 'POST':
        name = request.form.get('name')
        preferences = api_calls.fetch_user_preferences_by_name(name)
        return render_template('user_preferences.html', preferences=preferences, name=name)
    return render_template('user_preferences.html', preferences=None)

@app.route('/user-preferences/update', methods=['GET', 'POST'])
def update_user_preference():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        category = request.form.get('category')
        response = api_calls.update_user_preference(user_id, category)
        return render_template('update_user_preferences.html', response=response)
    return render_template('update_user_preferences.html')

@app.route('/user-preferences/delete', methods=['GET', 'POST'])
def delete_user_preference():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        category = request.form.get('category')
        response = api_calls.delete_user_preference(user_id, category)
        return render_template('delete_user_preferences.html', response=response)
    return render_template('delete_user_preferences.html')

# User Preference Statistics Route
@app.route('/user-preference-stats')
def view_user_preference_stats():
    stats = api_calls.fetch_user_preference_stats()
    return render_template('user_preference_stats.html', stats=stats)

if __name__ == "__main__":
    app.run(debug=True)
