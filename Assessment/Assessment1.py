
inventory = {
    "Paracetamol":{"price":2.5, "stock":50},
    "Amoxicillin":{"price":10,"stock":20},
}

sales = []

def process_sale():
    customer = input("Enter customer name: ").strip()
    medicine = input("Enter medicine name: ").strip().title()


    if medicine not in inventory:
        print(f"Medicine {medicine} not found in inventory.")
        return
    
    try:
        qty = int(input("Enter Quantitly: "))
        if qty <= 0:
            print("quantitly must be greater than 0.")
            return
    except ValueError:
        print("Invaild quantitly. please enter a number.")
        return
    
    if inventory[medicine]["stock"] < qty:
        print("not enough stock available.")
        return
    
    inventory[medicine]["stock"] -= qty
    total_price = qty* inventory[medicine]["price"]

    sale = {
        "customer": customer,
        "medicine": medicine,
        "quantitly": qty,
        "total": total_price,
    }
    sales.append(sale)  

    print("\n bill")
    print("-"* 30)
    print(f"customer: {customer}")
    print(f"medicine: {medicine}")
    print(f"quantitly: {qty}")
    print(f"price per unit: &{inventory[medicine]['price']}")
    print(f"Total Amount: &{total_price}")
    print(f"date:c{sale['date']}")
    print("-"*30)

def view_inventory():
    print("\n===== Current Inventory =====")
    for med, details in inventory.items():
        print(f"{med:15} | Price: ₹{details['price']} | Stock: {details['quantity']}")
    print("=============================")


def update_inventory():
    med = input("Enter medicine name to add/update: ")
    try:
        price = float(input("Enter price: "))
        qty = int(input("Enter quantity: "))
    except ValueError:
        print(" Invalid input. Price/Quantity must be numeric.")
        return
    
    if med in inventory:
        inventory[med]["price"] = price
        inventory[med]["quantity"] += qty
        print(f" Updated {med} stock and price.")
    else:
        inventory[med] = {"price": price, "quantity": qty}
        print(f" Added new medicine: {med}")
        
def main():
    while True:
        print("\n===== MediTrack Pharmacy =====")
        print("1. Process Medicine Sale")
        print("2. View Inventory")
        print("3. Update Inventory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            process_sale()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            update_inventory()
        elif choice == "4":
            print(" Exiting... Thank you for using MediTrack.")
            break
        else:
            print(" Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
