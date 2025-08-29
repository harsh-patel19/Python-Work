

# Abstraction :-  Hiding the implementation details of a class and only showing the essential features to the user.

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car started..")

# car1 = Car()
# car1.start()


import datetime

# -------------------------
# Sample Inventory (Dictionary)
# -------------------------
inventory = {
    "Paracetamol": {"price": 2.5, "stock": 100},
    "Amoxicillin": {"price": 5.0, "stock": 50},
    "Cough Syrup": {"price": 4.0, "stock": 30},
}

sales_history = []  # Store sales as dictionaries


# -------------------------
# Display Inventory
# -------------------------
def view_inventory():
    print("\n📦 Current Inventory")
    print("-" * 40)
    print(f"{'Medicine':<15}{'Price':<10}{'Stock':<10}")
    print("-" * 40)
    for med, details in inventory.items():
        print(f"{med:<15}{details['price']:<10}{details['stock']:<10}")
    print("-" * 40)


# -------------------------
# Add / Update Medicine
# -------------------------
def update_inventory():
    try:
        med_name = input("Enter medicine name: ").title()
        price = float(input("Enter price: "))
        stock = int(input("Enter quantity to add: "))

        if med_name in inventory:
            inventory[med_name]["price"] = price
            inventory[med_name]["stock"] += stock
            print(f"✅ Updated {med_name} successfully!")
        else:
            inventory[med_name] = {"price": price, "stock": stock}
            print(f"✅ Added {med_name} to inventory!")
    except ValueError:
        print("❌ Invalid input. Please enter numeric values for price/quantity.")


# -------------------------
# Process Sale
# -------------------------
def process_sale():
    try:
        customer = input("Enter customer name: ").title()
        medicine = input("Enter medicine name: ").title()
        qty = int(input("Enter quantity: "))

        if medicine not in inventory:
            print("❌ Medicine not available.")
            return

        if qty > inventory[medicine]["stock"]:
            print(f"❌ Only {inventory[medicine]['stock']} units available.")
            return

        # Calculate total
        total_price = qty * inventory[medicine]["price"]
        sale_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Update stock
        inventory[medicine]["stock"] -= qty

        # Record sale
        sale_record = {
            "customer": customer,
            "medicine": medicine,
            "qty": qty,
            "total": total_price,
            "date": sale_date,
        }
        sales_history.append(sale_record)

        # Print Bill
        print("\n🧾 Sale Receipt")
        print("-" * 30)
        print(f"Customer: {customer}")
        print(f"Medicine: {medicine}")
        print(f"Quantity: {qty}")
        print(f"Price/unit: ₹{inventory[medicine]['price']}")
        print(f"Total Bill: ₹{total_price}")
        print(f"Date: {sale_date}")
        print("-" * 30)
        print("✅ Sale processed successfully!")

    except ValueError:
        print("❌ Invalid input. Quantity must be a number.")


# -------------------------
# View Sales History
# -------------------------
def view_sales():
    print("\n📑 Sales History")
    print("-" * 60)
    for sale in sales_history:
        print(
            f"{sale['date']} | {sale['customer']} bought {sale['qty']} {sale['medicine']} (₹{sale['total']})"
        )
    print("-" * 60)


# -------------------------
# Main Menu
# -------------------------
def main():
    while True:
        print("\n=== MediTrack Pharmacy System ===")
        print("1. View Inventory")
        print("2. Add/Update Medicine")
        print("3. Process Sale")
        print("4. View Sales History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_inventory()
        elif choice == "2":
            update_inventory()
        elif choice == "3":
            process_sale()
        elif choice == "4":
            view_sales()
        elif choice == "5":
            print("👋 Exiting MediTrack. Have a good day!")
            break
        else:
            print("❌ Invalid choice, please try again.")


# -------------------------
# Run Program
# -------------------------
if __name__ == "__main__":
    main()


