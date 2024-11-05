import json,datetime
import os
import uuid

import src.models.authentication as auth




# importing class
from src.models.customer import Customer

def generate_id():
    return str(uuid.uuid4())[0:8]
    

def save_user(user_data):
    auth.sign_up_autentication(user_data)
   
           


# def create_admin_user():
#     """Create the first admin user if no users exist."""
#     print("Creating a new admin user.")
#     username = input("Enter admin username: ")
#     password = input("Enter admin password: ")
    
#     admin_user = {
#         "username": username,
#         "password": password,
#         "role": "admin"
#     }
    
#     save_user(admin_user)
#     print("admin user created successfully!")


def user_email():
    import re
    email = input("Enter customer Email: ").strip() 
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return email
    else:
        print("invalid email address")
        return user_email()
def user_first_name():    
    while True:
            first_name = input("Enter first name: ").strip()
            if first_name != "":
                break
            else:
                print("first name can't empty")
    return first_name
def user_name():
    while True:
            username = input("Enter your username: ").strip()
            if username != "":
                break
            else:
                print("username can't empty")
    return username

def user_password():
    while True:
        password = input("Enter your password (min 6 characters): ").strip()
        
        if len(password) < 6:
            print("Password must be at least 6 characters long.")
            continue
        
        confirm_password = input("Confirm your password: ").strip()
        
        if confirm_password != password:
            print("Passwords do not match. Please try again.")
            continue
        
        return password

def user_mobile_no():
    while True:
        try:
            mobile = input("Enter your mobile number: ")
            
            # Check if the input is a digit and is exactly 10 digits long
            if len(mobile) == 10 and mobile.isdigit():
                return int(mobile)  # Loop breaks here when a valid number is entered
            else:
                print("Error: Mobile number must be exactly 10 digits.")
        
        except ValueError:
            print("Error: Invalid input. Please enter only digits.")

def user_role():
    
    while True:
            conform = input("Are you admin (y/n)").strip().upper()
            if conform == "Y":
                role = "admin"
                break
            elif conform == "N":
                role = "customer"
                break
            else:
                print("Please enter valid input")  
    return role
            


def create_customer_user():
    print("Creating a new user.")

    customer_user = {
        "id": generate_id(),
        "name":user_first_name(),
        "username": user_name(),
        "user_email": user_email(),
        "password": user_password(),
        "mobile": user_mobile_no(),
        "role": user_role(),
        "joining_date": datetime.datetime.now().strftime("%d-%m-%Y")
    }
    
    save_user(customer_user)
    
    return customer_user

# def admin_menu(users_data):
#     while True:
#         print("\nadmin Menu:")
#         print("1. Login")
#         print("2. Sign Up")
#         print("3. Back")
        
#         choice = input("Enter your choice: ")
        
#         if choice == '1':
#             username = input("Enter your username: ")
#             password = input("Enter your password: ")
#             role = authenticate_user(username, password)
#             if role == 'admin':
#                 admin = admin(users_data)
#                 admin.run_admin_panel()
#         elif choice == '2':
#             create_admin_user()
#         elif choice == '3':
#             break
#         else:
#             print("Invalid choice. Please try again.")


def login_users():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    role = auth.authenticate_user(username, password)           
                       
    if role == 'customer':
                print("Login Successfully!\n")
                user = auth.get_user_from_db(username)
                customer = Customer(user)
                customer.run_customer_panel()
    elif role == 'admin':
                print("You are admin ")

def main_menu():
    """Main menu to choose between admin, customer, or Exit."""
    print("\n==============* Welcome to the Restaurant Management System *==================")
    while True:
        
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_customer_user()
        elif choice == '2':
            login_users()            
        elif choice == '3':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

# if __name__==  "__main__":
#     main_menu()
