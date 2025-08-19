
# Write a Python program to show method overloading?


from multipledispatch import dispatch

class Calculator:

    @dispatch(int,int)
    def add(self, a,b):
        print(a + b)

    @dispatch(int, int, int)
    def add(self, a,b,c):
        print(a + b + c)

    @dispatch(float,float)
    def add(self, a,b):
        print(a + b)

calc = Calculator()
calc.add(5,10)
calc.add(5,10,15)
calc.add(2.5, 3.5)

