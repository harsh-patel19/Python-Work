
class insufficeintamountexception(Exception):
    def __init__(self, *args):
        super().__init__(*args)



class Account:
     
    balance = 0 

    def get_balance(self):
        print("current balance is : ",self.balance)

    def deposite(self,amt):
        self.balance+=amt

    def withdrow(self,amt):
        if amt > self.balance:
            raise insufficeintamountexception("you need more in your account:",amt-self.balance)
        else:
            self.balance-=amt
    
ac = Account()
# ac.get_balance()
ac.deposite(50000)
ac.get_balance()
ac.withdrow(10000)
ac.get_balance()
ac.withdrow(10000)

try:
    ac.withdrow(15000)
except Exception as e:
    print(e)

ac.get_balance()