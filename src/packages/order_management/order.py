import json
import os
import random
from datetime import datetime
from colorama import Fore, Style # type: ignore
from tabulate import tabulate # type: ignore

from src.models.json_files_path import load_menu
from src.models.animation import loading
from src.models.json_files_path import load_all_invoices_of_an_user
from src.models.json_files_path import load_tracker
from src.models.json_files_path import tracker_update




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

        while True:  # Use an infinite loop and control exiting explicitly
            if add_more.lower() == 'n':
                confirm_exit = input("Do you want to finish your order? (y/n): ").strip().lower()
                if confirm_exit == 'y':
                    break
                elif confirm_exit == 'n':
                    add_more = 'y'  # Reset add_more to continue ordering
                    continue
                else:
                    print(Fore.RED+"Invalid input. Please type 'y' or 'n'."+Style.RESET_ALL)
                    continue

            order_name = input("Search item for order (press 0 for exit): ").strip().lower()
            ordered_items = [item for item in self.menu if order_name in item['name'].lower()]

            if order_name == '0':
                break
            if not ordered_items:
                print(Fore.YELLOW+"Item not available. Please select an item from the available menu.\n"+Style.RESET_ALL)
                continue

            print("Searching...", end="")
            loading()
            print(Fore.GREEN+"\n\nAvailable items: "+Style.RESET_ALL)
            print(Fore.LIGHTYELLOW_EX+'-' * 65)
            print(f"{'Index':<10} {'Name':<35} {'Half':<10}  {'Full'}")
            print('-' * 65 + Style.RESET_ALL)

            for index, item in enumerate(ordered_items, start=1):
                half_price = f"₹{item['half_price']}" if 'half_price' in item else ''
                print(Fore.GREEN+ f"{index:<10} {item['name']:<35} {half_price:<10} ₹{item['price']}"+Style.RESET_ALL)

            if len(ordered_items) > 1:
                try:
                    chosen_index = int(input("\nMultiple items found. Enter the index number of the item you want: ")) - 1
                    if chosen_index < 0 or chosen_index >= len(ordered_items):
                        print(Fore.RED+ "Invalid index. Please try again."+ Style.RESET_ALL)
                        continue
                    selected_item = ordered_items[chosen_index]
                except ValueError:
                    print(Fore.RED+ "Invalid input. Please enter a number."+ Style.RESET_ALL)
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
                    print(Fore.RED+ 'Invalid input! ' + Style.RESET_ALL)
            if confirm != 'y':
                continue

            if 'half_price' in selected_item:
                def order_type():
                    while True:
                        order_type_choice = input("\n1: half \n2: full \nEnter order type: ")
                        if order_type_choice == "1":
                            return "half"
                        elif order_type_choice == "2":
                            return "full"
                        else:
                            print("Invalid choice !")
                order_size = order_type()
            else:
                order_size = "full"

            while True:
                try:
                    quantity = int(input("Enter quantity: "))
                    if quantity <= 0:
                        print(Fore.RED + "Quantity must be a positive number."+ Style.RESET_ALL)
                        continue
                    break
                except ValueError:
                    print(Fore.RED + "Invalid input! Please enter a numeric value." + Style.RESET_ALL)

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

            # Combine quantities and prices for the same item
            existing_item = next((item for item in items if item['name'] == selected_item['name']), None)
            if existing_item:
                existing_item['quantity'] += item_entry['quantity']
                existing_item['total_price'] += item_entry['total_price']
            else:
                items.append(item_entry)

            while True:
                add_more = input("Would you like to order another item? (y/n): ").strip().lower()
                if add_more == 'y' or add_more == 'n':
                    break  # Exit the loop if the input is either 'y' or 'n'
                else:
                    print(Fore.RED + "Invalid input! Please enter 'y' for yes or 'n' for no." + Style.RESET_ALL)

        if items:  # Ensure there are items to process
            sub_total = sum(item['total_price'] for item in items)
            gst_amount = (sub_total * self.gst_rate)
            grand_total = sub_total + int(gst_amount)

            print(f"The total price including GST is: {Fore.GREEN}₹{grand_total:.2f}{Style.RESET_ALL}")

            while True:
                confirmation = input("Are you sure you want to place the order? (Y/N): ")
                if confirmation.upper()=='Y' or confirmation.upper()=='N':
                    break
                
                else:
                    print(Fore.RED + 'Invalid input !' + Style.RESET_ALL)
                    

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
                    "payment_status" : "Debited",
                    "payment_method": self.payment_method()
                }

                folder_name = f"{self.user['username']}_{self.user['id']}"
                file_path = f"src/data_base/customers/{folder_name}/invoice_{order_id}.json"

                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, 'w') as invoice_file:
                    json.dump(invoice_data, invoice_file, indent=4)

                data = load_tracker()
                data[0]["total_revenue"] += invoice_data["grand_total"]
                data[0]["order_status"]["Order Placed"] += 1
                tracker_update(data)
                

                print(f"SMS: You have paid ₹{grand_total:.2f} including GST.")
                print(Fore.GREEN + "Congratulation! your order placed successfully" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Order cancelled." + Style.RESET_ALL)

  


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
                    if invoice['status']!='Canceled/Refunded':
                        if invoice['status']=='delivered':
                            print(f"Error: Order {order_id} has delivered and cannot be canceled.")
                            return
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
                                invoice['status'] = 'Canceled/Refunded'
                                invoice['payment_status'] = 'Credited'
                                invoice['order_cancel_by'] = 'staff'
                                invoice['canceled_date'] = datetime.now().strftime('%Y-%m-%d')
                                invoice['canceled_time'] = datetime.now().strftime('%H:%M')
                                invoice['cancellation_reason'] = cancellation_reason
                                
                                # Write the updated invoice back to the file
                                with open(os.path.join(directory, f"invoice_{order_id}.json"), 'w') as file:
                                    json.dump(invoice, file, indent=4)
                                
                                # update analysis file
                                data = load_tracker()
                                data[0]["total_refunds"] += invoice['grand_total']
                                data[0]["order_status"]["canceled/refunded"] += 1
                                data[0]["order_status"]["Order Placed"] -= 1
                                tracker_update(data)
                                
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
            print(Fore.GREEN + f"{"Payment Mode":<20} {"Payment Status":<40} {"Date & Time":<25} {"Totle Payment"}")
            print("-"*110 +Style.RESET_ALL)
            for invoice in invoices_list:
                print( Fore.LIGHTYELLOW_EX + f"{invoice['payment_method']:<20} {'Debited':<40} {invoice['date']}, {invoice['time']:<15} -{invoice['grand_total']}" + Style.RESET_ALL)
                if invoice['status'] == 'Canceled/Refunded':
                    print( Fore.LIGHTYELLOW_EX + f"{invoice['payment_method']:<20} {'Credited':<40} {invoice['canceled_date']}, {invoice['canceled_time']:<15} +{invoice['grand_total']}" + Style.RESET_ALL)

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
        print(f"Staff: {customer_name} ({customer_email})")
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
            print(Fore.RED + "ERROR: Invalid order id! " + Style.RESET_ALL)
                

