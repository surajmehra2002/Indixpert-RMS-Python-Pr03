from src.models.json_files_path import load_users
from src.models.json_files_path import save_user_when_signup

class Users:
    def __init__(self):
        self.users = load_users()


    def view_user_profile(self):
        if not self.users:
            print("No users available in the system!")
            return

        while True:
            # Prompt the admin to enter a username to search
            search_term = input("Enter at least 3 characters of the username to search (0 to exit): ").strip()

            if search_term == '0':  # Exit condition
                print("Exiting user profile view.")
                return

            if len(search_term) < 3:  # Validation for minimum characters
                print("Please enter at least 3 characters to search.")
                continue

            # Find users whose username contains the search term (case-insensitive)
            matching_users = [user for user in self.users if search_term.lower() in user["username"].lower()]

            if not matching_users:  # No matches found
                print(f"No users found with the term '{search_term}'. Please try again.")
                continue

            # Display the list of matching users with index numbers
            print("\nMatching Users:")
            for index, user in enumerate(matching_users):
                print(f"{index + 1}. {user['username']}")  # Display index + 1 for user-friendly numbering

            while True:
                try:
                    # Ask for the index to view the profile
                    choice = input("Enter the index number of the user to view their profile (0 to go back): ").strip()

                    if choice == '0':  # Go back to search
                        print("Returning to search.")
                        break

                    choice_index = int(choice) - 1  # Convert to zero-based index

                    if 0 <= choice_index < len(matching_users):  # Validate index range
                        selected_user = matching_users[choice_index]

                        # Display user profile
                        print("\nUser Profile:")
                        for key, value in selected_user.items():
                            print(f"{key.capitalize()}: {value}")
                        print("-" * 40)
                        break
                    else:
                        print("Invalid index. Please select a valid number from the list.")
                except ValueError:
                    print("Please enter a valid number.")

        




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
        print('Staff List')
        print('-' * 85)
        print(f"{'ID':<15} {'Username':<15} {'Mobile':<15} {'Joining Date':<15}")
        print("-" * 85)
        
        for user in self.users:
            if user['role'] == 'staff':
                print(f"{user['id']:<15} {user['username']:<15} {user['mobile']:<15}  {user['joining_date']:<15}")
    
    def view_all_admins(self):
        print('Admin List')
        print('-' * 85)
        print(f"{'ID':<15} {'Username':<15} {'Mobile':<15} {'Joining Date':<15}")
        print("-" * 85)
        for user in self.users:
            if user['role'] == 'admin':
                print(f"{user['id']:<15} {user['username']:<15} {user['mobile']:<15}  {user['joining_date']:<15}")
        


    def view_block_users(self):
        print('Block Users List')
        print('-' * 85)
        print(f"{'ID':<15} {'Username':<15} {'Mobile':<15} {'Joining Date':<15} {'Block reason':<50}")
        print("-" * 85)
        found = False
        for user in self.users:
            if "blocked" in user:
                found = True
                print(f"{user['id']:<15} {user['username']:<15} {user['mobile']:<15}  {user['joining_date']:<15} {user['blocked']:<50}")
        if not found:
            print("Nothing blocked users yet! ") 
        
    def block_reason(self):
        print("\nChoose a reason to block the user:")
        reasons = [
            "1: Violation of terms and conditions",
            "2: Multiple failed login attempts",
            "3: Excessive complaints from other users",
            "4: Account temporarily suspended for security reasons",
            "5: Cancel block"
        ]

        for reason in reasons:
            print(reason)

        while True:
            choice = input("Enter the reason number (1-5): ").strip()
            if choice in ['1', '2', '3', '4']:
                return reasons[int(choice) - 1][3:]  # Remove the number and colon from the reason
            elif choice == '5':
                print("Block action canceled.")
                return None  # Indicate cancellation
            else:
                print("Invalid input. Please select a reason number (1-5).")


    def block_user(self):
        if not self.users:
            print("No users are logged in yet!")
            return

        while True:
            user_id = input("Enter user ID to block (0 for cancel): ").strip()
            if user_id == '0':
                print("Canceled blocking user.")
                return  # Exit function when pressing 0

            elif len(user_id) == 8:
                found_user = next((user for user in self.users if user['id'] == user_id), None)
                if found_user:
                    break
                else:
                    print("Invalid user ID!")
            else:
                print("User ID should be 8 characters.")
        
        user = next((user for user in self.users if user["id"] == user_id), None)
        if user:
            if user["role"] == "customer":
                if "blocked" in user:
                    print(f"User is already blocked. Reason: {user['blocked']}")
                else:
                    reason = self.block_reason()
                    if reason is None:
                        print("User blocking process canceled.")
                        return  # Exit if the user cancels blocking
                    
                    # Confirmation alert before blocking
                    confirm = input(f"Are you sure you want to block this user for '{reason}'? (yes/no): ").strip().lower()
                    if confirm == 'yes':
                        user["blocked"] = reason
                        print(f"User '{user['username']}' has been blocked for the following reason: {reason}")
                    else:
                        print("User blocking process canceled.")
            else:
                print("You don't have access to block an admin!")
        
        save_user_when_signup(self.users)


    def unblock_user(self):
        if not self.users:
            print("No users are available!")
            return

        while True:
            username = input("Enter the username to unblock (0 to cancel): ").strip()

            if username == '0':
                print("Unblocking operation canceled.")
                return

            # Find the user by username
            user = next((u for u in self.users if u["username"] == username), None)
            if user:
                if "blocked" in user:
                    # Remove the 'blocked' key to unblock the user
                    del user["blocked"]
                    save_user_when_signup(self.users)
                    print(f"User '{user['username']}' has been unblocked successfully.")
                else:
                    print(f"User '{user['username']}' is not blocked.")
                return
            else:
                print("Invalid username! Please try again.")

