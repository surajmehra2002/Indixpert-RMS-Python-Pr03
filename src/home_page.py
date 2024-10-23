import json
import os
import uuid
from users.authentication import authenticate_user
from users.authentication import get_user_from_db
# from users.authentication import authenticate_user
# from users.owner import owner
from users.customer import Customer

def generate_id():
    return str(uuid.uuid4())[0:8]

def load_users():
    """Load users from the JSON file or initialize if the file doesn't exist or is empty."""
    file_path = 'src/data/users.json'
    # dir_path = 'src/data'
    if os.path.exists(file_path):
        print('found')
        with open(file_path, 'r') as f:
            try:
                users = json.load(f)
                return users
            except json.JSONDecodeError:
                # print("Error decoding users.json. Please ensure it's a valid JSON file.")
                return None
    else:
        print('notfound')
        print("Users file not found, creating a new one.")
        with open(file_path, 'w') as f:
            json.dump([], f)  # Initialize with an empty list

  
    

def save_user(user_data):
    """Save the new user to users.json."""
    file_path = 'src/data/users.json'

    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file:
                users = json.load(file)
            
        except json.JSONDecodeError:   
            users = []

        found = False

        for user in users:
            if user_data["user_email"]==user["user_email"]:
                found = True
            
        if found:   
            print("User already exists")
        else:
            users.append(user_data)
            with open(file_path, 'w') as file:
                json.dump(users, file, indent=4)
            print("customer user created successfully!")
 


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
def user_email():
    import re
    email = input("Enter customer Email: ").strip() 
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return email
    else:
        print("\n invalid email address")
        return user_email()
    
def create_customer_user():
    """Create the first owner user if no users exist."""
    print("Creating a new customer user.")
    while True:
            username = input("Enter your username: ").strip()
            if username != "":
                break
            else:
                print("username can't empty")
    email = user_email()
    while True:
            password = input("Enter your password: ").strip()
            if password != "":
                break
            else:
                print("password can't empty")
    customer_user = {
        "id": generate_id(),
        "username": username,
        "user_email": email,
        "password": password,
        "role": "customer"
    }
    
    save_user(customer_user)
    
    return customer_user

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
    # users = load_users()
    
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
            
                       
            if role == 'customer':
                print("Login Successfully!\n")
                user = get_user_from_db(username)
                customer = Customer(user)
                customer.run_customer_panel()
            elif role == 'owner':
                print("Invalid credentials")
        elif choice == '2':
            create_customer_user()
        elif choice == '3':
            break
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
            customer_menu()
        elif choice == '3':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__==  "__main__":
    main_menu()
