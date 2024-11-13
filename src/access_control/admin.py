

from src.packages.menu_management.menu import Menu
from src.admin_models.user_managment import Users
from src.admin_models.order_managment import Orders
from src.admin_models.admin_panel_model import AdminPanelModel


class Admin:
    def __init__(self, user):
        self.user = user
        self.menu = Menu()
        self.users = Users()
        self.orders = Orders()
        self.panel = AdminPanelModel()

    def run_admin_panel(self):
        while True:
            self.panel.display_dashboard()
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
                self.orders.display_order_details()
                
                input("Press 'Enter' to show the Dashboard")
            elif choice == '6':
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
            self.panel.user_managment_dashboard()

            choice = input("Enter your choice: ")
            if choice == '1':
                self.users.view_all_users()
            elif choice == '2':
                self.users.block_user()
            elif choice == '3':
                self.users.promote_user_to_admin()
            elif choice == '4':
                self.users.remove_user_from_admin()
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")
