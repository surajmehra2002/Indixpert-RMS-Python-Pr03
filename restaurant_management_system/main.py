import json
import os
from users.authentication import authenticate_user
# from packages.menu_management.menu import Menu
# from packages.order_management.order import Order
# from packages.billing_system.billing import Billing
from users.admin import Admin
from users.client import Client

def load_users():
    """Load users from the JSON file or initialize if the file doesn't exist or is empty."""
    file_path = r'data/users.json'
    
    # Check if the file exists
    if not os.path.exists(file_path):
        print("Users file not found, creating a new one.")
        with open(file_path, 'w') as f:
            json.dump([], f)  # Initialize with an empty list
    
    # Load users from the file
    with open(file_path, 'r') as f:
        try:
            users = json.load(f)
            if not users:  # If the file is empty
                print("No users found in the system. Please create an admin user.")
                return None
            return users
        except json.JSONDecodeError:
            print("Error decoding users.json. Please ensure it's a valid JSON file.")
            return None

def save_user(user_data):
    """Save the new user to users.json."""
    file_path = 'data/users.json'
    
    # Check if the file is empty or contains invalid data
    if os.path.getsize(file_path) == 0:
        users = []  # If the file is empty, initialize an empty list
    else:
        with open(file_path, 'r+') as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                print("Error reading users.json. Initializing with an empty list.")
                users = []
    
    # Append the new user data to the list
    users.append(user_data)
    
    # Save the updated list of users back to the file
    with open(file_path, 'w') as f:
        json.dump(users, f, indent=4)


def create_admin_user():
    """Create the first admin user if no users exist."""
    print("Creating a new admin user.")
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    
    admin_user = {
        "username": username,
        "password": password,
        "role": "admin"
    }
    
    save_user(admin_user)
    print("Admin user created successfully!")
    return admin_user

def create_client_user():
    """Create the first admin user if no users exist."""
    print("Creating a new client user.")
    username = input("Enter client username: ")
    password = input("Enter client password: ")
    
    client_user = {
        "username": username,
        "password": password,
        "role": "client"
    }
    
    save_user(client_user)
    print("Client user created successfully!")
    return client_user

def admin_menu(users_data):
    while True:
        print("\nAdmin Menu:")
        print("1. Login")
        print("2. Sign Up")
        print("3. Back")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            role = authenticate_user(username, password)
            if role == 'admin':
                admin = Admin(users_data)
                admin.run_admin_panel()
        elif choice == '2':
            create_admin_user()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def client_menu(users_data):
    while True:
        print("\nClient Menu:")
        print("1. Login")
        print("2. Sign Up")
        print("3. Back")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            role = authenticate_user(username, password)
            
            if role == 'client':
                client = Client(users_data)
                client.run_client_panel()
        elif choice == '2':
            create_client_user()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    """Main menu to choose between Admin, Client, or Exit."""
    while True:
        print("\nWelcome to the Restaurant Management System")
        print("1. Admin")
        print("2. Client")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            users_data = load_users()
            if users_data is None:
                first_admin = create_admin_user()
                users_data = [first_admin]
            admin_menu(users_data)
        elif choice == '2':
            users_data = load_users()
            if users_data is not None:
                client_menu(users_data)
            else:
                print("No users found in the system.")
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
