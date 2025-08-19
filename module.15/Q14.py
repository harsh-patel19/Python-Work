
# Write a Python program to create a class and access the properties
# of the class using an object..?


class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}")
        

Car1 = Car("Tesla","model s", 85000)
Car1.show_details()