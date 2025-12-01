
# # ******* OOPS IN PYTHON ******

# # -> TO MAP WITH REAL WORLD SCENARIOS,WE STARTED USING OBJECTS IN CODE.

# # THIS IS CALLED OBJECT ORINETEND PROGRAMMING.

# # class student:
# #     name ="Harsh"

# # s1 = student()
# # print(s1)

# # class student:
# #     name ="harsh"   ---->class

# # s1 = student()      ---->object
# # print(s1.name)

# # s2 = student()
# # print(s2.name)

# # class car:
# #     color ="blue"
# #     brand ="mercedes"

# # car1 = car()
# # print(car1.color)
# # print(car1.brand)

# # INIT FUNCTION 

# # constructor :
# # ALL clsses have a function called init(),which is always executed when the object is being initited.

# # class student:
# #     def __init__(self,fullname):
# #         self.name = fullname
    
# # class student :
# #     name ="Harsh patel"
# #     def __init__(self):
# #         print("adding new student in database..")

# # s1 = student()

# # class student:
# #     name ="patel"
# #     def __init__(self):
# #         print(self)
# #         print("adding new student in database")
# # s1 = student()

# # class student:
# #     college_name ="VNSGU SURAT"

# #     def __init__(self,name):
# #         self.name = name
# #         print("adding new student in database.")

# # s1 = student("Harsh")
# # print(s1.name)

# # s2 = student("Dhruvika")
# # print(s2.name)

       
# # class & instance Attributes

# # class student:
# #     college_name ="VNSGU SURAT"
    
# #     def __init__(self,name, marks):
# #         self.name = name
# #         self.marks = marks
# #         print("adding new student in database.")

# # s1 = student("Harsh",100)
# # print(s1.name, s1.marks)

# # s2 = student("Dhruvika",100)
# # print(s2.name, s2.marks)

# # print(s2.college_name)


# #METHODS 

# # *methods are functions that belong to objects.

# # class student:
# #  def __init__(self,name,marks):
# #     self.name = name
# #     self.marks = marks

# #  def welcome(self):
# #     print("welcome student",self.name)

# #  def get_marks(self):
# #     return self.marks

# # s1 = student("harsh",99)
# # s1.welcome()
# # print(s1.get_marks())


# #STATIC METHODS:

# # methods that don use the self parameters(work at class level)

# class student:
#     @staticmethod
#     def college():
#         print("ABC COLLEGE")

# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
    
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started..")
    
# car1 = car()
# car1.start()

