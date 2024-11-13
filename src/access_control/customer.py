
from src.packages.menu_management.menu import Menu
from src.packages.order_management.order import Order
from src.models.menus_model import MenuModel

class Customer:
    def __init__(self, user):
        self.user = user
        self.menu = Menu()     # Initialize the Menu class for display menu item, only owner can add and update menu item 
        self.order = Order(user)  # Initialize the Order class for take, update, cancel orders
        self.menu_panel = MenuModel()

    def run_customer_panel(self):
        """customer control panel with options to view the menu, place an order, or exit."""
        print(f"\n******** Welcome {self.user["name"]}! ********")
        
        while True:            
            self.menu_panel.customer_panel_model()

            choice = input("Enter your choice: ")
            if choice == '1':
                self.menu.display_menu()
                input("Press 'Enter' to show the Dashboard")
            elif choice == '2':
                self.order.take_order()
                input("Press 'Enter' to show the Dashboard")
                                
            elif choice == '3':
                self.order.view_ongoing_order()
                input("Press 'Enter' to show the Dashboard")
                                
            elif choice == '4':
                self.order.cancel_order()
                input("Press 'Enter' to show the Dashboard")
                                
            elif choice == '5':
                self.order.payment_history()
                input("Press 'Enter' to show the Dashboard")
                                
            elif choice == '6':
                print("ongoing..")
                input("Press 'Enter' to show the Dashboard")
                                
            elif choice == '7':
                self.order.find_invoice()
                input("Press 'Enter' to show the Dashboard")
                                
            elif choice == '8':
                print("ongoing..")      
                input("Press 'Enter' to show the Dashboard")
                                             
            elif choice == '9':
                self.profile_info()
                input("Press 'Enter' to show the Dashboard")
                                
            elif choice == '0':
                print("Log out Successfully!\n")
                break
            else:
                print('OPTION ERROR: Invalid option')

    def profile_info(self):
        
        print(f"{'\nUser_id:':<10} {self.user['id']}")
        print(f"{'Username:':<10} {self.user['username']}")
        print(f"{'Email:':<10} {self.user['user_email']}")
        print(f"{'Mobile:':<10} {self.user['mobile']}")
        print(f"{'Role:':<10} {self.user['role']}")
        print(f"{'Joining_date:':<10} {self.user['joining_date']}")
    
    