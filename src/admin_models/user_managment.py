from src.models.json_files_path import load_users
from src.models.json_files_path import save_user_when_signup

class Users:
    def __init__(self):
        self.users = load_users()
        
    def block_reason(self):
        print("\nChoose a reason to block the user:")
        reasons = [
            "1: Violation of terms and conditions",
            "2: Multiple failed login attempts",
            "3: Excessive complaints from other users",
            "4: Account temporarily suspended for security reasons"
        ]
        
        for reason in reasons:
            print(reason)

        while True:
            choice = input("Enter the reason number (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                return reasons[int(choice) - 1][3:]  # Remove the number and colon from the reason
            else:
                print("Invalid input. Please select a reason number (1-4).")

    def block_user(self):
        if not self.users:
            print("No users are login yet!")
        else:
            while True:
                user_id = input("Enter user ID to block: (0 for cancel): ").strip()
                if user_id == '0' or len(user_id)==8:
                    break
                elif len(user_id)<8 or len(user_id)>8:
                    print('User ID should 8 character')
                    continue
            if user_id == '0':
                print('Canceled to block user')
                return #exit function when press 0
            
            user_found = False

            for user in self.users:
                if user["id"] == user_id:
                    if user['role']=='customer':
                        if "blocked" in user:
                            print(f"User is already blocked. Reason: {user['blocked']}")
                        else:
                            reason = self.block_reason()
                            user["blocked"] = reason
                            print(f"User '{user['username']}' has been blocked for the following reason: {reason}")
                            
                        user_found = True
                        break
                    else:
                        print("You havn't access to block admin! ")
            save_user_when_signup(self.users)  
            if not user_found:
                print("User ID not found. Please try again.")

# # Usage example:
# users = [
#     {"id": "2e38fdfc", "name": "suraj", "username": "suraj", "user_email": "suraj@gmail.com", "password": "surajsingh", "mobile": 9634912165, "role": "customer", "joining_date": "05-11-2024"},
#     {"id": "83437730", "name": "manoj", "username": "manoj", "user_email": "manoj@gmail.com", "password": "manojsingh", "mobile": 9634377090, "role": "admin", "joining_date": "07-11-2024"}
# ]

# block_user(users)
