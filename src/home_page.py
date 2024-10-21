# import json
# import os
from users.authentication import authenticate_user
# from users.authentication import authenticate_user
# from users.owner import owner
# from users.customer import customer

# def load_users():
#     """Load users from the JSON file or initialize if the file doesn't exist or is empty."""
#     file_path = r'data/users.json'
    
#     # Check if the file exists
#     if not os.path.exists(file_path):
#         print("Users file not found, creating a new one.")
#         with open(file_path, 'w') as f:
#             json.dump([], f)  # Initialize with an empty list
    
#     # Load users from the file
#     with open(file_path, 'r') as f:
#         try:
#             users = json.load(f)
#             if not users:  # If the file is empty
#                 print("No users found in the system. Please create an owner user.")
#                 return None
#             return users
#         except json.JSONDecodeError:
#             print("Error decoding users.json. Please ensure it's a valid JSON file.")
#             return None

# def save_user(user_data):
#     """Save the new user to users.json."""
#     file_path = 'data/users.json'
    
#     # Check if the file is empty or contains invalid data
#     if os.path.getsize(file_path) == 0:
#         users = []  # If the file is empty, initialize an empty list
#     else:
#         with open(file_path, 'r+') as f:
#             try:
#                 users = json.load(f)
#             except json.JSONDecodeError:
#                 print("Error reading users.json. Initializing with an empty list.")
#                 users = []
    
#     # Append the new user data to the list
#     users.append(user_data)
    
#     # Save the updated list of users back to the file
#     with open(file_path, 'w') as f:
#         json.dump(users, f, indent=4)


# def create_owner_user():
#     """Create the first owner user if no users exist."""
#     print("Creating a new owner user.")
#     username = input("Enter owner username: ")
#     password = input("Enter owner password: ")
    
#     owner_user = {
#         "username": username,
#         "password": password,
#         "role": "owner"
#     }
    
#     save_user(owner_user)
#     print("owner user created successfully!")

# def create_customer_user():
#     """Create the first owner user if no users exist."""
#     print("Creating a new customer user.")
#     username = input("Enter customer username: ")
#     password = input("Enter customer password: ")
    
#     customer_user = {
#         "username": username,
#         "password": password,
#         "role": "customer"
#     }
    
#     save_user(customer_user)
#     print("customer user created successfully!")
#     return customer_user

# def owner_menu(users_data):
#     while True:
#         print("\nowner Menu:")
#         print("1. Login")
#         print("2. Sign Up")
#         print("3. Back")
        
#         choice = input("Enter your choice: ")
        
#         if choice == '1':
#             username = input("Enter your username: ")
#             password = input("Enter your password: ")
#             role = authenticate_user(username, password)
#             if role == 'owner':
#                 owner = owner(users_data)
#                 owner.run_owner_panel()
#         elif choice == '2':
#             create_owner_user()
#         elif choice == '3':
#             break
#         else:
#             print("Invalid choice. Please try again.")

def customer_menu():
    while True:
        print("\ncustomer Menu:")
        print("1. Login")
        print("2. Sign Up")
        print("3. Back")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            role = authenticate_user(username, password)
            print(role)
            
        #     if role == 'customer':
        #         customer = customer(users_data)
        #         customer.run_customer_panel()
        # elif choice == '2':
        #     create_customer_user()
        # elif choice == '3':
        #     break
        # else:
        #     print("Invalid choice. Please try again.")

def main_menu():
    """Main menu to choose between owner, customer, or Exit."""
    while True:
        print("\nWelcome to the Restaurant Management System")
        print("1. owner")
        print("2. customer")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            pass
            # users_data = load_users()
            # if users_data is None:
            #     first_owner = create_owner_user()
            #     users_data = [first_owner]
            # owner_menu(users_data)
        elif choice == '2':
            # users_data = load_users()
            customer_menu()
        elif choice == '3':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__==  "__main__":
    main_menu()
