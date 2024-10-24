import json
import os
import random
from datetime import datetime

class Order:
    def __init__(self, user):
        self.user = user
        self.orders = []  # List to store all orders
        self.gst_rate = 0.18  # 18% GST


    def calculate_price_with_gst(self, price):
        return price + (price * self.gst_rate)

    def generate_invoice_id(self):
        random_number = random.randint(1000, 9999)
        return "INV"+str(random_number) 

    def take_order(self):
        order_name = input("Enter order name: ")
        quantity = int(input("Enter quantity: "))

        base_price = 100  # Example base price for each order
        total_price = base_price * quantity
        total_price_with_gst = self.calculate_price_with_gst(total_price)

        print(f"The total price including GST is: ₹{total_price_with_gst:.2f}")

        confirmation = input("Are you sure you want to take the order? (Y/N): ")

        if confirmation.upper() == 'Y':
            # Step 4: Generate the invoice and save it to a JSON file
            invoice_id = self.generate_invoice_id()
            date_now = datetime.now().strftime('%Y-%m-%d')
            time_now = datetime.now().strftime('%H:%M')
            customer_details = {
                "customer_id": self.user["id"],
                "name": self.user['username'],
                "email": self.user['user_email'],
                "role": self.user["role"]
            }

            # Creating order item details
            items = [
                {
                    "item_id": "ITEM001",
                    "name": order_name,
                    "quantity": quantity,
                    "price_per_unit": base_price,
                    "total_price": total_price
                }
            ]

            sub_total = total_price
            gst_percentage = 5  # Example GST percentage
            gst_amount = (sub_total * gst_percentage) / 100
            grand_total = sub_total + gst_amount

            invoice_data = {
                "invoice_id": invoice_id,
                "date": date_now,
                "time": time_now,
                "customer_details": customer_details,
                "items": items,
                "sub_total": sub_total,
                "gst_percentage": gst_percentage,
                "gst_amount": gst_amount,
                "grand_total": grand_total,
                "status": "Paid"
            }

            folder_name = f"{self.user['username']}_{self.user['id']}"
            file_path = f"S:/indixpert_coaching/python/python_project/Indixpert-RMS-Python-Pr03/src/data/customers/{folder_name}/invoice_{invoice_id}.json"

            os.makedirs(os.path.dirname(file_path), exist_ok=True)

         
            with open(file_path, 'w') as invoice_file:
                json.dump(invoice_data, invoice_file, indent=4)

            print(f"SMS: You have paid ₹{grand_total:.2f} including GST.")
            print("Order placed successfully!")
        else:
            print("Order cancelled.")
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
#     order_manager = Order({
#         "id": "6d30803b",
#         "username": "suraj",
#         "user_email": "suraj@gmail.com",
#         "password": "suraj",
#         "role": "customer"
#     })
#     order_manager.take_order()
    
#     # Sample order placement
#     order_manager.add_order("Pizza", 2)
#     order_manager.add_order("Burger", 1)
    
#     # Display all orders
#     order_manager.display_orders()
