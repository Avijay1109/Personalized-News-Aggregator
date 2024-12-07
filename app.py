from flask import Flask, render_template
from Console import api_calls

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/articles')
def articles():
    articles = api_calls.fetch_articles()
    return render_template('articles.html', articles=articles)

@app.route('/users')
def users():
    users = api_calls.fetch_users()
    return render_template('users.html', users=users)

@app.route('/user_preferences')
def user_preferences():
    preferences = api_calls.fetch_user_preferences()
    return render_template('user_preferences.html', users=preferences)

@app.route('/categories')
def categories():
    categories = api_calls.fetch_categories()
    return render_template('categories.html', categories=categories)

if __name__ == '__main__':
    app.run(debug=True)