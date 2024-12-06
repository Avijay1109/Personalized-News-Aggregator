import requests

BASE_URL = "http://localhost:5000/api"

# ----------------------------------------
# Article Endpoints
# ----------------------------------------

def fetch_articles(limit=10):
    """
    Fetch articles with an optional limit.
    """
    response = requests.get(f"{BASE_URL}/articles?limit={limit}")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch articles. Status code: {response.status_code}"}

def fetch_articles_by_category(category, limit=None):
    """
    Fetch articles by category name with an optional limit.
    """
    url = f"{BASE_URL}/articles/by-category-name?category={category}"
    if limit:
        url += f"&limit={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch articles by category. Status code: {response.status_code}"}

# ----------------------------------------
# Category Endpoints
# ----------------------------------------

def fetch_categories(limit=None):
    """
    Fetch categories with an optional limit.
    """
    url = f"{BASE_URL}/categories"
    if limit:
        url += f"?limit={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch categories. Status code: {response.status_code}"}

# ----------------------------------------
# User Endpoints
# ----------------------------------------

def fetch_users(limit=None, name=None):
    """
    Fetch users with optional limit or by name.
    """
    url = f"{BASE_URL}/users"
    if limit:
        url += f"?limit={limit}"
    elif name:
        url += f"?name={name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch users. Status code: {response.status_code}"}

def create_user(name, email, password):
    """
    Create a new user.
    """
    data = {"Name": name, "Email": email, "Password": password}
    response = requests.post(f"{BASE_URL}/users", json=data)
    if response.status_code == 201:
        return response.json()
    else:
        return {"error": f"Failed to create user. Status code: {response.status_code}"}

# ----------------------------------------
# User Preference Endpoints
# ----------------------------------------

def fetch_user_preferences(limit=None):
    """
    Fetch user preferences with an optional limit.
    """
    url = f"{BASE_URL}/user_preferences"
    if limit:
        url += f"?limit={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch user preferences. Status code: {response.status_code}"}

def update_user_preference(user_id, category):
    """
    Update an existing user preference.
    """
    data = {"Category": category}
    response = requests.put(f"{BASE_URL}/user_preferences/{user_id}", json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to update user preference. Status code: {response.status_code}"}
    
def delete_user_preference(user_id, category):
    """Delete a user preference by user ID and category ID."""
    response = requests.delete(f"{BASE_URL}/user_preferences/{user_id}/{category}")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to delete user preference. Status code: {response.status_code}"}
    
def get_user_preference_stats():
    """
    Fetch user preference statistics from the API.
    """
    response = requests.get(f"{BASE_URL}/user-preferences/stats")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch user preference statistics. Status code: {response.status_code}"}