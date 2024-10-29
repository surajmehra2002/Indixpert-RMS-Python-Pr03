

import json
import os

from src.models.json_files_path import get_menu_json

class Menu:
    def __init__(self):
        self.menu_file = get_menu_json()
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
                print(f"{'Item Id':<20} {'Name':<25} {'Category':<20} {'Price':<20} {'Description':<20} {'Availablity':<20} ")  # Header
                print("-" * 125)  
            
                for item in self.items:
                    print(f"{item['item_id']:<20} {item['name']:<25} {item['category']:<20} {item['price']:<20} {item['description']} {item['availability']}")
            else:
                print("menu item not available")

   