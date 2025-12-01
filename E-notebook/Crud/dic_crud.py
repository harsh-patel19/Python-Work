
# Great! Here's a simple and clear CRUD project using Python Dictionary — perfect for beginners.

# CRUD Project Using Dictionary (Single File, Very Easy)
# Each item will have:
# id
# name
# price
# Data stored in a list of dictionaries

items = []

def create():
    print("-----Create Item-----")
    item_id = int(input("Enter Id: "))
    name = input("Enter Name: ")
    price = float(input("Enter price: "))


    item = {
        "id":item_id,
        "name":name,
        "price":price
    }

    items.append(item)
    price("Item added sucessfully!!")

def read():
    print("---Item List---")
    if not items:
        print("No available")
        return

    for item in items:
        print(f"ID:{item['id']} | name:{item['name']} | price:{item['price']}")

def update():
    item_id = int(input("Enter ID to Update: "))

    for item in items:
        if item['id'] == item_id:
            new = input("Enter new name: ")
            newprice = float(input("Enter new price: "))

            item['name'] = new
            item['price']= newprice

            print("updated")
            return
    print("not found")

def menu():
    while True:
        print("--CRUD MENU----")
        print("1.create item")
        print("2.read item")
        print("3.update item")
       
        choice = int(input("Enter Your choice: "))

        if choice =="1":
            create()
        elif choice =="2":
            read()
        elif choice =="3":
            update()
        else:
            print("invalid choice!!")

menu()