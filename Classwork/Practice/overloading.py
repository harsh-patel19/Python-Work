

# class Shape:
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length ,breadth):
#         self.lenght = length
#         self.breadth = breadth

#     def area(self):
#         return self.lenght * self.breadth

# class Circle(Shape):
#     def __init__(self, radius):
#        self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius
    
#     def area(self, diameter):
#         self.radius = diameter / 2
#         return 3.14 * self.radius *self.radius

# r = Rectangle(5,10)
# print("Area of rectangle:", r.area())
# c = Circle(7)
# print("Area of circlle with radius 7:", c.area())
# print("Area of circle with diameter 10:", c.area(10))




# class MyClass:
#     def my_method(Self, arg1, arg2=None):
#         if arg2:
#             print(arg1 + arg2)
#         else:
#             print(arg1)


# obj = MyClass()
# obj.my_method(10)

# obj.my_method(10,20)


# class Animal:
#     def speak(self):
#         print("Animal speaking..")

# class Dog(Animal):
#         def speak(self):
#             print("Dog barking..")
    
# obj = Dog()
# obj.speak()




# class parent:
#     def my_method(self,arg1,arg2):
#         print("Parent my_method")

# class child(parent):
#     def my_method(self, arg1):
#         print("child my_method")
# obj = child()
# obj.my_method("Hello")



class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive..")
        
    
class Boat:
    def __init__(self,brand,model):
        self.breand = brand
        self.model = model

    def move(self)        :
        print("sail..")

class plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("fly..")

car1 = Car("lember","mustang")
Boat1 = Boat("harsh","100")
plane1 = plane("boat","25")
        
for x in (car1,Boat1,plane1):
    x.move