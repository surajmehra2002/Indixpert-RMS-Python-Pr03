from src.models.json_files_path import get_all_invoices
class Orders:
    def __init__(self):
        self.orders = get_all_invoices()
        pass
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