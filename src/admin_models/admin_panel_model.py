class AdminPanelModel:
    def display_dashboard(self):
        print("\nAdmin dashboard")
        print("-" * 40)
        print("1. View Analytics")
        print("2. Menu Management")
        print("3. User Management")
        print("4. Order Management")
        print("5. Profile information")
        print("0. Log out")
        print("-" * 40)
    
    def menu_managment_dashboard(self):  
        print("\nMenu Managment Dashboard")
        print("-" * 40)      
        print("1. View menu")
        print("2. Add menu item")
        print("3. Update menu item")
        print("4. Delete menu item")
        print("0. Back to main")
        print("-" * 40)

    def user_managment_dashboard(self):
        print("\nUser Managment Dashboard")
        print("-" * 40)
        print("1. List of all Staff ")
        print("2. List of Admins")
        print("3. View Blocked Users")
        print("4. Block user")
        print("5. Unblock user")
        print("6. Create admin")
        print("7. Remove admin")
        print("8. User profile information")
        print("0. Back to main")
        print("-" * 40)

    def order_managment_dashboard(self):
        print("\nOrder Managment Dashboard")
        print("-" * 40)
        print("1. Totle Completed Orders") #which order by customers
        print("2. Totle Ongoing Orders") #which order by customers
        print("3. Order History") # summery of perticular order
        print("4. deliever order")
        print("5. Cancel Order")
        # print("3. Ongoing order")
        print("0. Back to main")
        print("-" * 40)