

from src.packages.menu_management.menu import Menu
from src.admin_models.user_managment import Users
from src.admin_models.order_managment import Orders
from src.admin_models.admin_panel_model import AdminPanelModel

# function(module)
from src.admin_models.order_traker import analytical


class Admin:
    def __init__(self, user):
        self.user = user #one admin person
        self.menu = Menu() # class object 
        self.users = Users()
        self.orders = Orders()
        self.panel = AdminPanelModel()

    def run_admin_panel(self):
        while True:
            self.panel.display_dashboard()
            choice = input("Enter your choice: ")
            if choice == '1':
                analytical()
                input("Press 'Enter' to show the Dashboard")
            elif choice == '2':
                self.menu_managment()
            elif choice == '3':
                self.user_managment()
            elif choice == '4':
                self.order_managment()
            elif choice == '5':
                self.profile_info()
                input("Press 'Enter' to show the Dashboard")
            elif choice == '0':
                confirm = input("Are you sure you want to log out? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    print("Logged out successfully.\n")
                    break
                else:
                    print("Logout canceled. Returning to the dashboard.")
                    continue
            else:
                print("Invalid choice. Please try again.")


  

    def menu_managment(self):
        while True:
            self.panel.menu_managment_dashboard()
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
                self.menu.delete_menu_item()
                input("Press 'Enter' to show the Dashboard")

            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again")

    def user_managment(self):
        while True:
            
            self.panel.user_managment_dashboard()

            choice = input("Enter your choice: ")
            if choice == '1':
                self.users.view_all_users()
                input("Press 'Enter' to show the Dashboard")

            elif choice == '2':
                self.users.view_all_admins()
                input("Press 'Enter' to show the Dashboard")

            elif choice == '3':
                self.users.view_block_users()
                input("Press 'Enter' to show the Dashboard")

            elif choice == '4':
                self.users.block_user()
                input("Press 'Enter' to show the Dashboard")

            elif choice == '5':
                self.users.unblock_user()
                input("Press 'Enter' to show the Dashboard")

            elif choice == '6':
                self.users.promote_user_to_admin()
                input("Press 'Enter' to show the Dashboard")

            elif choice == '7':
                self.users.remove_user_from_admin()
                input("Press 'Enter' to show the Dashboard")

            elif choice == '8':
                self.users.view_user_profile()
                input("Press 'Enter' to show the Dashboard")

            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")

    def order_managment(self):
        while True:
            self.panel.order_managment_dashboard()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.orders.totle_completed_order()
                input("Press 'Enter' to show the Dashboard")

            elif choice == '2':
                self.orders.totle_Ongoing_order()
                input("Press 'Enter' to show the Dashboard")

            elif choice == '3':
                self.orders.display_order_details()
                input("Press 'Enter' to show the Dashboard")

            elif choice == '4':
                self.orders.deliver_order()
                input("Press 'Enter' to show the Dashboard")

            elif choice == '5':
                self.orders.cancel_order()
                input("Press 'Enter' to show the Dashboard")

            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again")

        
    def profile_info(self):
        
        print(f"{'\nUser_id:':<10} {self.user['id']}")
        print(f"{'Username:':<10} {self.user['username']}")
        print(f"{'Email:':<10} {self.user['user_email']}")
        print(f"{'Mobile:':<10} {self.user['mobile']}")
        print(f"{'Role:':<10} {self.user['role']}")
        print(f"{'Joining_date:':<10} {self.user['joining_date']}")