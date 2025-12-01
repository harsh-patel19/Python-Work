# METHOD OVERRINDING..?

class Animal:

    def eat(self):
        print("I Can Eat")

class Dog(Animal):

    def eat(self):
        print("I like to eat bones")

labrador = Dog()
labrador.eat()


# THE SUPER FUNCTION IN INHERITANCE..?

class Animal:
    def eat(self):
        print("I can eat")

class Dog(Animal):
    def eat(self):
        super().eat()
        print("I like to eat bones")

labrador = Dog()
labrador.eat()


# PYTHON MULTIPLE INHERITANCE..?

class mammal:
    def mammal_info(self):
        print("Mammals can give direct birth..")

class wingdAnimal:
    def wing_info(self):
        print("wing animals can flap..")

class bat(mammal,wingdAnimal):
    pass

b1 = bat()
b1.mammal_info()
b1.wing_info()


# MULTILEVEL INHERITANCE..?

class Superclass:
    def super_method(self):
        print("super class method called")
class Derivedclass1(Superclass):
    def derived1_method(self):
        print("Derived class 1 method called")
class Derivedclass2(Derivedclass1):
    def derived2_method(self):
       print("Dervied class 2 method called")

d = Derivedclass2()
d.super_method()
d.derived1_method()
d.derived2_method()

