import platform
import os
from api_calls import (
    fetch_articles,
    fetch_articles_by_category,
    fetch_categories,
    fetch_users,
    create_user,
    update_user,
    delete_user,
    fetch_user_preferences_by_name,
    update_user_preference,
    delete_user_preference,
    get_user_preference_stats
)

class Term:
    """
    Utility class for text styling and screen clearing.
    """
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

    @classmethod
    def red(cls, text):
        return cls.RED + text + cls.RESET

    @classmethod
    def green(cls, text):
        return cls.GREEN + text + cls.RESET

    @classmethod
    def yellow(cls, text):
        return cls.YELLOW + text + cls.RESET

    @classmethod
    def blue(cls, text):
        return cls.BLUE + text + cls.RESET

    @classmethod
    def clear(cls):
        if platform.system() == "Windows":
            os.system('cls')  # Clear screen for Windows
        else:
            os.system('clear')  # Clear screen for Linux and macOS

def entry_error(txt="Invalid choice!"):
    print(Term.red(txt))
    input("Press Enter to continue...")

# ------------------------------- Menu Functions -------------------------------

def view_articles():
    Term.clear()
    print(Term.blue("Fetching articles..."))
    articles = fetch_articles(limit=10)
    if "error" in articles:
        print(Term.red(articles["error"]))
    else:
        print(Term.green("Articles:"))
        for article in articles:
            print(f"Title: {article['Title']}")
            print(f"Content: {article['Content']}")
            print(f"Authors: {article['Authors']}")
            print(f"Link: {article['URL']}")
            print("-" * 20)
    input(Term.yellow("Press Enter to continue..."))

def view_articles_by_category():
    Term.clear()
    category = input(Term.blue("Enter the category name: "))
    limit = input(Term.blue("Enter the number of articles to fetch (or leave blank for default): "))
    limit = int(limit) if limit else None
    print(Term.blue(f"Fetching articles in category '{category}'..."))
    articles = fetch_articles_by_category(category, limit)
    if "error" in articles:
        print(Term.red(articles["error"]))
    else:
        print(Term.green(f"Articles in '{category}':"))
        for article in articles:
            print(f"Title: {article['Title']}")
            print(f"Category: {article['Category']}")
            print(f"Content: {article['Content']}")
            print("-" * 20)
    input(Term.yellow("Press Enter to continue..."))

def view_categories():
    Term.clear()
    print(Term.blue("Fetching categories..."))
    categories = fetch_categories()
    if "error" in categories:
        print(Term.red(categories["error"]))
    else:
        print(Term.green("Categories:"))
        for category in categories:
            print(f"Category: {category['Category']}")
            print(f"Description: {category['Description']}")
            print("-" * 20)
    input(Term.yellow("Press Enter to continue..."))

def view_users():
    Term.clear()
    choice = input(Term.blue("Do you want to search by name? (y/n): ")).strip().lower()
    if choice == 'y':
        name = input(Term.blue("Enter the name to search: "))
        print(Term.blue(f"Fetching users with name '{name}'..."))
        users = fetch_users(name=name)
    else:
        print(Term.blue("Fetching all users..."))
        users = fetch_users(limit=10)
    if "error" in users:
        print(Term.red(users["error"]))
    else:
        print(Term.green("Users:"))
        for user in users:
            print(f"Name: {user['Name']} | Email: {user['Email']}")
            print("-" * 20)
    input(Term.yellow("Press Enter to continue..."))

def create_new_user():
    Term.clear()
    name = input(Term.blue("Enter user name: "))
    email = input(Term.blue("Enter user email: "))
    password = input(Term.blue("Enter user password: "))
    print(Term.blue("Creating user..."))
    result = create_user(name, email, password)
    if "error" in result:
        print(Term.red(result["error"]))
    else:
        print(Term.green(f"User created successfully! User ID: {result['User_ID']}"))
    input(Term.yellow("Press Enter to continue..."))

def update_user_menu():
    """
    Menu option to update a user's name.
    """
    Term.clear()
    user_id = input(Term.blue("Enter User ID to update: ")).strip()
    new_name = input(Term.blue("Enter new name for the user: ")).strip()
    
    if not user_id or not new_name:
        print(Term.red("User ID and New Name are required."))
        input(Term.yellow("Press Enter to continue..."))
        return

    print(Term.blue("Updating user information..."))
    result = update_user(user_id, new_name)
    if "error" in result:
        print(Term.red(result["error"]))
    else:
        print(Term.green(f"User updated successfully! New Name: {result['user']['Name']}"))
    input(Term.yellow("Press Enter to continue..."))

