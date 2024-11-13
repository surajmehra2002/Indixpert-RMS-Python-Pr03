from src.models.json_files_path import load_users
from src.models.json_files_path import save_user_when_signup

class Users:
    def __init__(self):
        self.users = load_users()

    def promote_user_to_admin(self):
        while True:
            # Prompt for the username
            username = input("Enter the username of the customer to promote to admin (press 0 for exit): ").strip()
            if username == '0':
                break
            # Check if username input is empty
            if not username:
                print("Username cannot be empty. Please enter a valid username.")
                continue

            user_found = False

            # Search for the user in the list
            for user in self.users:
                if user['username'].lower() == username.lower():
                    user_found = True
                    # Check if user is already an admin
                    if user['role'] == 'customer':
                        user['role'] = 'admin'
                        save_user_when_signup(self.users)
                        print(f"User '{username}' has been promoted to admin.")
                    else:
                        print(f"User '{username}' is already an admin.")
                    break

            # If user is not found, prompt again
            if not user_found:
                print(f"No user found with username '{username}'. Please try again.")
            else:
                break
    def remove_user_from_admin(self):
        while True:
            # Prompt for the username
            username = input("Enter the username of the customer to promote to customer (press 0 for exit): ").strip()
            if username == '0':
                break
            # Check if username input is empty
            if not username:
                print("Username cannot be empty. Please enter a valid username.")
                continue

            user_found = False

            # Search for the user in the list
            for user in self.users:
                if user['username'].lower() == username.lower():
                    user_found = True
                    # Check if user is already an admin
                    if user['role'] == 'admin':
                        user['role'] = 'customer'
                        save_user_when_signup(self.users)
                        print(f"User '{username}' has been removed from to admin.")
                    else:
                        print(f"User '{username}' is already an customer.")
                    break

            # If user is not found, prompt again
            if not user_found:
                print(f"No user found with username '{username}'. Please try again.")
            else:
                break

    def view_all_users(self):
        print(f"{'ID':<15} {'Username':<15} {'Mobile':<15} {'Role':<30} {'Joining Date':<15}")
        print("-" * 85)
        
        for user in self.users:
            print(f"{user['id']:<15} {user['username']:<15} {user['mobile']:<15} {user['role']:<30} {user['joining_date']:<15}")

        
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
                if user_id == '0':
                    break
                    
                elif len(user_id)==8:
                    found = False
                    for user in self.users:
                        if user['id'] == user_id:
                            break
                        else:
                            found = True
                            
                    if found:
                        print("Invalid user ID! ")


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

