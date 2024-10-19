# packages/menu_management/menu.py
import json
import os

class Menu:
    def __init__(self, menu_file='packages/menu_management/menu.json'):
        self.menu_file = menu_file
        self.items = []  # Initialize items attribute to store menu items
        self.load_menu()

    def load_menu(self):
        """Load menu items from the JSON file."""
        if os.path.exists(self.menu_file):
            with open(self.menu_file, 'r') as file:
                self.items = json.load(file)  # Load items into the items attribute
        else:
            self.items = []  # Initialize an empty menu if the file doesn't exist
            self.save_menu()  # Create the menu.json file

    def save_menu(self):
        """Save menu items to the JSON file."""
        with open(self.menu_file, 'w') as file:
            json.dump(self.items, file, indent=4)

    def add_item(self, item):
        """Add a new menu item."""
        self.items.append(item)
        self.save_menu()  # Save changes to the file
        print(f"Menu item '{item['name']}' added successfully!")

    def update_item(self, item_id, updated_item):
        """Update an existing menu item."""
        for index, item in enumerate(self.items):
            if item['id'] == item_id:
                self.items[index] = updated_item
                self.save_menu()  # Save changes to the file
                print(f"Menu item '{item_id}' updated successfully!")
                return
        print(f"Menu item with ID '{item_id}' not found!")

    def delete_item(self, item_id):
        """Delete a menu item."""
        for index, item in enumerate(self.items):
            if item['id'] == item_id:
                del self.items[index]
                self.save_menu()  # Save changes to the file
                print(f"Menu item '{item_id}' deleted successfully!")
                return
        print(f"Menu item with ID '{item_id}' not found!")

    def display_menu(self):
        """Display all menu items."""
        if not self.items:
            print("No menu items found.")
        else:
            print("Menu Items:")
            for item in self.items:
                print(f"ID: {item['id']}, Name: {item['name']}, Price: {item['price']}, Available: {item['available']}")

# Example usage
if __name__ == "__main__":
    menu_manager = Menu()

    # Sample menu item to add
    new_item = {
        "id": 1,
        "name": "Pizza",
        "description": "Delicious cheese pizza",
        "price": 12.99,
        "available": True
    }
    
    menu_manager.add_item(new_item)  # Add the item to the menu
    menu_manager.display_menu()  # Display the menu
