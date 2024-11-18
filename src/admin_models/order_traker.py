
import json
def analytical():

    try:
        # Path to the status_count JSON file
        status_count_file = 'src/data_base/status_count.json'
        
        # Load status_count data
        with open(status_count_file, 'r') as file:
            data = json.load(file)

        # Extract details
        total_revenue = data.get('total_revenue', 0.00)
        total_refunds = data.get('total_refunds', 0.00)
        order_status = data.get('order_status', {})
        
        # Calculate total orders
        total_orders = sum(order_status.values())

        # Insights
        print("\n--- Business status_count ---")
        print(f"Total Revenue: ₹{total_revenue:,.2f}")
        print(f"Total Refunds: ₹{total_refunds:,.2f}")
        print(f"Total Orders: {total_orders}")
        print("\n--- Order Status Breakdown ---")
        for status, count in order_status.items():
            percentage = (count / total_orders) * 100 if total_orders > 0 else 0
            print(f"{status.capitalize()}: {count} orders ({percentage:.2f}%)")
        
        # Refund Analysis
        refund_percentage = (total_refunds / total_revenue) * 100 if total_revenue > 0 else 0
        print(f"\nRefund Percentage: {refund_percentage:.2f}%")
        
        # Order Completion Rate
        completed_orders = order_status.get("completed", 0)
        completion_rate = (completed_orders / total_orders) * 100 if total_orders > 0 else 0
        print(f"Order Completion Rate: {completion_rate:.2f}%")
        
        # Business Trend
        print("\n--- Business Trend ---")
        if refund_percentage < 5 and completion_rate > 90:
            print("Business is performing well with minimal refunds and high order completion.")
        elif refund_percentage > 10:
            print("Refund percentage is high. Consider reviewing your refund policy or product quality.")
        elif completion_rate < 70:
            print("Low order completion rate. Improve customer experience or address order fulfillment issues.")
        else:
            print("Business is stable but has room for improvement.")

    except FileNotFoundError:
        print("status_count data file not found. Please ensure the file exists at the specified location.")
    except Exception as e:
        print(f"An error occurred during analysis: {str(e)}")
