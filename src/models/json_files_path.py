import os, json


users_file_path = 'src/data_base/users.json'
menu_file_path = 'src/data_base/menu.json'
order_file_path = 'src/data_base/customers'
analysis_file_path = 'src/data_base/tracker_analysis.json'

def if_not_exit_tracer():
    tracker = []
    report = {}
    report["total_revenue"]=0.00
    report["total_refunds"]=0.00
    report["order_status"]={}
    report["order_status"]["completed"] = 0
    report["order_status"]["canceled/refunded"] = 0
    report["order_status"]["Order Placed"] = 0
    tracker.append(report)
    return tracker

def load_tracker():
    if os.path.exists(analysis_file_path):
        try:
            with open(analysis_file_path) as file:
                tracker = json.load(file) #list
        except:
            tracker = if_not_exit_tracer()
            tracker_update(tracker)
    else:
        tracker = if_not_exit_tracer()
        tracker_update(tracker)
    return tracker

def tracker_update(data):
    with open(analysis_file_path, 'w') as file:
        json.dump(data, file, indent=4)
            

def menu_update(menu):
    with open (menu_file_path, 'w') as file:
        json.dump(menu, file, indent=4)
    

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

def load_all_invoices_of_an_user(directory):
    invoices_list = []
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".json"):
                with open(os.path.join(directory, filename) ) as file:
                    invoice = json.load(file)
                    invoices_list.append(invoice)
            
    except FileNotFoundError:
        pass
    return invoices_list

def get_all_invoices():
    invoices = []

    # Traverse all subdirectories and files in the root_folder
    for subdir, _, files in os.walk(order_file_path):
        for file in files:
            if file.startswith("invoice") and file.endswith(".json"):
                file_path = os.path.join(subdir, file)
                # Read the JSON content from the invoice file
                try:
                    with open(file_path, 'r') as f:
                        invoice_data = json.load(f)
                        invoices.append(invoice_data)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    
    return invoices
