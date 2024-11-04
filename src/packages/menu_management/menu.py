

import json
import os

from src.models.json_files_path import load_menu

class Menu:
    def __init__(self):
        self.items = load_menu()   


    def display_menu(self):

            if len(self.items)>0:        
                print("\n********Display all menu items.**********")
                print(f"{'Item Id':<20} {'Name':<25} {'Category':<20} {'Price':<20} {'Description':<20} {'Availablity':<20} ")  # Header
                print("-" * 125)  
            
                for item in self.items:
                    print(f"{item['item_id']:<20} {item['name']:<25} {item['category']:<20} {item['price']:<20} {item['description']} {item['availability']}")
            else:
                print("menu item not available")

   