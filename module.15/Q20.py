
# Write a Python program to show hybrid inheritance.?

class person:
    def show_details(self):
        print("I am a person")

class student(person):
    def student_info(self):
        print("I am a student")

class Teacher(person):
    def teacher_info(self):
        print("I am a teacher")

class TeachingAssistant(student,Teacher):
    def assistant_info(self):
        print("I am a teaching Assistant (student + Teacher role)")

s = student()
s.show_details()
s.student_info()

