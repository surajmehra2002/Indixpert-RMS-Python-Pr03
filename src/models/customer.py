
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
    
    def place_order(self):
        """Place an order from available menu items using the Order class."""
        if not self.menu.items:
            print("No items available to order.")
            return

        print("Place an order:")
        self.menu.display_menu()  # Show the menu to the customer
        item_name = input("Enter the name of the item you'd like to order: ")

        # Check if the item exists in the menu
        item_exists = any(item['name'] == item_name for item in self.menu.items)
        if not item_exists:
            print("Item not found in the menu.")
            return

        quantity = int(input("Enter the quantity: "))
        self.order.add_order(item_name, quantity)  # Call the add_order method to place the order
        print(f"Order placed for {quantity} x {item_name}.")

    # def add_menu_item(self):
    #     """Method to add a new item to the menu."""
    #     print("Add a new menu item:")
    #     item_name = input("Enter the name of the item: ")
    #     item_description = input("Enter the description of the item: ")
    #     item_price = float(input("Enter the price of the item: "))
    #     item_id = len(self.menu.items) + 1  # Generate a new ID based on the current number of items
    #     item_available = True  # Default availability

    #     new_item = {
    #         "id": item_id,
    #         "name": item_name,
    #         "description": item_description,
    #         "price": item_price,
    #         "available": item_available
    #     }

    #     self.menu.add_item(new_item)  # Call the add_item method to add the new item
# customer = Customer()
# customer.run_customer_panel()