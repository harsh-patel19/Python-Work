

# INHERITANCE EXAMPLE : -

# class Empolyee:
#     def __init__(self, name, salary):
#         self.name = name 
#         self.salary = salary

#     def show_deails(self):
#         print({self.name},{self.salary})

# class Manager(Empolyee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department

#     def show_deails(self):
#         super().show_deails()
#         print({self.department})

# class Developer(Empolyee):
#     def __init__(self, name, salary, programming_language):
#         super().__init__(name, salary)
#         self.language = programming_language

#     def show_deatils(self):
#         super().show_deails()
#         print({self.language})

    
# c1 = Manager("Harsh",80000,"hR")
# d1 = Developer("Dhruvika", 750000, "pyhton")

# c1.show_deails()
# d1.show_deails()


# 2. ENCAPSULATION EXAMPLE :- 

# class Student:
#     def __init__(self, name):
#         self.name = name 
#         self.__marks = 0

#     def set_marks(self, marks):
#         if 0 <= marks <= 100:
#             self.__marks = marks
#         else:
#             print("invalid marks")

#     def get_marks(self):
#         return self.__marks
    

# s1 = Student("Harsh")
# s1.set_marks(85)
# print(f"{s1.name}", s1.get_marks())
        
    
# 3. ABSTRACTION EXAMPLE :-

# from abc import ABC, abstractmethod
        
# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass

# class CreditCarPayment(Payment):
#     def pay(self, amount):
#         super().pay(amount)
#         print(f"{amount} using Credit card..")

# class PayPalPayment(Payment):
#     def pay(self, amount):
#         super().pay(amount)
#         print(f"{amount} Using paypal..")


# Payment1 = CreditCarPayment()
# Payment2 = PayPalPayment()

# Payment1.pay(5000)
# Payment2.pay(2000)


# 4 . POLYMORPHISM EXAMPLE:-

# class square:
#     def area(self):
#         return 4 *4
    
# class circle:
#     def area(self):
#         return 3.14 *3 *3
    
# shapes = [square(), circle()]

# for shape in square:
#    print(f"{shape.area()}")



