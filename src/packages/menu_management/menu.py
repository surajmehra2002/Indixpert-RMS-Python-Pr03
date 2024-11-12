

import json
import os


from src.models.json_files_path import load_menu
from src.models.json_files_path import menu_update

class Menu:
    def __init__(self):
        self.items = load_menu()   
    
    import json

    def update_menu_item(self):
        item_found = False

        item_name = input("Enter the item name which you want update: ").strip()
        
        for item in self.items:
            # Find the item by name (case-insensitive)
            if item['name'].lower() == item_name.lower():
                item_found = True

                while True:
                    new_price_input = input(f"Enter new price for '{item['name']}' (or press Enter to keep current price of ₹{item['price']}): ")
                    if new_price_input.strip() == "":
                        break
                    try:
                        new_price = float(new_price_input)  # Try to convert input to float
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
                            new_half_price = float(half_price_input)
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
            print("\n===================  MENU  ====================")

            for category in categories:
                print(f"\n\nCategory: {category}")
                print("-" * 50)
                print(f"{'Name':<25} {'Half':<15} {'Full':<25}")
                print("-" * 50)

                for item in self.items:
                    # Only show the item if it is available
                    if item['category'] == category :
                        half_price = f"₹{item['half_price']}" if 'half_price' in item else '-'
                        print(f"{item['name']:<25} {half_price:<15} ₹{item['price']:<25}")

        else:
            print("Menu item not available.")


  

    def add_menu_item(self):
        if not self.items: #if list empty this this will excute
            print("Menu file not found.")
        else:
            while True:
                menu_name_list = [item['name'].lower() for item in self.items]
                name = input("Enter item name: ").strip()
                if name.lower() in menu_name_list:
                    print(f"ERROR: '{name}' already available in your menu! Add another...")
                else:
                    break

            category = input("Enter item category (e.g., Pizza, Beverage): ").strip()
            
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
                        half_price = float(input("Enter half price: "))
                        break
                    except ValueError:
                        print("Invalid input for half price. Please enter a numeric value.")
                        
            else:
                half_price = None  # No half price for items like Water

            # Full price and availability inputs with validation
            while True:
                try:
                    price = float(input("Enter full price: "))
                    availability_input = input("Is the item available? (yes/no): ").strip().lower()
                    availability = availability_input == 'yes'
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
            menu_update(self.items)
            print(f"Item '{new_item['name']}' added successfully.")

            

            

