
from src.packages.menu_management.menu import Menu
# from packages.order_management.order import Order

class Customer:
    def __init__(self, user):
        self.user = user
        self.menu = Menu()
        # self.order = Order()  # Initialize the Order class for placing orders

    def run_customer_panel(self):
        """customer control panel with options to view the menu, place an order, or exit."""
        print(f"\nWelcome {self.user["username"]}!")
        while True:
            enter_key = input("Press 'Enter' to show the menu")
            if enter_key == "":
                print("\n1. View menu")
                print("2. Take order")
                print("3. Update ongoing order")
                print("4. Cancel")
                print("5. View ongoing order")
                print("6. Table booking")
                print("7. Profile Information")
                print("0. Log out")
                choice = input("Enter your choice: ")

                if choice == '1':
                    self.menu.display_menu()
                elif choice == '2':
                    # self.place_order()
                    pass
                elif choice == '3':
                    # self.add_menu_item()
                    pass
                elif choice == '7':
                    self.profile_info()
                elif choice == '0':
                    print("Log out Successfully!\n")
                    break
                else:
                    print("Invalid choice. Please try again.")
          

    def profile_info(self):
        
        print(f"{'Name:':<10} {self.user['username']}")
        print(f"{'Role:':<10} {self.user['role']}")
    # def view_menu(self):
    #     """Display menu items using the Menu class from the menu management package."""
    #     # print("Displaying menu...")
      
    #     if not self.menu.items:  # Check if there are any items in the menu
    #         print("No items available in the menu.")
    #     else:
    #         self.menu.display_menu()  # Call the display_menu method from Menu class

    # def place_order(self):
    #     """Place an order from available menu items using the Order class."""
    #     if not self.menu.items:
    #         print("No items available to order.")
    #         return

    #     print("Place an order:")
    #     self.menu.display_menu()  # Show the menu to the customer
    #     item_name = input("Enter the name of the item you'd like to order: ")

    #     # Check if the item exists in the menu
    #     item_exists = any(item['name'] == item_name for item in self.menu.items)
    #     if not item_exists:
    #         print("Item not found in the menu.")
    #         return

    #     quantity = int(input("Enter the quantity: "))
    #     self.order.add_order(item_name, quantity)  # Call the add_order method to place the order
    #     print(f"Order placed for {quantity} x {item_name}.")

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