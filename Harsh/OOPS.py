

# class Student:
#     college_name = "ABC college"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("Welcome student", self.name)
        
    
#     def get_marks(self):
#         return self.marks
    
# s1 = Student("Harsh",100)
# s1.welcome()
# print(s1.get_marks())

# Create students class that takes name & marks of 3 subjects as argument in constructor..?

class Student:
    
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")


    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("HII",self.name, "Your avg score is:",sum/3) 

s1 = Student("Dhruvika", [100,99,98])
s1.get_avg()
        
       
s1.name = "Harsh"
s1.get_avg()
s1.hello()