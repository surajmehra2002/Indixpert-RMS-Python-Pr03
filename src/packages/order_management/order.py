import json
import os
import random
from datetime import datetime

from src.models.json_files_path import load_menu
from src.models.animation import loading

class Order:
    def __init__(self, user):
        self.user = user
        self.orders = []
        self.menu = load_menu()
        self.gst_rate = 0.18

    def calculate_price_with_gst(self, price):
        return price + (price * self.gst_rate)

    def generate_invoice_id(self):
        return "401-" + str(random.randint(1000, 9999)) + "-" + str(random.randint(1000, 9999))

    def take_order(self):
        print("Available items:")
        for item in self.menu:
            print(f"{item['name']} - ₹{item['price']}")

        items = []
        add_more = 'y'

        while add_more.lower() == 'y':
            order_name = input("Enter the name of the item you'd like to order: ").strip().lower()
            ordered_item = [item for item in self.menu if order_name in item['name'].lower()]

            if not ordered_item:
                print("Item not available. Please select an item from the available menu.")
                continue

            print("Searching...", end="")
            loading()
            print("\nAvailable items: ")
            print(f"{'Name':<20} {'Price':<20}")
            for item in ordered_item:
                print(f"{item['name']:<20} {item['price']:<20}")

            if len(ordered_item) == 1:
                selected_item = ordered_item[0]
                if not selected_item['availability']:
                    print("Sorry, this item is currently unavailable.")
                    continue

                confirm = input("Is this the item you'd like to order? (y/n): ").strip().lower()
                if confirm != 'y':
                    continue
            else:
                print("Multiple items found. Choose one item")
                continue

            quantity = int(input("Enter quantity: "))
            base_price = selected_item['price']
            total_price = base_price * quantity

            items.append({
                "item_id": selected_item["item_id"],
                "name": selected_item['name'],
                "quantity": quantity,
                "price_per_unit": base_price,
                "total_price": int(total_price)
            })

            add_more = input("Would you like to order another item? (y/n): ").strip().lower()

        sub_total = sum(item['total_price'] for item in items)
        gst_percentage = 18
        gst_amount = (sub_total * gst_percentage) / 100
        grand_total = sub_total + gst_amount

        print(f"The total price including GST is: ₹{grand_total:.2f}")
        confirmation = input("Are you sure you want to place the order? (Y/N): ")

        if confirmation.upper() == 'Y':
            order_id = self.generate_invoice_id()
            date_now = datetime.now().strftime('%Y-%m-%d')
            time_now = datetime.now().strftime('%H:%M')
            customer_details = {
                "customer_id": self.user["id"],
                "name": self.user['username'],
                "email": self.user['user_email'],
                "role": self.user["role"]
            }

            invoice_data = {
                "order_id": order_id,
                "date": date_now,
                "time": time_now,
                "customer_details": customer_details,
                "items": items,
                "sub_total": sub_total,
                "gst_percentage": gst_percentage,
                "gst_amount": gst_amount,
                "grand_total": grand_total,
                "status": "Ordered"
            }

            folder_name = f"{self.user['username']}_{self.user['id']}"
            file_path = f"src/data_base/customers/{folder_name}/invoice_{order_id}.json"

            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as invoice_file:
                json.dump(invoice_data, invoice_file, indent=4)

            print(f"SMS: You have paid ₹{grand_total:.2f} including GST.")
            print("Order placed successfully!")
        else:
            print("Order cancelled.")
