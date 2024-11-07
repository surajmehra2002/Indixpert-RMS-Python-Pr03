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

    def payment_method(self):
        methods = ['Card', 'Net Banking', 'UPI']
        print("Choose your payment method:")
        for index, method in enumerate(methods, start=1):
            print(f"{index}. {method}")

        while True:
            choice = input("Enter the number of your choice: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(methods):
                return methods[int(choice) - 1]
            else:
                print("Invalid choice. Please select a valid payment method.")

    def take_order(self):
        current_hour = datetime.now().hour

        if current_hour < 8 or current_hour >= 18:
            print("Closed: Orders can only be placed between 8 AM and 6 PM.")
            return

        items = []
        add_more = 'y'

        while add_more.lower() == 'y':
            order_name = input("Search item for order: ").strip().lower()
            ordered_items = [item for item in self.menu if order_name in item['name'].lower()]

            if not ordered_items:
                print("Item not available. Please select an item from the available menu.\n")
                break

            print("Searching...", end="")
            loading()
            print("\n\nAvailable items: ")
            print('-' * 65)
            print(f"{'Index':<10} {'Name':<35} {'Half':<10}  {'Full'}")
            print('-' * 65)

            for index, item in enumerate(ordered_items, start=1):
                half_price = f"₹{item['half_price']}" if 'half_price' in item else ''
                print(f"{index:<10} {item['name']:<35} {half_price:<10} ₹{item['price']}")

            if len(ordered_items) > 1:
                try:
                    chosen_index = int(input("\nMultiple items found. Enter the index number of the item you want: ")) - 1
                    if chosen_index < 0 or chosen_index >= len(ordered_items):
                        print("Invalid index. Please try again.") 
                        continue
                    selected_item = ordered_items[chosen_index]
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue
            else:
                selected_item = ordered_items[0]

            if not selected_item['availability']:
                print("Sorry, this item is currently unavailable.")
                continue
            
            confirm = input(f"Is this the item '{selected_item['name']}' you'd like to order? (y/n): ").strip().lower()
            if confirm != 'y':
                continue
            def order_type():
                while True:
                    
                    order_type_choice = input("\n1: half \n2: full \nEnter order type: ")

                    if order_type_choice == "1":
                        order_type = "half"
                        break
                    elif order_type_choice == "2":
                        order_type = "full"
                        break
                    else:
                        print("Invalid choice. Order canceled.")
                        
                return order_type
           
            order_size = order_type()
            quantity = int(input("Enter quantity: "))
            def base_price():
                if order_size == 'half':
                    return selected_item['half_price']
                else:
                    return selected_item['price']
            total_price = base_price() * quantity

            items.append({
                "item_id": selected_item["item_id"],
                "name": selected_item['name'],
                "quantity": quantity,
                "type": order_size,
                "price_per_unit": base_price(),
                "total_price": int(total_price)
            })

            add_more = input("Would you like to order another item? (y/n): ").strip().lower()

        if items:  # Ensure there are items to process
            sub_total = sum(item['total_price'] for item in items)
            gst_amount = (sub_total * self.gst_rate)
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
                    "gst_amount": gst_amount,
                    "grand_total": grand_total,
                    "status": "Order Placed",
                    "payment_method": self.payment_method() 
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

  


    def view_ongoing_order(self):
        user_directory = f"{self.user['username']}_{self.user['id']}"
        directory = f'src/data_base/customers/{user_directory}/'  # Path to the directory where invoice files are stored
        # order_found = False 
        
        user_all_order_invoice_list = []
        try:
            for filename in os.listdir(directory):
                if filename.endswith(".json"):
                    with open(os.path.join(directory, filename)) as file:
                        orders = json.load(file)
                        user_all_order_invoice_list.append(orders)
                        # order_found = True
            print(f"{'Name':<35} {'Quantity':<10} {'Type':<20} {'Status':<20} {'Payment'}")
            print('-'*65)
            for invoice in user_all_order_invoice_list:
                for item in invoice['items']:
                    print(f"{item['name']:<35} {item['quantity']:<10} {item['type']:<20} {invoice['status']:<20} {invoice['payment_method']}")
                
        except FileNotFoundError:
            print("No order placed yet!")

        # if not order_found:
        #     print("Order not found or not in ongoing status.")

