import os,json

from src.models.json_files_path import get_all_invoices
class Orders:
    def __init__(self):
        self.orders = get_all_invoices()

    def totle_completed_order(self):
        found = False
        for order in self.orders:
            if order['status']=='delivered':
                found = True
                break
        if found:
            print(f"\n{'Order ID':<20}{'Ordered By':<25}{'Order date':<15}{'Payment method':<20}{'Status'}")            
            for order in self.orders:
                if order['status']=='delivered':
                    print(f"{order['order_id']:<20}{order['customer_details']['email']:<25}{order['date']:<15}{order['payment_method']:<20}{order['status']}")
        else:
            print("No orders delievered yet!")
    def deliver_order(self):
        
        
        while True:
            # Ask for order ID
            order_id = input("Enter the Order ID to mark as delivered (press 0 to exit): ").strip()
            
            if order_id == '0':
                print("Exiting delivery process.")
                break

            # Search for the order in the system
            order_found = False
            for order in self.orders:  # Assuming self.orders contains all the orders
                if order['order_id'] == order_id:
                    order_found = True
                    
                    if order['status'] == "Order Placed":
                        confirm = input("Are you sure to delivered this order(yes/no): ").strip().lower()
                        if confirm == 'yes':
                            order['status'] = "delivered"
                            user_directory = f"{order['customer_details']['name']}_{order['customer_details']['customer_id']}"
                            directory = f'src/data_base/customers/{user_directory}/'  # Path to the directory where invoice files are stored

                            # Write the updated invoice back to the file
                            with open(os.path.join(directory, f"invoice_{order['order_id']}.json"), 'w') as file:
                                json.dump(order, file, indent=4)

                            print(f"Order ID '{order_id}' has been successfully marked as delivered.")
                        else:
                            print('Your process canceled! ')
                    elif order['status'] == "Canceled/Refunded":
                        print(f"Error: Order ID '{order_id}' has been canceled and cannot be delivered.")
                    elif order['status'] == "delivered":


                        print(f"Order ID '{order_id}' is already marked as delivered.")
                    else:
                        print(f"Order ID '{order_id}' is in an invalid state.")
                    break

            if not order_found:
                print(f"Order ID '{order_id}' not found. Please try again.")
            
    

    def display_order_details(self):
        while True:
            order_id = input("Enter the order ID to view details (press 0 to exit): ").strip()

            if order_id == "0":
                print("Exiting...")
                break

            if not order_id:
                print("Order ID cannot be empty. Please try again.")
                continue

            order = next((invoice for invoice in self.orders if invoice["order_id"] == order_id), None)

            if order:
                print("\nOrder Details:")
                print(f"Order ID: {order['order_id']}")
                print(f"Status: {order['status']}")
                print(f"Order Date: {order['date']}")
                print(f"Order Time: {order['time']}")
                print(f"Total Payment (including GST): {order['grand_total']} {order['payment_method']}")

                # Customer details
                customer = order["customer_details"]
                print("\nCustomer Details:")
                print(f"Customer ID: {customer['customer_id']}")
                print(f"Name: {customer['name']}")
                print(f"Email: {customer['email']}")
                print(f"Role: {customer['role']}")
                break
            else:
                print("Order ID not found. Please try again or press 0 to exit.")