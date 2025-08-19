
# Write a Python program to demonstrate the use of super() in inheritance.

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        print("Person constructor called")

    def show_deatils(self):
        print(self.name,self.age) 

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.students_id = student_id
        print("Student constructor called..")

    def show_deatils(self):
        super().show_deatils()
        print(self.students_id)

Student1 = Student("Harsh", 21, "ST123")
print("---student deatils---")
Student1.show_deatils()
