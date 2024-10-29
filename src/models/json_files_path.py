users_file_path = 'src/data_base/users.json'
menu_file_path = 'src/data_base/menu.json'

import os

def get_users_json():
    return users_file_path

def get_menu_json():
    return menu_file_path

# def get_menu_json():
#     if os.path.exists(menu_file_path):
#         try:
