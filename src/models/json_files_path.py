users_file_path = 'src/data_base/users.json'
menu_file_path = 'src/data_base/menu.json'

import os, json

def load_users():
    if os.path.exists(users_file_path):
        try:
            with open(users_file_path) as file:
                users = json.load(file)
        except:
            users = []
    else:
        users = []
        with open(users_file_path, 'w') as file:
            json.dump(users, file)
    return users

def save_user_when_signup(users):
    with open(users_file_path, 'w') as file:
        json.dump(users, file, indent=4)

def load_menu():
    if os.path.exists(menu_file_path):
        try:
            with open(menu_file_path) as file:
                menu_data = json.load(file)
        except:
            menu_data = []
    else:
        menu_data = []
    return menu_data
