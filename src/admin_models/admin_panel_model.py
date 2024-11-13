class AdminPanelModel:
    def display_dashboard(self):
        print("Admin dashboard")
        print("-" * 40)
        print("1. View menu")
        print("2. Add menu item")
        print("3. Update menu item")
        print("4. User Management")
        print("5. Order status")
        print("6. Profile information")
        print("0. Log out")
    
    def user_managment_dashboard(self):
        print("\n\n1. View all customer")
        print("2. Block user")
        print("3. Create admin")
        print("4. Remove admin")
        print("0. Back")