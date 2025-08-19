
# class A :
#     def display(self):
#         print("running display of class A")


# class B:
#     def display(self):
#         print("running display of class B")

# b = B(A)
# b.display()

# class A:
#     def __init__(self,id,name):
#         self.id = id
#         self.name = name 

#     def display(self):
#         print(self.id,self.name)

# class B(A):

#     def __init__(self, id, name,phone):
#         super().__init__(id, name)
#         self.phone = phone
#     def sample(self):
#         print(self.id,self.name,self.phone)


# b = B(20,"Harsh","0133456789")
# b.sample()



# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def display_info(self):
#         print(f"car: {self.brand}, model: {self.model}")


# car1 = Car("hasss","patel")
# car1.display_info()



# single inheritance

# class Animal:
#     def sound(self):
#         print("Animals make sounds")

# class Dog(Animal):
#     def sound(self):
#         print("DOg barks")

# d = Dog()
# d.sound()


# Multilevel inheritance

# class vehicle:
#     def show_type(self):
#         print("This is a vehicle")

# class car(vehicle):
#     def show_car(self):
#         print("This is a car")

# class Electriccar(car):
#     def show_electric(self):
#       print("This is electric car")

# e = Electriccar()
# e.show_type()
# e.show_car()
# e.show_electric()


#  Multiple inheritance

class Father:
    def skill(self):
        print("knows Driving")

class Mother:
    def skill(self):
        print("knows Cooking")

class child(Father,Mother):
    def skill(self):
        print("child programming")

c = child()
c.skill()