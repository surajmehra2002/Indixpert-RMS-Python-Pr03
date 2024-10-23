

import json
import os

class Menu:
    def __init__(self, menu_file = '../../data/menu.json'):
        self.menu_file = os.path.join(os.path.dirname(__file__), menu_file)
        self.items = self.load_menu()

    def load_menu(self):
        """Load menu items from the JSON file."""
        if os.path.exists(self.menu_file):
            try:
                with open(self.menu_file, 'r') as file:
                    self.items = json.load(file)
            except:
                print("menu item not available")
                self.items = []
        else:
            self.items = []
        return self.items


    def display_menu(self):

            if len(self.items)>0:        
                print("\n********Display all menu items.**********")
                print(f"{'Name':<20} {'Price':<10}")  # Header
                print("-" * 27)  
            
                for item in self.items:
                    print(f"{item['Name']:<20} {item['Price']:<10}")
            else:
                print("menu item not available")

    # def update_item(self, item_id, updated_item):
    #     """Update an existing menu item."""
    #     for index, item in enumerate(self.items):
    #         if item['id'] == item_id:
    #             self.items[index] = updated_item
    #             self.save_menu()  # Save changes to the file
    #             print(f"Menu item '{item_id}' updated successfully!")
    #             return
    #     print(f"Menu item with ID '{item_id}' not found!")

    # def delete_item(self, item_id):
    #     """Delete a menu item."""
    #     for index, item in enumerate(self.items):
    #         if item['id'] == item_id:
    #             del self.items[index]
    #             self.save_menu()  # Save changes to the file
    #             print(f"Menu item '{item_id}' deleted successfully!")
    #             return
    #     print(f"Menu item with ID '{item_id}' not found!")

    
# # Example usage
# if __name__ == "__main__":
#     menu_manager = Menu()

#     # Sample menu item to add
#     new_item = {
#         "id": 1,
#         "name": "Pizza",
#         "description": "Delicious cheese pizza",
#         "price": 12.99,
#         "available": True
#     }
    
#     menu_manager.add_item(new_item)  # Add the item to the menu
#     menu_manager.display_menu()  # Display the menu

# if __name__ == "__main__":
#     menu = Menu()
#     menu.display_menu()
