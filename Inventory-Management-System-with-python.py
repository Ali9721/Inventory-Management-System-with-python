# At first, using "csv"
import csv

FILENAME = 'inventory.csv'

# Add item
def add_item():
    name = input("Please enter item name: ")
    quantity = int(input("Please enter quantity: "))
    price = float(input("Please enter price: "))

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, quantity, price])
    print("Item added!")

# view items
def view_items():
    try:
        with open(FILENAME,'r') as file:
            reader = csv.reader(file)
            print(f"{'Name': <20} {'Quantity': <10} {'Price': <10}")
            print("_"*40)
            for row in reader:
                print(f"{row[0]:<20} {row[1]:<10} {row[2]:<10}")
    except FileNotFoundError:
        print("No Inventory Found!")

# Main Menu
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. View Items")
        print("3. Exit")
        choice = input("choose an option: ")
        if choice == "1":
            add_item()
        elif choice == '2':
            view_items()
        elif choice == '3':
            print("goodbye!")
            break
        else:
            print( "Invalid choice.")

if __name__ == "__main__":
    main()
