# users/admin.py
import json

from src.packages.menu_management.menu import Menu
from src.admin_models.user_managment import Users


class Admin:
    def __init__(self, user):
        self.user = user
        self.menu = Menu()
        self.users = Users()

    def run_admin_panel(self):
        print("Admin dashboard")
        print("-"*40)
        while True:
            
            print("1. View menu")
            print("2. Add menu item")
            print("3. Update menu item")
            print("4. View all customer")
            print("5. Customer information")
            print("6. Remove user")
            print("7. Order status")
            print("8. Payment history")
            print("9. Refund request")
            print("0. log out")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.menu.display_menu()
                input("Press 'Enter' to show the Dashboard")
            elif choice == '2':
                self.menu.add_menu_item()
                input("Press 'Enter' to show the Dashboard")
            elif choice == '3':
                self.menu.update_menu_item()
                input("Press 'Enter' to show the Dashboard")
            elif choice == '6':
                self.users.block_user()
                input("Press 'Enter' to show the Dashboard")

                pass
            elif choice == '0':
                print("Log out successfully \n ")
                break
            else:
                print("Invalid choice. Please try again.")
