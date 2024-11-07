

import json
import os


from src.models.json_files_path import load_menu

class Menu:
    def __init__(self):
        self.items = load_menu()   


    def display_menu(self):
            categories = list({item['category'] for item in self.items})

            if len(self.items)>0:        
                print("\n===================  MENU  ====================")

                for category in categories:
                    print(f"\n\nCategory: {category}")
                    print("-" * 50)
                    print(f"{'Name':<25} {'Half':<15} {'Full':<25}")
                    print("-" * 50)


                    
                    for item in self.items:
                        if item['category'] == category:
                            half_price = f"₹{item['half_price']}" if 'half_price' in item else ''
                            print(f"{item['name']:<25} {half_price:<10} ₹{item['price']:<25}")


            else:
                print("menu item not available")
