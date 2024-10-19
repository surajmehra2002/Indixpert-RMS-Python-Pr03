# class Order:
#     def __init__(self, order_id, table_id, items):
#         self.order_id = order_id
#         self.table_id = table_id
#         self.items = items
#         self.status = "ongoing"
    
#     def update_order(self, new_items):
#         self.items = new_items
#         print("Order updated successfully")
    
#     def cancel_order(self):
#         self.status = "cancelled"
#         print("Order cancelled")


# packages/order_management/order.py

class Order:
    def __init__(self):
        self.orders = []  # List to store all orders

    def add_order(self, item_name, quantity):
        """Add an order to the list."""
        order = {
            "item_name": item_name,
            "quantity": quantity
        }
        self.orders.append(order)  # Append the new order to the orders list

    def display_orders(self):
        """Display all orders placed."""
        if not self.orders:
            print("No orders placed.")
        else:
            print("Current Orders:")
            for index, order in enumerate(self.orders):
                print(f"{index + 1}. Item: {order['item_name']}, Quantity: {order['quantity']}")

# Example usage
if __name__ == "__main__":
    order_manager = Order()
    
    # Sample order placement
    order_manager.add_order("Pizza", 2)
    order_manager.add_order("Burger", 1)
    
    # Display all orders
    order_manager.display_orders()
