
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
    print("\n current Inventory")
    print("-" *40)
    print(f"{med: <15}{deatils['price']:<10}{details}")