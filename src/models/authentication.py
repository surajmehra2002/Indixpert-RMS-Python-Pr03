import os,json
from src.models.json_files_path import load_users
from src.models.json_files_path import save_user_when_signup

def get_user_from_db(username):
    found = False
    users = load_users()
    for user in users:
        if user["username"]==username:
            found = True
            return user
    if not found:
        print("User not exist! Please Sign Up..")
       
       


def authenticate_user(username, password):
    """Authenticate the user by checking username and password."""
    user = get_user_from_db(username)
    
    if user is not None:    
        if user["password"] == password:
            if user["role"]=="admin":
                return "admin" 
            else:
                return "customer"
        else:
            print("Invalid credentials")

def user_block(username):
    user = get_user_from_db(username)
    if user is None:
        return
    elif "blocked" in user:
        return True 
    else:
        return False


def sign_up_autentication(user_data):
    users = load_users()
    found = False

    for user in users:
        if user_data["user_email"]==user["user_email"]:
            found = True
            
    if found:   
        print("User already exists")
    else:
        users.append(user_data)
        save_user_when_signup(users)
          
        print(f"successfully {user_data["role"]} account created!")

            


       
# if __name__=="__main__":
#     authenticate_user("deep", "singh")