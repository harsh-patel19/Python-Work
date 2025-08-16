
# class Student():
#     def display(self):
#         print(self.id,self.name)


# s1 = Student()
# s1. id =20
# s1.name ="Harsh"
# s1.display()

# s2 = Student()
# s2. id =20
# s2.name ="Hardik"
# s2.display()

# s3 = Student()
# s3.display()


# ************************ CONSTRUCTOR **********************



# class Emp():
#     def __init__(self,id,name,email):
#         self.id = id
#         self.name = name
#         self.email = email

#     def display(self):
#         print(self.id,self.name,self.email)

#     # def test(self):
#     #     print(self.id)

# e1 = Emp(10,"Harsh","Harsh@123")
# e1.display()
# # e1.test()












# class Animal():
#     def __init__(self,name,color,weight):
#         self.name = name
#         self.color = color
#         self.weight = weight

#     def display(self):
#         print(self.name,self.color,self.weight)

# d1 = Animal("Tiger","blue",125)
# d1.display()

    
# **************************** CONSTUTOR OVERLOADING *************

# class Emp:
#     def __init__(self,*a):
#         sum = 0
#         for i in a:
#             sum += i
#         print(sum)
    

# e1 = Emp(10,20)
# e2 = Emp(10,20,30)
# e3 = Emp(10,20,30,40,50,60,70,80,90,100)



class Test:

    clg = "VNSGU"

    def __init__(self,id,name):
        self.id = 45
        self.name = "abc"


    def disp(self):
        print(self.id,self.name,self.clg)

    # # instance method
    def display(self):
        self.id = 45
        self.name = "abc"
        print("self calling...")
    
    #classmethod
    @classmethod
    def run(cls):
        cls.id = 50
        cls.clg = "abc"
        print(cls.id,cls.clg)

#     #staticmethod
    # @staticmethod
    # def sample():
    #     print("Hello...sample calling")

# t1 = Test()
# t1.display()

# Test.run()
# Test.sample()

# t4 = Test(10,"harsh")
# Test.clg = "Tapi clg"
# t4.disp()

# t5 = Test(20,"lalit")
# t5.disp()


# t5 = Test(20,"xyz")
# t5.disp()

# Test.run()