
from src.packages.menu_management.menu import Menu
from src.packages.order_management.order import Order

class Customer:
    def __init__(self, user):
        self.user = user
        self.menu = Menu()     # Initialize the Menu class for display menu item, only owner can add and update menu item 
        self.order = Order(user)  # Initialize the Order class for take, update, cancel orders

    def run_customer_panel(self):
        """customer control panel with options to view the menu, place an order, or exit."""
        print(f"\n******** Welcome {self.user["name"]}! ********")
        while True:
            enter_key = input("Press 'Enter' to show the Dashboard")
            if enter_key == "":
                print("\n1. View menu")
                print("2. Take new order")
                print("3. View ongoing order")
                print("4. Cancel order")
                print("5. Payment history")
                print("6. Order status")
                print("7. View invoice")
                print("8 View reserved tables")
                print("9. Profile Information")
                print("0. Log out")
                choice = input("Enter your choice: ")
                if choice == '1':
                    self.menu.display_menu()
                elif choice == '2':
                    self.order.take_order()
                elif choice == '3':
                    self.order.view_ongoing_order()
                elif choice == '4':
                    self.order.cancel_order()
                elif choice == '5':
                    self.order.payment_history()
                elif choice == '6':
                    print("ongoing..")
                elif choice == '7':
                    self.order.find_invoice()
                elif choice == '8':
                    print("ongoing..")                   
                elif choice == '9':
                    self.profile_info()
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
    
    