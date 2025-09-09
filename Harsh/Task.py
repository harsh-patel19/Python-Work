
# 1. Inheritance Task :- 

# class Vehicle :

#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def show_deatils(self):
#         print({self.brand},{self.model})


# class Car(Vehicle):
#     def __init__(self, brand, model, seats):
#         super().__init__(brand,model)
#         self.seats = seats

#     def show_deatils(self):
#         super().show_deatils()
#         print({self.seats})


# class Bike(Vehicle):
#     def __init__(self, brand, model, engine_cc):
#         super().__init__(brand, model)
#         self.engine_cc = engine_cc

#     def show_deatils(self):
#         super().show_deatils()
#         print({self.engine_cc})

# car1 = Car("Toyota","corolla",5)
# car1.show_deatils()

# print("*****************")
# Bike1 = Bike("Yamaha","R15",155)
# Bike1.show_deatils()



# 2. Encapsulation Task :-

# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self.__balance = initial_balance
        

#     def deposite(self,amount):
#         if amount > 0:
#             self.__balance += amount
#             print({amount})

#         else:
#             print("deposite amount must be positive")

        
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print({amount})

#         else:
#             print("invaild amount")

#     def get_balance(self):
#         return self.__balance
    
# num1 = BankAccount(10000)
# num1.deposite(5000)
# num1.withdraw(2000)
# num1.get_balance()


# 3. Abstraction Task :- 

# from abc import ABC , abstractmethod
# import math

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)
    
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width
    
# c1 = Circle(10)
# c2 = Rectangle(5,5)

# print(Circle.area())
# print(Rectangle.area())
        

# 4 . Polymorphism Task :- 

# class Dog:
#     def speak(self):
#         return "Woof!"
    
# class Cat:
#     def speak(self):
#         return "Meow!"
    

# animals = [Dog(), Cat()]
# for animal in animals:
#     print(animal.speak())


# def f (a, L=[]):
#     L.append(a)
#     return L
# print(f(1))
# print(f(2, []))
# print(f(3))




