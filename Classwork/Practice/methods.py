
# METHODS :-

# Methods are functions that belong to objects.

class Student:
    college_name = "ABC COLLEGE"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        # print("adding new student in Dtabase..")

    def welcome(self):
        print("welcome student", self.name)

    def get_marks(self):
        return self.marks
    
s1 = Student("Harsh", 100)
# print(s1.name)
s1.welcome()
print(s1.get_marks())
