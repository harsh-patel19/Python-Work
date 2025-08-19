
# Write a Python program to show single inheritance

class Animal:
    def speak(self):
        print("ANIMALS CAN MAKE SOUNDS..")

class Dog(Animal):
    def bark(self):
        print("DOG BARKS: WOOF.. WOOF..")

Dog1 = Dog()
Dog1.speak()
Dog1.bark()