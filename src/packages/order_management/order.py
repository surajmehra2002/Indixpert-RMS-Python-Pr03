

class Order:
    def __init__(self, user):
        self.user = user
        self.orders = []  # List to store all orders

    def take_order(self):
        print('take order')
        print(self.user)
        # order = {
        #     "item_name": item_name,
        #     "quantity": quantity
        # }
        # self.orders.append(order)  # Append the new order to the orders list
    def update_order(self):
        print("update")

    def cancel_order():
        print("cancel")

    def display_orders(self):
        print("display")
        # """Display all orders placed."""
        # if not self.orders:
        #     print("No orders placed.")
        # else:
        #     print("Current Orders:")
        #     for index, order in enumerate(self.orders):
        #         print(f"{index + 1}. Item: {order['item_name']}, Quantity: {order['quantity']}")

# # Example usage
# if __name__ == "__main__":
#     order_manager = Order()
    
#     # Sample order placement
#     order_manager.add_order("Pizza", 2)
#     order_manager.add_order("Burger", 1)
    
#     # Display all orders
#     order_manager.display_orders()
