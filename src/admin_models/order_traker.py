def track_total_order_info(self):
    orders = self.load_orders()  # Load orders from the database or JSON file
    total_orders = len(orders)
    status_count = {
        "Completed": 0,
        "Pending": 0,
        "Canceled": 0,
        "Refunded/Returned": 0
    }
    total_revenue = 0
    gst_collected = 0

    # Count orders by status and calculate totals
    for order in orders:
        status_count[order['status']] += 1
        if order['status'] in ['Completed', 'Delivered']:
            total_revenue += order['total']
            gst_collected += order.get('GST', 0)

    print("\nTotal Order Information")
    print("-" * 40)
    print(f"Total Orders: {total_orders}")
    print(f"Completed Orders: {status_count['Completed']}")
    print(f"Pending Orders: {status_count['Pending']}")
    print(f"Canceled Orders: {status_count['Canceled']}")
    print(f"Refunded/Returned Orders: {status_count['Refunded/Returned']}")
    print(f"Total Revenue: ₹{total_revenue}")
    print(f"GST Collected: ₹{gst_collected}")
    print("-" * 40)

def load_orders(self):
    import json
    with open("src/data_base/orders.json", "r") as file:
        return json.load(file)
