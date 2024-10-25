import os,json
from src.models.json_files_path import get_users_json

def load_users():
    """Load users from the JSON file or initialize if the file doesn't exist or is empty."""
    file_path = get_users_json()
    if os.path.exists(file_path):
       
        with open(file_path, 'r') as f:
            try:
                users = json.load(f)
                return users
            except json.JSONDecodeError:
                # print("Error decoding users.json. Please ensure it's a valid JSON file.")
                users = []
                return users
    else:       
        users = []
        with open(file_path, 'w') as f:
            json.dump(users, f)  # Initialize with an empty list
        return users
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
            


       
# if __name__=="__main__":
#     authenticate_user("deep", "singh")