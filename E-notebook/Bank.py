bank = {}

print("""
    WELCOME TO PYHTON BANK MANAGMENT SYSTEM
    select your role
      
    1) banker
    2) customer
    3) exit
""")
choice = int(input("choose your role: "))
choice =int(input("WElcome to Banker's App: "))
print("""   Operations Menu
            1)Add Customer
            2)view Customer
            3)serach Customer
            4)view All Customer
            5)Total Amounts in Bank
""")
if choice == 1:
   name = input("Enter customer name: ")
   acc_no = input("Enter acoount number: ")
   balance = float(input("Enter balance: "))
   bank.update({name:{"acc_no":acc_no,"balance":balance}})
   print("customer added..") 

elif choice == 2:
   acc_no = input("Enter account numbers: ")
   print(bank)
   
