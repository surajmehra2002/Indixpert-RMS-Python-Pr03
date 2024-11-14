
# Restaurant Management System

**before run this project** make sure that you are in "\Indixpert-RMS-Python-Pr03" directory in console if not then enter "cd .\indixpert_coaching\" in cmd panel :

## Overview

This Restaurant Management System is a Python-based application that allows administrators to manage a restaurant’s inventory, menu, orders, billing, and table reservations. It has two user roles: **Admin** and **Customer**, each with distinct access permissions. The project is structured following Object-Oriented Programming (OOP) principles and organized into packages for easy maintenance and scalability.

## Features

- **User Authentication**: Separate login and registration for Admin and Customer users.
- **Inventory Management**: Track inventory items with stock and prices.
- **Menu Management**: Add, update, delete, and display menu items.
- **Order Processing**: Take and manage customer orders, calculate total prices with GST, and generate invoices.
- **Table Reservation**: Manage table reservations based on party size.
- **User Blocking**: Admin can block users with specific reasons, preventing blocked users from logging in.
- **Detailed Invoice Generation**: Generate detailed invoices with order details, GST, and total cost.

## Project Structure


## Prerequisites

- **Python 3.x**: Ensure you have Python installed. [Download Python](https://www.python.org/downloads/)
- **Required Modules**: Install the necessary Python packages listed in `requirements.txt` (or use the list below).

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. **Set up a Virtual Environment**(optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   
3. **Install Dependencies:** If you have a requirements.txt file, run:
   ```bash
   pip install -r requirements.txt
   pip install colorama maskpass tabulate

4. **Data Setup:** Ensure that necessary JSON files (e.g., menu.json, users.json) are available in the src/database folder. These files store the initial data for menus, invoices, and other elements required for the system.

## Usage Instructions
    
1. **Running the Application:** If you have a requirements.txt file, run:
   ```bash
   python main.py


2. **User Guide**
**1. Admin:**
   
**Login/Register**: Choose the Admin role and login or sign up if it’s your first time.
**Admin Dashboard**: Access various functionalities, such as viewing and managing the menu, checking order status, blocking users, and managing tables.
**Order Status**: Check ongoing orders with detailed information, including date, time, customer details, items, subtotal, GST, grand total, status, and payment method.
**Blocking Users**: Admin can block users by choosing from predefined reasons and adding it to the user’s record.


 3.**Customer**

 **Login/Register**: Choose the Customer role and login or sign up.
 **View Menu**: Browse available menu items with prices.
 **Place Order**: Select items from the menu to place an order. The system will generate an invoice with details like subtotal, GST, and total cost.

## 3. Configuration

**Role-based Access**: Admin and Customer have different access levels. Admin has full control, while Customers can only place orders and reserve tables.
**User Data**: User-related data (such as blocked status and reasons) are stored in respective JSON files.

## 4. Examples

**Adding a Menu Item (Admin)**
  ```bash
  1. Go to Admin Dashboard -> Menu Management.
  2. Choose "Add Menu Item" and provide the required details (item name, price, category).


**Placing an Order (Customer)**
  ```bash
    1. Login as a Customer.
    2. View Menu and select items to place an order.
    3. An invoice will be generated with order details, GST, and total cost.
  





