

# inheritance :- When one class(child/derived) derives the properties & methods of another class(parent/base).BaseException

# class Car:
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class Toyota(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = Toyota("fortuner")
# car2 = Toyota("prius")

# print(car1.name)


# # TYPES : -   *SINGLE
# #             *MULTI-LEVEL
# #             *MULTIPLE


# # Super Method :-
# # super()method is used to access methods of the parent class.

# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped..")

    
# class Toyatacar(Car):
#     def __init__(self, type, name):
#         super().__init__(type)
#         self.name = name
#         super().start()
        

# car1 = Toyatacar("prius", "electric")
# print(car1.type)


# class Animal:
#     def __init__(self, name):
#         self.name = name 

#     def speak(self):
#         print(f"{self.name} make a sound")

# class Dog(Animal):
#     def speak(self):
#       print(f"{self.name} says Woof!")

# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name}says Meow!")


# a1 = Dog("tommmy")
# a1.speak()

# a2 = Cat("poppy")
# a2.speak()




