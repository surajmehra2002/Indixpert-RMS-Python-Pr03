
from colorama import Fore, Style # type: ignore


from src.models.json_files_path import menu_update
from src.models.json_files_path import load_menu

class Menu:
    def __init__(self):
        self.items = load_menu()   
    
    
    def delete_menu_item(self):
        while True:  # Keep the function running until valid input or cancel
            # Asking for search input to match menu items
            search_term = input("Enter the name of the menu item to delete (min 3 characters): ").strip()
            
            if len(search_term) < 3:
                print("Search term must be at least 3 characters.")
                continue  # Keep asking for a valid search term

            # Filtering the items that match the search term
            matching_items = [item for item in self.items if search_term.lower() in item['name'].lower()]
            
            if not matching_items:
                print("No menu items found matching that name.")
                continue  # Keep asking for a valid search term

            # Display the matching items with index
            print("\nMatching menu items:")
            for idx, item in enumerate(matching_items, 1):
                print(f"{idx}. {item['name']} - {item['category']}")

            # Ask for the index of the item to delete
            try:
                item_idx = int(input("\nEnter the index of the item to delete (0 to cancel): "))
                if item_idx == 0:
                    print("Cancelled deletion.")
                    break  # Exit the function when pressing 0
                elif 1 <= item_idx <= len(matching_items):
                    # Get the item to delete
                    item_to_delete = matching_items[item_idx - 1]
                    self.items = [item for item in self.items if item != item_to_delete]
                    
                    # Save the updated menu back to the JSON file
                    menu_update(self.items)
                    print(f"Menu item '{item_to_delete['name']}' has been deleted.")
                    break  # Exit the function after successful deletion
                else:
                    print("Invalid index. Please select a valid index.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")


   


    
    def update_menu_item(self):
        item_found = False
        found = False
        while True:
            exit = False
            item_name = input("Enter the item name which you want update (press 0 to exit): ").strip()
            if item_name == '0':
                exit = True
                break
            if item_name == '':
                print("Empty item name not allow !")
                continue
            for item in self.items:
                if item['name'].lower() == item_name.lower():
                    found = True
                    break
            if found:
                break
            else:
                print(f"Invalid item name {item_name} in your menu !")


        if exit:
            return
        
        for item in self.items:
            # Find the item by name (case-insensitive)
            if item['name'].lower() == item_name.lower():
                item_found = True

                while True:
                    new_price_input = input(f"Enter new price for '{item['name']}' (or press Enter to keep current price of ₹{item['price']}): ")
                    if new_price_input.strip() == "":
                        break
                    try:
                        new_price = int(new_price_input)  # Try to convert input to float
                        if new_price < 0:
                            print("Price cannot be negative. Please enter a valid price.")
                            continue
                        item['price'] = new_price  # Update price if valid
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number for the price.")
                
                if 'half_price' in item:
                    while True:
                        half_price_input = input(f"Enter new half price for '{item['name']}' (or press Enter to keep current half price of ₹{item['half_price']}): ")
                        if half_price_input.strip() == "":
                            break
                        try:
                            new_half_price = int(half_price_input)
                            if new_half_price < 0:
                                print("Half price cannot be negative. Please enter a valid price.")
                                continue
                            item['half_price'] = new_half_price
                            break
                        except ValueError:
                            print("Invalid input. Please enter a valid number for the half price.")


                # Update availability if a new availability status is provided
                def new_availability():
                    while True:
                        availability = input("Is this item available (yes/no): ").strip().lower()
                        if availability == 'yes' or availability == 'no':
                            break
                        else:
                            print('Invalid input! ')
                    if availability == 'yes':
                        return True
                    else:
                        return False
                    
                item['availability'] = new_availability()

                print(f"Item '{item['name']}' updated successfully.")
                break

        if not item_found:
            print(f"Item '{item_name}' not found in the menu.")
        else:
            # Save the updated menu back to the JSON file
            menu_update(self.items)



    def display_menu(self):
        categories = list({item['category'] for item in self.items if item['availability']})

        if len(self.items) > 0:        
            print(Fore.GREEN+"\n===================  MENU  ===================="+Style.RESET_ALL)

            for category in categories:
                print(Fore.LIGHTMAGENTA_EX+ f"\n\n{category}"+Style.RESET_ALL)
                print(Fore.GREEN+ "-" * 50+ Style.RESET_ALL)
                print(Fore.GREEN+ f"{'Name':<25} {'Half':<15} {'Full':<25}"+Style.RESET_ALL)
                print(Fore.GREEN+ "-" * 50+ Style.RESET_ALL)

                for item in self.items:
                    # Only show the item if it is available
                    if item['category'] == category :
                        half_price = f"₹{item['half_price']}" if 'half_price' in item else '-'
                        print(Fore.LIGHTGREEN_EX+ f"{item['name']:<25} {half_price:<15} ₹{item['price']:<25}"+Style.RESET_ALL)

        else:
            print("Menu item not available.")


  

    def add_menu_item(self):
        if not self.items: #if list empty this this will excute
            print("Menu file not found.")
        else:
            exit = False
            while True:
                menu_name_list = [item['name'].lower() for item in self.items]
                name = input("Enter item name (press 0 to exit): ").strip()
                if name.lower() in menu_name_list:
                    print(f"ERROR: '{name}' already available in your menu! Add another...")
                elif name == '0':
                    exit = True
                    break
                else:
                    break
                    
            if exit:
                return
            category = input("Enter item category (e.g., Pizza, Beverage) (press 0 to exit): ").strip()

            if category == '0':
                return
                    
            
            # Check if the item has a half price option
            while True:
                choice = input("Does this item have a half-price option? (yes/no): ").strip().lower()
                if choice == 'yes' or choice == 'no':
                    break
                else:
                    continue
            has_half_price = choice == 'yes'
            
            if has_half_price:
                while True:
                    try:
                        half_price = int(input("Enter half price: "))
                        break
                    except ValueError:
                        print("Invalid input for half price. Please enter a numeric value.")
                        
            else:
                half_price = None  # No half price for items like Water

            # Full price and availability inputs with validation
            while True:
                try:
                    price = int(input("Enter full price: "))
                    availability = True
                    break
                except ValueError:
                    print("Invalid input for price. Please enter numeric values.")
                    

            # Create the new item, only including 'half_price' if applicable
            new_item = {
                "name": name,
                "category": category,
                "price": price,
                "availability": availability
            }
            
            # Include half price if it exists
            if half_price is not None:
                new_item["half_price"] = half_price
            self.items.append(new_item)
            confirm = input(f"Are you confirm to add {new_item['name']} item in menu(y/n): ")
            
            while True:
                if confirm == 'y':
                    menu_update(self.items)
                    print(f"Item '{new_item['name']}' added successfully.")
                    break
                
                elif confirm == 'n':
                    print('Canceled to add ')
                    break

                else:
                    print('Invalid item! ')

            

# menu = Menu()