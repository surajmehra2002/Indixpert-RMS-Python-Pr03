from src.models.json_files_path import load_users
from src.models.json_files_path import save_user_when_signup

from colorama import Fore, Style # type: ignore


def get_user_from_db(username):
    found = False
    users = load_users()
    for user in users:
        if user["username"]==username:
            found = True
            return user
    if not found:
        print(Fore.RED+"User not exist! Please Sign Up.."+ Style.RESET_ALL)
       
       


def authenticate_user(username, password):
    """Authenticate the user by checking username and password."""
    user = get_user_from_db(username)
    
    if user is not None:    
        if user["password"] == password:
            if user["role"]=="admin":
                return "admin" 
            else:
                return "staff"
        else:
            print(Fore.RED +"Invalid credentials"+ Style.RESET_ALL)

def user_block(username):
    user = get_user_from_db(username)
    if user is None:
        return
    elif "blocked" in user:
        return True 
    else:
        return False

def sign_up_authentication(user_data):
    users = load_users()
    
    # Check if email or mobile number already exists
    email_exists = False
    mobile_exists = False

    for user in users:
        if user_data["user_email"] == user["user_email"]:
            email_exists = True
        if user_data["mobile"] == user["mobile"]:
            mobile_exists = True
        # Break early if both are found
        if email_exists or mobile_exists:
            break

    # Display appropriate messages
    if email_exists:
        print(Fore.YELLOW + "User with this email already exists." + Style.RESET_ALL)
    elif mobile_exists:
        print(Fore.YELLOW + "Mobile number already used!" + Style.RESET_ALL)
    else:
        # Add user and save to database
        users.append(user_data)
        save_user_when_signup(users)
        print(f"Successfully created {user_data['role']} account!")
