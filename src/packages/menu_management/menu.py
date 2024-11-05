

import json
import os


from src.models.json_files_path import load_menu

class Menu:
    def __init__(self):
        self.items = load_menu()   


    def display_menu(self):
            categories = list({item['category'] for item in self.items})

            if len(self.items)>0:        
                print("\n=============  MENU  ================")

                for category in categories:
                    print(f"\n{category}")
                    print("-" * 35)
                    for item in self.items:
                        if item['category'] == category:
                            print(f"{item['name']:<25} ₹{item['price']:<25}")


            else:
                print("menu item not available")
