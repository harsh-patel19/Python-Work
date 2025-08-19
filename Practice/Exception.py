
# try:
#     numerator = 10
#     deonminator = 0

#     result = numerator/deonminator

#     print(result)

# except:
#     print("Error: Denominator cannot be 0.")


# try:
#     even_numbers = [2,4,6,8]
#     print(even_numbers[10])

# except ZeroDivisionError:
#     print("cannot be 0.")

# except IndexError:
#     print("Index out of bound")


# try: 
#     num = int(input("Enter a number: "))
#     assert num % 2 == 0
# except:
#     print("Not an even number..")
# else:
#     reciprocal = 1/num
#     print(reciprocal)


# try:
#     numerator = 10
#     denominator = 0

#     result = numerator/denominator
    
#     print(result)
# except:
#     print("Error: Denominator cannot be 0.")

# finally:
#     print("This is finally block..")





# class InvalidAgeException(Exception):
#     pass

# number = 18

# try:
#     input_num = int(input("Enter a number: "))
#     if input_num < number:
#         raise InvalidAgeException
#     else:
#         print("Eligible to vote")

# except InvalidAgeException:
#     print("invalid age")




# class salarynotinrangeerror(Exception):
#     def __init__(self, salary, message = "salary is not in (5000, 15000) range"):
#         self.salary = salary
#         self.message = message
#         super().__init__(self.message)

# salary = int(input("Enter salary amount: "))
# if not 5000 < salary < 15000:
#     raise salarynotinrangeerror(salary)


class Cat:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def info(self):
        print("i am a cat")

    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print( f"I am Dog.. my name is {self.name}.i am {self.name} {self.age} yeras old.")

    def make_sound(self):
        print("Bark")

cat1 = Cat("dhruka",2.5)    
dog1 = Dog("harsh",4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()

