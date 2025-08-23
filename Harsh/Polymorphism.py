
# Polymorphism :- Operator overloading

# when the same operator is allowed to have different meaning according to the context..

# class Complex:
#     def __init__(self, real ,img):
#         self.real  = real
#         self.img  = img


#     def showNumber(self):
#         print(self.real, " +", self.img,"j")

#     def add(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return complex(newReal,newImg)

# num1 = complex(1,3)
# print(num1)

# num2 = complex(4,6)
# print(num2)

# print(num1 + num2)
# num3 = num1.add(num2)
# print(num3)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
c1 = Circle(21)
print(c1.area)
print(c1.radius)
        