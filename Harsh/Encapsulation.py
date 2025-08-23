
# Encapsulation : - Wrapping data and function into a single unit(object).




# Create Account class with 2 attributes - balance & account no.
# create methods for debit, credit & printing the balance.
    
class Account :
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("RS.",amount, "was debited")
        print("total balance =",self.get_balance())


    def credit(self, amount):
        self.balance += amount
        print("RS.",amount, "was creadited")
        print("total balance =",self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)
# print(acc1.balance)
# print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)