
# ************** CLASS AND OBJECT(OOPS CONCEPTS) ************


# Write a Python program to create a class and access its properties using an objec



class Student:
    def __init__(self,name,age,grade):
        self.name = name 
        self.age = age 
        self.grade = grade

    def display_info(self):
        print(f"name :{self.name}")
        print(f"Age: {self.age}")
        print(f"grade : {self.grade}")


Student1 = Student("Harsh",19,"A")

print("Name:", Student1.name)
print("Age:", Student1.age)
print("Grade:", Student1.grade)

Student1.display_info()
        