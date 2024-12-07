from flask import Flask, render_template, request, jsonify
import api_calls

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/articles')
def view_articles():
    articles = api_calls.fetch_articles()
    if "error" in articles:
        return jsonify({"error": articles["error"]}), 404
    return render_template('articles.html', articles=articles)

@app.route('/articles/category', methods=['GET', 'POST'])
def view_articles_by_category():
    if request.method == 'POST':
        category = request.form.get('category')
        articles = api_calls.fetch_articles_by_category(category)
        if "error" in articles:
            return jsonify({"error": articles["error"]}), 404
        return render_template('articles.html', articles=articles)
    return render_template('categories.html')

@app.route('/categories')
def view_categories():
    categories = api_calls.fetch_categories()
    if "error" in categories:
        return jsonify({"error": categories["error"]}), 404
    return render_template('categories.html', categories=categories)

@app.route('/users')
def view_users():
    users = api_calls.fetch_users()
    if "error" in users:
        return jsonify({"error": users["error"]}), 404
    return render_template('users.html', users=users)

@app.route('/users/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        response = api_calls.create_user(name, email, password)
        if "error" in response:
            return jsonify({"error": response["error"]}), 400
        return jsonify({"message": "User created successfully!", "User_ID": response["User_ID"]}), 201
    return render_template('create_user.html')

@app.route('/users/update', methods=['GET', 'POST'])
def update_user():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        new_name = request.form.get('new_name')
        response = api_calls.update_user(user_id, new_name)
        if "error" in response:
            return jsonify({"error": response["error"]}), 400
        return jsonify({"message": "User updated successfully!", "user": response["user"]}), 200
    return render_template('update_user.html')

@app.route('/users/delete', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        response = api_calls.delete_user(user_id)
        if "error" in response:
            return jsonify({"error": response["error"]}), 404
        return jsonify({"message": "User deleted successfully!"}), 200
    return render_template('delete_user.html')

@app.route('/user_preferences')
def view_user_preferences():
    name = request.args.get('name')
    preferences = api_calls.fetch_user_preferences_by_name(name)
    if "error" in preferences:
        return jsonify({"error": preferences["error"]}), 404
    return render_template('user_preferences.html', preferences=preferences)

@app.route('/user_preferences/update', methods=['GET', 'POST'])
def update_user_preference():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        category = request.form.get('category')
        response = api_calls.update_user_preference(user_id, category)
        if "error" in response:
            return jsonify({"error": response["error"]}), 400
        return jsonify({"message": "User preference updated successfully!"}), 200
    return render_template('update_user_preference.html')

@app.route('/user_preferences/delete', methods=['GET', 'POST'])
def delete_user_preference():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        category = request.form.get('category')
        response = api_calls.delete_user_preference(user_id, category)
        if "error" in response:
            return jsonify({"error": response["error"]}), 404
        return jsonify({"message": "User preference deleted successfully!"}), 200
    return render_template('delete_user_preference.html')

@app.route('/stats')
def view_user_preference_stats():
    stats = api_calls.get_user_preference_stats()
    if "error" in stats:
        return jsonify({"error": stats["error"]}), 404
    return render_template('stats.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
