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
            print("4. User Managment")
            print("5. Order status")
            print("6. Payment history")
            print("7. Refund request")
            print("8. Profile informaion")
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
            elif choice == '4':
                self.user_managment()
            elif choice == '5':
                pass
                
                input("Press 'Enter' to show the Dashboard")
            elif choice == '8':
                self.profile_info()
                input("Press 'Enter' to show the Dashboard")

                pass
            elif choice == '0':
                print("Log out successfully \n ")
                break
            else:
                print("Invalid choice. Please try again.")
    def profile_info(self):
        
        print(f"{'\nUser_id:':<10} {self.user['id']}")
        print(f"{'Username:':<10} {self.user['username']}")
        print(f"{'Email:':<10} {self.user['user_email']}")
        print(f"{'Mobile:':<10} {self.user['mobile']}")
        print(f"{'Role:':<10} {self.user['role']}")
        print(f"{'Joining_date:':<10} {self.user['joining_date']}")

    def user_managment(self):
        while True:
            print("\n\n1. View all customer")
            print("2. Customer information")
            print("3. Remove user")
            print("4. Create admin")
            print("0. Back")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.users.view_all_customer()
            elif choice == '2':
                self.users.customer_info()
            elif choice == '3':
                self.users.block_user()
            elif choice == '4':
                self.users.create_admin()
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")
