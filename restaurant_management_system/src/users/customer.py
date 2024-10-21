# from packages.menu_management.menu import Menu
# from packages.order_management.order import Order

# class Client:
#     def __init__(self, users_data):
#         self.users_data = users_data
#         self.menu = Menu()  # Initialize the Menu class to interact with menu items
#         self.order = Order()  # Initialize the Order class for placing orders

#     def run_client_panel(self):
#         """Client control panel with options to view the menu, place an order, or exit."""
#         print("Client Panel")
#         while True:
#             print("\n1. View menu")
#             print("2. Place order")
#             print("3. Add menu item")
#             print("4. Exit")
#             choice = input("Enter your choice: ")

#             if choice == '1':
#                 self.view_menu()
#             elif choice == '2':
#                 self.place_order()
#             elif choice == '3':
#                 self.add_menu_item()
#             elif choice == '4':
#                 print("Exiting client panel...")
#                 break
#             else:
#                 print("Invalid choice. Please try again.")

#     def view_menu(self):
#         """Display menu items using the Menu class from the menu management package."""
#         print("Displaying menu...")
#         if not self.menu.items:  # Check if there are any items in the menu
#             print("No items available in the menu.")
#         else:
#             self.menu.display_menu()  # Call the display_menu method from Menu class

#     def place_order(self):
#         """Place an order from available menu items using the Order class."""
#         if not self.menu.items:
#             print("No items available to order.")
#             return

#         print("Place an order:")
#         self.menu.display_menu()  # Show the menu to the client
#         item_name = input("Enter the name of the item you'd like to order: ")

#         # Check if the item exists in the menu
#         item_exists = any(item['name'] == item_name for item in self.menu.items)
#         if not item_exists:
#             print("Item not found in the menu.")
#             return

#         quantity = int(input("Enter the quantity: "))
#         self.order.add_order(item_name, quantity)  # Call the add_order method to place the order
#         print(f"Order placed for {quantity} x {item_name}.")

#     def add_menu_item(self):
#         """Method to add a new item to the menu."""
#         print("Add a new menu item:")
#         item_name = input("Enter the name of the item: ")
#         item_description = input("Enter the description of the item: ")
#         item_price = float(input("Enter the price of the item: "))
#         item_id = len(self.menu.items) + 1  # Generate a new ID based on the current number of items
#         item_available = True  # Default availability

#         new_item = {
#             "id": item_id,
#             "name": item_name,
#             "description": item_description,
#             "price": item_price,
#             "available": item_available
#         }

#         self.menu.add_item(new_item)  # Call the add_item method to add the new item
