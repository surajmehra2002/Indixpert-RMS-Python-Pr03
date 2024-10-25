# users/admin.py
import json

class Admin:
    def __init__(self, users_data):
        self.users_data = users_data

    def run_admin_panel(self):
        print("Admin Panel")
        while True:
            print("\n1. Create new client")
            print("2. View users")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_client_user()
            elif choice == '2':
                self.view_users()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    def create_client_user(self):
        """Create a new client user and save to users.json."""
        username = input("Enter client username: ")
        password = input("Enter client password: ")

        new_client = {
            "username": username,
            "password": password,
            "role": "client"
        }

        self.save_user(new_client)
        print(f"Client {username} created successfully!")

    def save_user(self, user_data):
        """Save the new user to users.json."""
        file_path = 'data/users.json'
        with open(file_path, 'r+') as f:
            users = json.load(f)
            users.append(user_data)
            f.seek(0)
            json.dump(users, f, indent=4)

    def view_users(self):
        """Display all users in the system."""
        print("Users in the system:")
        for user in self.users_data:
            print(f"Username: {user['username']}, Role: {user['role']}")
