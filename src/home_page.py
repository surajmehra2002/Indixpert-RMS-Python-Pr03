
import uuid,datetime

import src.models.authentication as auth
# importing class
from src.access_control.customer import Customer
from src.access_control.admin import Admin

def generate_id():
    return str(uuid.uuid4())[0:8]
    

def save_user(user_data):
    auth.sign_up_autentication(user_data)
   

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
        
        if len(username) < 5:
            print("Username must be at least 5 characters long.")
        elif username == "":
            print("Username can't be empty.")
        else:
            break
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
            
            if len(mobile) == 10 and mobile.isdigit():
                return int(mobile) 
            else:
                print("Error: Mobile number must be exactly 10 digits.")
        
        except ValueError:
            print("Error: Invalid input. Please enter only digits.")

def user_role():
    role = 'customer'
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


def login_users():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    role = auth.authenticate_user(username, password)           
    
    
                
    if role == 'customer':
                has_user_block = auth.user_block(username)
                user = auth.get_user_from_db(username)
                if has_user_block:
                    print(f"You are block by our system with '{user['blocked']}' reason ")
                    return
                
                print("Login Successfully!\n")
                customer = Customer(user)
                customer.run_customer_panel()
    if role == 'admin':
                print("Login Successfully!\n")
                user = auth.get_user_from_db(username)
                admin = Admin(user)
                admin.run_admin_panel()

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
