import os,json

def load_users():
    """Load users from the JSON file or initialize if the file doesn't exist or is empty."""
    file_path = 'src/data/users.json'
    dir_path = 'src/data'
    
    # Check if the data directory exists, create it if not
    if not os.path.exists(dir_path):
        print(f"'{dir_path}' directory not found, creating it.")
        os.makedirs(dir_path)

    # Check if the users.json file exists, create it if not
    if not os.path.exists(file_path):
        print("Users file not found, creating a new one.")
        with open(file_path, 'w') as f:
            json.dump([], f)  # Initialize with an empty list
    
    # Load users from the file
    with open(file_path, 'r') as f:
        try:
            users = json.load(f)
            return users
        except json.JSONDecodeError:
            print("Error decoding users.json. Please ensure it's a valid JSON file.")
            return None


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
            if user["role"]=="owner":
                return "owner" 
            else:
                return "customer"
        else:
            print("Invalid credentials")
            


       
# if __name__=="__main__":
#     authenticate_user("deep", "singh")