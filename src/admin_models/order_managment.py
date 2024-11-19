import os,json

from src.models.json_files_path import get_all_invoices
from src.models.json_files_path import load_tracker
from src.models.json_files_path import tracker_update

class Orders:
    def __init__(self):
        self.orders = get_all_invoices()


    def cancel_order(self):
        try:
            # Ensure orders are loaded
            if not self.orders:
                print("No orders available to cancel.")
                return

            # Display all orders for admin to choose from
            print("\n--- All Orders ---")
            for order in self.orders:
                print(f"Order ID: {order['order_id']} | Customer: {order['customer_details']['name']} | Status: {order['status']}")

            # Prompt admin for order ID to cancel
            order_id = input("\nEnter the Order ID to cancel: ").strip()

            # Find the order
            order_to_cancel = next((order for order in self.orders if order['order_id'] == order_id), None)

            if not order_to_cancel:
                print(f"No order found with ID: {order_id}")
                return

            # Check if the order is already canceled
            if order_to_cancel['status'] == 'Canceled/Refunded':
                print(f"Order {order_id} is already canceled by {order_to_cancel['order_cancel_by']}")
                return
            if order_to_cancel['status'] == 'delivered':
                print(f"Error: Order {order_id} has delivered and cannot be canceled.")
                return

            # Display predefined cancellation reasons
            predefined_reasons = [
                "Customer request",
                "Item out of stock",
                "Payment issue",
                "Other"
            ]
            print("\n--- Cancellation Reasons ---")
            for idx, reason in enumerate(predefined_reasons, start=1):
                print(f"{idx}. {reason}")

            # Prompt for reason
            reason_choice = int(input("Select a reason for cancellation (1-4): "))
            if reason_choice < 1 or reason_choice > 4:
                print("Invalid choice. Cancellation aborted.")
                return

            cancellation_reason = predefined_reasons[reason_choice - 1]

            # Update the order status and reason
            order_to_cancel['status'] = 'Canceled/Refunded'
            order_to_cancel['order_cancel_by'] = 'admin'
            order_to_cancel['cancellation_reason'] = cancellation_reason

            user_directory = f"{order['customer_details']['name']}_{order['customer_details']['customer_id']}"
            directory = f'src/data_base/customers/{user_directory}/'  # Path to the directory where invoice files are stored

            with open(os.path.join(directory, f"invoice_{order_id}.json"), 'w') as file:
                json.dump(order_to_cancel, file, indent=4)

            # update analysis file
            data = load_tracker()
            data[0]["total_refunds"] += order_to_cancel['grand_total']
            data[0]["order_status"]["canceled/refunded"] += 1
            data[0]["order_status"]["Order Placed"] -= 1
            tracker_update(data)

            print(f"Order {order_id} has been successfully canceled.")

        except ValueError:
            print("Invalid input. Please try again.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


    def totle_Ongoing_order(self):
        found = False
        for order in self.orders:
            if order['status']=='Order Placed':
                found = True
                break
        if found:
            print(f"\n{'Order ID':<20}{'Ordered By':<25}{'Order date':<15}{'Payment method':<20}{'Status'}")            
            for order in self.orders:
                if order['status']=='Order Placed':
                    print(f"{order['order_id']:<20}{order['customer_details']['email']:<25}{order['date']:<15}{order['payment_method']:<20}{order['status']}")
        else:
            print("No orders placed yet!")

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

                            # update analysis file
                            data = load_tracker()
                            data[0]["order_status"]["completed"] += 1
                            data[0]["order_status"]["Order Placed"] -= 1
                            tracker_update(data)

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