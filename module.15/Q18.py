
# Write a Python program to show multilevel inheritance

class person:
    def display_person(self):
        print("I am a person")

class Employee(person):
    def display_employee(self):
        print("I am an Employee")

class Manager(Employee):
    def display_Manager(self):
        print("I am a manager")

obj = Manager()
obj.display_person()
obj.display_employee()
obj.display_Manager()