def delete_user_menu():
    """
    Menu option to delete a user.
    """
    Term.clear()
    user_id = input(Term.blue("Enter User ID to delete: ")).strip()
    
    if not user_id:
        print(Term.red("User ID is required."))
        input(Term.yellow("Press Enter to continue..."))
        return

    print(Term.blue("Deleting user..."))
    result = delete_user(user_id)
    if "error" in result:
        print(Term.red(result["error"]))
    else:
        print(Term.green(f"User deleted successfully! User ID: {result['user']['User_ID']}"))
        if result['user'].get('preferences'):
            print(Term.yellow("Deleted Preferences:"))
            for pref in result['user']['preferences']:
                print(f"  - {pref}")
    input(Term.yellow("Press Enter to continue..."))

def view_user_preferences():
    """
    View user preferences by user name with color-coded terminal output.
    """
    Term.clear()
    name = input(Term.blue("Enter User Name: "))
    print(Term.blue(f"Fetching preferences for user: {name}..."))
    
    preferences = fetch_user_preferences_by_name(name)

    if "error" in preferences:
        print(Term.red(preferences["error"]))
    elif not preferences.get("users", []):
        print(Term.yellow(f"No preferences found for the user name: {name}"))
    else:
        print(Term.green("User Preferences:"))
        for user in preferences["users"]:
            print(Term.blue(f"User ID: {user['User_ID']} | Name: {user['Name']}"))
            for pref in user["Preferences"]:
                print(Term.yellow(f"  - Category: {pref['Category']} (ID: {pref['Category_ID']})"))
    
    input(Term.yellow("Press Enter to continue..."))

def update_user_preference_menu(): 
    Term.clear()
    user_id = input(Term.blue("Enter User ID: "))
    category = input(Term.blue("Enter Category: "))
    print(Term.blue("Updating user preference..."))
    result = update_user_preference(user_id, category)
    if "error" in result:
        print(Term.red(result["error"]))
        print(Term.yellow(result.get("details", "No additional details.")))  # Log backend error details
    else:
        print(Term.green("User preference updated successfully!"))
    input(Term.yellow("Press Enter to continue..."))

def delete_user_preference_menu():
    """Delete an existing user preference."""
    Term.clear()
    user_id = input(Term.blue("Enter User ID: ")).strip()
    category = input(Term.blue("Enter Category to delete preference: ")).strip()
    
    print(Term.yellow("Deleting user preference..."))
    result = delete_user_preference(user_id, category)
    
    if "error" in result:
        print(Term.red(f"Error: {result['error']}"))
    else:
        print(Term.green(f"Preference deleted successfully for User ID: {user_id} and Category: {category}"))
    
    input(Term.yellow("Press Enter to continue..."))

def view_user_preference_stats():
    """Display user preference statistics."""
    print(Term.blue("Fetching user preference statistics..."))
    stats = get_user_preference_stats()
    
    if "error" in stats:
        print(Term.red(f"Error: {stats['error']}"))
    else:
        print(Term.green("User Preference Statistics:"))
        
        # Iterate through each item in the list
        for stat in stats:
            # Extract the category and user count using correct keys
            category = stat.get('Category', 'Unknown Category')
            user_count = stat.get('User_Count', 0)
            
            # Print the category and count
            print(Term.yellow(f"Category: {category}") + Term.yellow(f" - Number of Users: {user_count}"))
    
    input(Term.yellow("Press Enter to continue..."))



# ------------------------------- Main Menu -------------------------------

def main_menu():
    while True:
        Term.clear()
        print(Term.green("--- Personalized News Aggregator ---"))
        print(Term.green("1. View Articles"))
        print(Term.green("2. View Articles by Category"))
        print(Term.green("3. View Categories"))
        print(Term.green("4. View Users"))
        print(Term.green("5. Create New User"))
        print(Term.green("6. Update User"))
        print(Term.green("7. Delete User"))
        print(Term.green("8. View User Preferences"))
        print(Term.green("9. Update User Preference"))
        print(Term.green("10. Delete User Preference"))
        print(Term.green("11. View User Preference Statistics"))
        print(Term.green("12. Exit"))
        choice = input(Term.blue("Enter your choice: ")).strip()
        if choice == '1':
            view_articles()
        elif choice == '2':
            view_articles_by_category()
        elif choice == '3':
            view_categories()
        elif choice == '4':
            view_users()
        elif choice == '5':
            create_new_user()
        elif choice == '6':
            update_user_menu()
        elif choice == '7':
            delete_user_menu()
        elif choice == '8':
            view_user_preferences()
        elif choice == '9':
            update_user_preference_menu()
        elif choice == '10':
            delete_user_preference_menu()
        elif choice == '11':
            view_user_preference_stats()
        elif choice == '12':
            print(Term.blue("Goodbye!"))
            break
        else:
            entry_error()

if __name__ == "__main__":
    main_menu()
