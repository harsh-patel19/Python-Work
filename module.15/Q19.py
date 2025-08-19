
# Write a Python program to show hierarchical inheritance.

class Animal:
    def speak(self):
        print("ANimals can make sounds")

class Dog(Animal):
    def speak(self):
        print("Dog says: woof woof")

class cat(Animal):
    def speak(self):
        print("cat says: Meow Meow..")

class cow(Animal):
    def speak(self):
       print("cow says: moo moo..")

Dog = Dog()
Dog.speak()
cat = cat()
cat.speak()
cow = cow()
cow.speak()
