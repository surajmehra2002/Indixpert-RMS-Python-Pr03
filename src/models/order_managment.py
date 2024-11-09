import os
import json

from src.models.json_files_path import load_all_invoices_of_an_user

class OrderManager:
    def __init__(self, user):
        self.user = user
        self.user_directory = f"{self.user['username']}_{self.user['id']}"
        self.directory = f'src/data_base/customers/{self.user_directory}/'
        
    def view_invoices(self):
        invoices_list = []
        try:
            for filename in os.listdir(self.directory):
                if filename.endswith(".json"):
                    with open(os.path.join(self.directory, filename)) as file:
                        invoice = json.load(file)
                        invoices_list.append(invoice)
            return invoices_list
        except FileNotFoundError:
            print("No invoices found.")
            return []

    def cancel_order(self):
        invoices_list = self.view_invoices()
        if not invoices_list:
            return
        
        order_id = input("Enter the order ID you want to cancel: ")
        order_found = False

        for invoice in invoices_list:
            if invoice['order_id'] == order_id:
                order_found = True
                print("Why do you want to cancel this order?")
                print("1. Ordered by mistake")
                print("2. Found a better deal elsewhere")
                print("3. Long delivery time")
                print("4. Other")
                
                reason_choice = input("Enter the number corresponding to your reason: ")
                reasons = {
                    "1": "Ordered by mistake",
                    "2": "Found a better deal elsewhere",
                    "3": "Long delivery time",
                    "4": "Other"
                }
                
                cancellation_reason = reasons.get(reason_choice, "Other")
                
                # Update the status to "Canceled" and add the reason
                invoice['status'] = 'Canceled'
                invoice['cancellation_reason'] = cancellation_reason
                
                # Write the updated invoice back to the file
                with open(os.path.join(self.directory, f"{order_id}.json"), 'w') as file:
                    json.dump(invoice, file, indent=4)
                
                print(f"Order {order_id} has been canceled for the following reason: {cancellation_reason}")
                break
        
        if not order_found:
            print("Order ID not found.")

# Example usage:
user_info = {'username': 'suraj', 'id': '2e38fdfc'}
manager = OrderManager(user_info)
manager.cancel_order()
