from multipledispatch import dispatch

class Calc:

    # @dispatch(int,int)
    @dispatch(int,int)
    def add(self,a,b):
        print(f"addition is {a+b}")

    @dispatch(int,int,int)
    def add(self,a,b,c):
        print(f"additon is {a+b+c}")

    @dispatch(float,int)
    def add(self,a,b):
        print(f"addition is {a+b}")

    # def add(self,*a):
    #     sum = 0
    #     for i in a:
    #         sum += i
    #     print(f"addition is {sum}")

c = Calc()
c.add(10,20)
c.add(10,20,30)
c.add(10.02,3)