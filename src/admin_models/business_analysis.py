from colorama import Fore, Style # type: ignore
# module
from src.models.json_files_path import load_tracker
from src.models.json_files_path import get_all_invoices

class Analysis:
    def analytical(self):
        data_list = load_tracker()
        if not data_list:
            print("Tracking not available..")
            return
        data = data_list[0]

        try:
            # Extract details
            total_revenue = data.get('total_revenue', 0.00)
            total_refunds = data.get('total_refunds', 0.00)
            order_status = data.get('order_status', {})
            
            # Calculate total orders
            total_orders = sum(order_status.values())

            # Insights
            print(Fore.LIGHTGREEN_EX+"\nBusiness Analytics Report")
            print("-------------------------------------"+ Style.RESET_ALL)
            print(f"{'Total Revenue:':<20} ₹{total_revenue:,.2f}")
            print(f"{'Total Refunds:':<20} ₹{total_refunds:,.2f}")
            print(f"{'Total Orders:':<20} {total_orders}")
            print("\n--- Order Status Breakdown ---")
            for status, count in order_status.items():
                percentage = (count / total_orders) * 100 if total_orders > 0 else 0
                print(f"{status.capitalize()}: {count} orders ({percentage:.2f}%)")
            
            # Refund Analysis
            refund_percentage = (total_refunds / total_revenue) * 100 if total_revenue > 0 else 0
            print(f"\n{'Refund Percentage:':<20} {refund_percentage:.2f}%")
            
            # Order Completion Rate
            completed_orders = order_status.get("completed", 0)
            completion_rate = (completed_orders / total_orders) * 100 if total_orders > 0 else 0
            print(f"{'Order Completion Rate:':<20} {completion_rate:.2f}%")
            
            # Business Trend
            print("\n--- Business Trend ---")
            if refund_percentage < 5 and completion_rate > 90:
                print(Fore.GREEN+"Business is performing well with minimal refunds and high order completion."+ Style.RESET_ALL)
            elif refund_percentage > 10:
                print(Fore.LIGHTYELLOW_EX+"Refund percentage is high. Consider reviewing your refund policy or product quality."+ Style.RESET_ALL)
            elif completion_rate < 70:
                print("Low order completion rate. Improve customer experience or address order fulfillment issues.")
            else:
                print("Business is stable but has room for improvement.")
            print('--------------------------------------\n')

        except Exception as e:
            print(Fore.RED + f"An error occurred during analysis: {str(e)}" + Style.RESET_ALL)


    def filter_analysis(self):
        data = get_all_invoices()
        from datetime import datetime

  
        # Step 1: Ask the user for a start date
        input_date = input("Enter the start date (YYYY-MM-DD): ")
        try:
            start_date = datetime.strptime(input_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        
        # Step 2: Filter data from the entered date to the current date
        current_date = datetime.now()
        filtered_data = [
            order for order in data
            if datetime.strptime(order['date'], "%Y-%m-%d") >= start_date
        ]
        
        if not filtered_data:
            print("No orders found in the given date range.")
            return
        
        # Step 3: Initialize metrics
        total_revenue = 0
        total_delivered_orders = 0
        total_refund_amount = 0
        total_canceled_orders = 0
        total_items_sold = 0
        
        # Step 4: Analyze filtered data
        for order in filtered_data:
            if order['status'] == "delivered":
                total_revenue += order['grand_total']
                total_delivered_orders += 1
                for item in order['items']:
                    total_items_sold += item['quantity']
            elif order['status'] == "Canceled/Refunded":
                total_refund_amount += order['grand_total']
                total_canceled_orders += 1
        
        # Step 5: Display analysis
        print("\n--- Order Analysis ---")
        print(f"Total Revenue: ₹{total_revenue:.2f}")
        print(f"Total Delivered Orders: {total_delivered_orders}")
        print(f"Total Items Sold: {total_items_sold}")
        print(f"Total Refund Amount: ₹{total_refund_amount:.2f}")
        print(f"Total Canceled Orders: {total_canceled_orders}")
        print(f"Orders Analyzed: {len(filtered_data)}")

  