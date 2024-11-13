import json
import os
import random
from datetime import datetime
from tabulate import tabulate # type: ignore

from src.models.json_files_path import load_menu
from src.models.animation import loading
from src.models.json_files_path import load_all_invoices_of_an_user




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
        methods = ['Card', 'Net Banking', 'UPI', 'Cash']
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
            while True:
                confirm = input(f"Is this the item '{selected_item['name']}' you'd like to order? (y/n): ").strip().lower()
                if confirm == 'y' or confirm == 'n':
                    break
                else:
                    print('Invalid input! ')
            if confirm != 'y':
                continue

            # Check if the item has a half price; if not, skip order type selection
            if 'half_price' in selected_item:
                def order_type():
                    while True:
                        order_type_choice = input("\n1: half \n2: full \nEnter order type: ")
                        if order_type_choice == "1":
                            return "half"
                        elif order_type_choice == "2":
                            return "full"
                        else:
                            print("Invalid choice. Order canceled.")
                order_size = order_type()
            else:
                order_size = "full"

            quantity = int(input("Enter quantity: "))

            # Determine the base price based on order type
            def base_price():
                if order_size == 'half' and 'half_price' in selected_item:
                    return selected_item['half_price']
                else:
                    return selected_item['price']
            
            total_price = base_price() * quantity

            item_entry = {
                
                "name": selected_item['name'],
                "quantity": quantity,
                "price_per_unit": base_price(),
                "total_price": int(total_price)
            }
            if 'half_price' in selected_item and order_size == 'half':
                item_entry["type"] = "half"

            items.append(item_entry)

            add_more = input("Would you like to order another item? (y/n): ").strip().lower()

        if items:  # Ensure there are items to process
            sub_total = sum(item['total_price'] for item in items)
            gst_amount = (sub_total * self.gst_rate)
            grand_total = sub_total + int(gst_amount)

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
        invoices_list = load_all_invoices_of_an_user(directory)
        
        if len(invoices_list)!=0:
            print(f"{'Order ID':<40}{'Name':<35} {'Quantity':<10} {'Type':<20} {'Status':<20} {'Payment'}")
            print('-'*135)
            for invoice in invoices_list:
                for item in invoice['items']:
                    item_type = item.get('type', '-')
                    print(f"{invoice['order_id']:<40} {item['name']:<35} {item['quantity']:<10} {item_type:<20} {invoice['status']:<20} {invoice['payment_method']}")

        else:
            print("No order placed yet!")
    def take_order_id(self,invoices_list):
        while True:
            order_id = input("Enter the order ID you want to cancel (quit for 0): ").strip()
            order_id_list = [invoice['order_id'] for invoice in invoices_list]
            if order_id == '0' or order_id in order_id_list:
                break
        return order_id

    def cancel_order(self):
        user_directory = f"{self.user['username']}_{self.user['id']}"
        directory = f'src/data_base/customers/{user_directory}/'  # Path to the directory where invoice files are stored
        invoices_list = load_all_invoices_of_an_user(directory)
        
        # while True
        order_id = self.take_order_id(invoices_list)
        if order_id != '0':
            order_found = False
            
            for invoice in invoices_list:
                if invoice['order_id'] == order_id:
                    order_found = True
                    if invoice['status']!='Canceled':
                        while True:
                            print("Why do you want to cancel this order?")
                            print("0. Go back to main menu")
                            print("1. Ordered by mistake")
                            print("2. Found a better deal elsewhere")
                            print("3. Long delivery time")
                            print("4. Other")
                            
                            reason_choice = input("Enter the number corresponding to your reason: ").strip()
                            
                            if reason_choice == "0":
                                print("Returning to main menu without canceling the order.",end='')
                                loading()
                                print('\n')
                                return  # Exit the function without canceling
                            
                            reasons = {
                                "1": "Ordered by mistake",
                                "2": "Found a better deal elsewhere",
                                "3": "Long delivery time",
                                "4": "Other"
                            }
                            
                            cancellation_reason = reasons.get(reason_choice)
                            
                            if cancellation_reason:
                                # Update the status to "Canceled" and add the reason
                                invoice['status'] = 'Canceled'
                                invoice['cancellation_reason'] = cancellation_reason
                                
                                # Write the updated invoice back to the file
                                with open(os.path.join(directory, f"invoice_{order_id}.json"), 'w') as file:
                                    json.dump(invoice, file, indent=4)
                                
                                print(f"Order {order_id} has been canceled for the following reason: {cancellation_reason}")
                                break
                            else:
                                print("Invalid input. Please enter a valid option.")
                    else:
                        print("This order already canceled")    

            if not order_found:
                print("Order ID not found.")

    def payment_history(self):
        user_directory = f"{self.user['username']}_{self.user['id']}"
        directory = f'src/data_base/customers/{user_directory}/'  # Path to the directory where invoice files are stored
        invoices_list = load_all_invoices_of_an_user(directory)
        
        if len(invoices_list)!=0:
            print(f"{"Payment Mode":<20} {"Order ID":<40} {"Date & Time":<25} {"Totle Payment"}")
            print("-"*110)
            for invoice in invoices_list:
                print(f"{invoice['payment_method']:<20} {invoice['order_id']:<40} {invoice['date']}, {invoice['time']:<25} {invoice['grand_total']}")
        else:
            print("No payment yet!")  


    def generate_invoice(self,order_data):
        # Extracting customer and order details
        order_id = order_data.get("order_id")
        date = order_data.get("date")
        time = order_data.get("time")
        customer_name = order_data["customer_details"].get("name")
        customer_email = order_data["customer_details"].get("email")
        payment_method = order_data.get("payment_method")
        status = order_data.get("status")
        
        # Extracting items details
        items = order_data.get("items", [])
        
        # Creating item table
        item_table = []
        for item in items:
            item_name = item.get("name")
            quantity = item.get("quantity")
            price_per_unit = item.get("price_per_unit")
            total_price = item.get("total_price")
            item_table.append([item_name, quantity, f"₹{price_per_unit:.2f}", f"₹{total_price:.2f}"])

        sub_total = order_data.get("sub_total")
        gst_amount = order_data.get("gst_amount")
        grand_total = order_data.get("grand_total")

        print("\n" + "="*50)
        print(f"{'INVOICE':^50}")
        print("="*50)
        print(f"Order ID: {order_id}")
        print(f"Date: {date} | Time: {time}")
        print(f"Customer: {customer_name} ({customer_email})")
        print(f"Payment Method: {payment_method}")
        print(f"Status: {status}")
        print("="*50)
        
        print(tabulate(item_table, headers=["Item Name", "Quantity", "Price per Unit", "Total Price"], tablefmt="fancy_grid"))
        
        print("="*50)
        print(f"{'Subtotal:':<30} ₹{sub_total:.2f}")
        print(f"{'GST (18%):':<30} ₹{gst_amount:.2f}")
        print(f"{'Grand Total:':<30} ₹{grand_total:.2f}")
        print("="*50)

    



    def find_invoice(self):
        user_directory = f"{self.user['username']}_{self.user['id']}"
        directory = f'src/data_base/customers/{user_directory}/'  # Path to the directory where invoice files are stored
        invoices_list = load_all_invoices_of_an_user(directory)
        order_ID = input("enter order id for want view invoice: ")
        order_found = False
        for invoice in invoices_list:
            if invoice['order_id']==order_ID:
                order_found = True
                self.generate_invoice(invoice)
        if not order_found:
            print("ERROR: Invalid order id! ")
                

