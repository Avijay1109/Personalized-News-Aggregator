from flask import Flask, render_template, request, redirect, url_for, flash
import api_calls

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/view-articles')
def view_articles():
    articles = api_calls.fetch_articles()
    if "error" in articles:
        flash(articles["error"], "error")
        return redirect(url_for('home'))
    return render_template('view_articles.html', articles=articles)

@app.route('/view-articles-by-category', methods=['GET', 'POST'])
def view_articles_by_category():
    if request.method == 'POST':
        category = request.form.get('category')
        articles = api_calls.fetch_articles_by_category(category)
        if "error" in articles:
            flash(articles["error"], "error")
            return redirect(url_for('view_articles_by_category'))
        return render_template('view_articles_by_category.html', articles=articles, category=category)
    return render_template('view_articles_by_category_form.html')

@app.route('/view-categories')
def view_categories():
    categories = api_calls.fetch_categories()
    if "error" in categories:
        flash(categories["error"], "error")
        return redirect(url_for('home'))
    return render_template('view_categories.html', categories=categories)

@app.route('/view-users')
def view_users():
    users = api_calls.fetch_users()
    if "error" in users:
        flash(users["error"], "error")
        return redirect(url_for('home'))
    return render_template('view_users.html', users=users)

@app.route('/create-user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        response = api_calls.create_user(name, email, password)
        if "error" in response:
            flash(response["error"], "error")
            return redirect(url_for('create_user'))
        flash(f"User created successfully with ID: {response['User_ID']}", "success")
        return redirect(url_for('home'))
    return render_template('create_user_form.html')

@app.route('/update-user', methods=['GET', 'POST'])
def update_user():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        new_name = request.form.get('new_name')
        response = api_calls.update_user(user_id, new_name)
        if "error" in response:
            flash(response["error"], "error")
            return redirect(url_for('update_user'))
        flash("User updated successfully!", "success")
        return redirect(url_for('home'))
    return render_template('update_user_form.html')

@app.route('/delete-user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        response = api_calls.delete_user(user_id)
        if "error" in response:
            flash(response["error"], "error")
            return redirect(url_for('delete_user'))
        flash("User deleted successfully!", "success")
        return redirect(url_for('home'))
    return render_template('delete_user_form.html')

@app.route('/view-user-preferences', methods=['GET', 'POST'])
def view_user_preferences():
    if request.method == 'POST':
        name = request.form.get('name')
        preferences = api_calls.fetch_user_preferences_by_name(name)
        if "error" in preferences:
            flash(preferences["error"], "error")
            return redirect(url_for('view_user_preferences'))
        return render_template('view_user_preferences.html', preferences=preferences, name=name)
    return render_template('view_user_preferences_form.html')

@app.route('/update-user-preference', methods=['GET', 'POST'])
def update_user_preference():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        category = request.form.get('category')
        response = api_calls.update_user_preference(user_id, category)
        if "error" in response:
            flash(response["error"], "error")
            return redirect(url_for('update_user_preference'))
        flash("User preference updated successfully!", "success")
        return redirect(url_for('home'))
    return render_template('update_user_preference_form.html')

@app.route('/delete-user-preference', methods=['GET', 'POST'])
def delete_user_preference():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        category = request.form.get('category')
        response = api_calls.delete_user_preference(user_id, category)
        if "error" in response:
            flash(response["error"], "error")
            return redirect(url_for('delete_user_preference'))
        flash("User preference deleted successfully!", "success")
        return redirect(url_for('home'))
    return render_template('delete_user_preference_form.html')

@app.route('/view-user-preference-stats')
def view_user_preference_stats():
    stats = api_calls.fetch_user_preference_stats()
    if "error" in stats:
        flash(stats["error"], "error")
        return redirect(url_for('home'))
    return render_template('view_user_preference_stats.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
