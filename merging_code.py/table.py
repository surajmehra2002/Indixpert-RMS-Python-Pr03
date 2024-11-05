import json
from datetime import datetime

class TableBooking:
    def __init__(self, num_tables=10, seats_per_table=4):
        self.num_tables = num_tables
        self.seats_per_table = seats_per_table
        self.tables = self.load_tables()

    def load_tables(self):
        try:
            with open("tables.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            # Initialize tables if file not found
            return {f"Table_{i+1}": {"available_seats": self.seats_per_table} for i in range(self.num_tables)}

    def save_tables(self):
        with open("tables.json", "w") as file:
            json.dump(self.tables, file, indent=4)

    def book_table(self, table_id, seats_requested):
        if table_id not in self.tables:
            return f"{table_id} does not exist."

        if self.tables[table_id]["available_seats"] >= seats_requested:
            self.tables[table_id]["available_seats"] -= seats_requested
            self.tables[table_id]["booking_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_tables()
            return f"Table {table_id} booked successfully with {seats_requested} seats."
        else:
            return f"Table {table_id} does not have enough seats available."

    def check_availability(self):
        availability = {}
        for table_id, info in self.tables.items():
            availability[table_id] = "Available" if info["available_seats"] > 0 else "Not Available"
        return availability

    def reset_table(self, table_id):
        if table_id in self.tables:
            self.tables[table_id]["available_seats"] = self.seats_per_table
            self.tables[table_id].pop("booking_time", None)
            self.save_tables()
            return f"Table {table_id} reset successfully."
        else:
            return f"{table_id} does not exist."

# Main function with initial options
def main():
    booking_system = TableBooking()
    
    while True:
        # Display options to the user
        print("\nPlease choose an option:")
        print("1. Check Table Availability")
        print("2. Book a Table")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            # Show table availability
            availability = booking_system.check_availability()
            print("\nCurrent Availability of Tables:")
            for table, status in availability.items():
                print(f"{table}: {status}")

        elif choice == '2':
            # Book a table
            table_id = input("Enter the table ID you want to book (e.g., Table_1): ").strip()
            seats_requested = int(input("Enter the number of seats you want to book: "))
            booking_result = booking_system.book_table(table_id, seats_requested)
            print(booking_result)

        elif choice == '3':
            # Exit the program
            print("Exiting the system. Thank you!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
