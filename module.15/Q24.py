
# Write a Python program to show method overriding.?

class Vehicle:
    def start(self):
        print("Vehicle start system")

class Bike(Vehicle):
    def start(self):
        super().start()
        print("Bike starts with a kick or button")

bike = Bike()
bike.start()