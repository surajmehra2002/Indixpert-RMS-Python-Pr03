import os,json

def load_users():
    """Load users from the JSON file or initialize if the file doesn't exist or is empty."""
    file_path = 'data/users.json'
    dir_path = 'data'
    
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
    """Fetch a user by username from the users.json file."""
    users = load_users()
    if users:
        for user in users:
            if user['username'] == username:
                return user
    return None

def authenticate_user(username, password):
    """Authenticate the user by checking username and password."""
    user = get_user_from_db(username)
    
    if user and user['password'] == password:
        if user['role'] == 'admin':
            return 'admin'
        else:
            return 'client'
    else:
        print("Invalid credentials")
        return None
