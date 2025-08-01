
# • Write a Python program to create a function that takes a string as input and prints it.

# def print_string(text):
#     print("You entered:", text)

# user_input = input("Enter a string: ")
# print_string(user_input)




# Write a Python program to create a calculator using functions..

# Define functions for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Main program
print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform calculation based on user choice
if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")
