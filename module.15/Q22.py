
# **** METHOD OVERLOADING AND OVERRIDING ****

# Write Python programs to demonstrate method overloading and method overriding.



#Method overloading...
class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c
    
calc = Calculator()

print("sum of 2 numbers:", calc.add(10,20))
print("sum of 3 numbers:", calc.add(10,20,30))
print("sum of 1 number:", calc.add(50))


#Method overriding...

class Animal:
    def sound(self):
        print("Animals make different sounds..")

class Dog(Animal):
    def sound(self):
        print("Woof Woof..")

animal = Animal()
dog = Dog()

animal.sound()
dog.sound()