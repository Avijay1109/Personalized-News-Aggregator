import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import api_calls
import matplotlib.pyplot as plt

# Create the main application window
root = tk.Tk()
root.title("Personalized News Aggregator")
root.geometry("800x600")

# Functionality for each menu option
def view_articles():
    articles = api_calls.fetch_articles()
    if "error" in articles:
        messagebox.showerror("Error", articles["error"])
    else:
        result = "\n".join([f"Title: {article['Title']}" for article in articles])
        messagebox.showinfo("Articles", result)

def view_articles_by_category():
    category = simpledialog.askstring("Input", "Please enter a category:")
    if not category:
        return
    articles = api_calls.fetch_articles_by_category(category)
    if "error" in articles:
        messagebox.showerror("Error", articles["error"])
    else:
        result = "\n".join([f"Title: {article['Title']} - Category: {category}" for article in articles])
        messagebox.showinfo("Articles by Category", result)

def view_categories():
    categories = api_calls.fetch_categories()
    if "error" in categories:
        messagebox.showerror("Error", categories["error"])
    else:
        result = "\n".join([f"Category: {cat['Category']}" for cat in categories])
        messagebox.showinfo("Categories", result)

def view_users():
    users = api_calls.fetch_users()
    if "error" in users:
        messagebox.showerror("Error", users["error"])
    else:
        result = "\n".join([f"User: {user['Name']} - Email: {user['Email']}" for user in users])
        messagebox.showinfo("Users", result)

def create_new_user():
    name = simpledialog.askstring("Input", "Please enter the name:")
    email = simpledialog.askstring("Input", "Please enter the email:")
    password = simpledialog.askstring("Input", "Please enter the password:")
    if not name or not email or not password:
        messagebox.showerror("Error", "Name, Email, and Password are required")
        return
    response = api_calls.create_user(name, email, password)
    if "error" in response:
        messagebox.showerror("Error", response["error"])
    else:
        messagebox.showinfo("Success", f"User created successfully with ID: {response['User_ID']}")

def update_user():
    user_id = simpledialog.askstring("Input", "Please enter the User ID:")
    new_name = simpledialog.askstring("Input", "Please enter the new name:")
    if not user_id or not new_name:
        messagebox.showerror("Error", "User ID and New Name are required")
        return
    response = api_calls.update_user(user_id, new_name)
    if "error" in response:
        messagebox.showerror("Error", response["error"])
    else:
        messagebox.showinfo("Success", f"User updated successfully to: {response['user']['Name']}")

def delete_user():
    user_id = simpledialog.askstring("Input", "Please enter the User ID:")
    if not user_id:
        messagebox.showerror("Error", "User ID is required")
        return
    response = api_calls.delete_user(user_id)
    if "error" in response:
        messagebox.showerror("Error", response["error"])
    else:
        messagebox.showinfo("Success", f"User deleted successfully. Deleted User ID: {response['user']['User_ID']}")

def view_user_preferences():
    name = simpledialog.askstring("Input", "Please enter the user's name:")
    if not name:
        return
    response = api_calls.fetch_user_preferences_by_name(name)
    if "error" in response:
        messagebox.showerror("Error", response["error"])
    else:
        users = response.get("users", [])
        if not users:
            messagebox.showinfo("User Preferences", f"No preferences found for the user name: {name}")
            return
        
        # Assume the first user match
        user = users[0]
        preferences = user.get("Preferences", [])
        if not preferences:
            messagebox.showinfo("User Preferences", f"No preferences found for the user name: {name}")
            return

        result = f"User Name: {user['Name']}\nUser ID: {user['User_ID']}\nPreferences:\n"
        result += "\n".join([f"- {pref['Category']} (ID: {pref['Category_ID']})" for pref in preferences])
        messagebox.showinfo("User Preferences", result)

def update_user_preference():
    user_id = simpledialog.askstring("Input", "Please enter the User ID:")
    category = simpledialog.askstring("Input", "Please enter the Category:")
    if not user_id or not category:
        messagebox.showerror("Error", "User ID and Category are required")
        return
    response = api_calls.update_user_preference(user_id, category)
    if "error" in response:
        messagebox.showerror("Error", response["error"])
    else:
        messagebox.showinfo("Success", "User preference updated successfully")

def delete_user_preference():
    user_id = simpledialog.askstring("Input", "Please enter the User ID:")
    category = simpledialog.askstring("Input", "Please enter the Category to delete preference:")
    if not user_id or not category:
        messagebox.showerror("Error", "User ID and Category are required")
        return
    response = api_calls.delete_user_preference(user_id, category)
    if "error" in response:
        messagebox.showerror("Error", response["error"])
    else:
        messagebox.showinfo("Success", "User preference deleted successfully")

def view_user_preference_stats():
    stats = api_calls.get_user_preference_stats()
    if "error" in stats:
        messagebox.showerror("Error", stats["error"])
    else:
        categories = [stat['Category'] for stat in stats]
        user_counts = [stat['User_Count'] for stat in stats]

        # Create a bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(categories, user_counts, color='skyblue')
        plt.xlabel('Categories')
        plt.ylabel('Number of Users')
        plt.title('User Preferences by Category')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

def exit_app():
    root.quit()

# Create and configure widgets for the UI
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Add buttons for each functionality
buttons = [
    ("1. View Articles", view_articles),
    ("2. View Articles by Category", view_articles_by_category),
    ("3. View Categories", view_categories),
    ("4. View Users", view_users),
    ("5. Create New User", create_new_user),
    ("6. Update User", update_user),
    ("7. Delete User", delete_user),
    ("8. View User Preferences", view_user_preferences),
    ("9. Update User Preference", update_user_preference),
    ("10. Delete User Preference", delete_user_preference),
    ("11. View User Preference Statistics", view_user_preference_stats),
    ("12. Exit", exit_app)
]

for idx, (text, command) in enumerate(buttons):
    ttk.Button(frame, text=text, command=command).grid(row=idx, column=0, pady=5, sticky=tk.W)

# Run the main event loop
root.mainloop()
