

# Write a Python program to create a calculator using functions.

def add(a,b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return
    return a / b

print("simple calculator")
print("select operation:")
print("1. Add")
print("2. subtract")
print("3. multiply")
print("4. Divide")

choice = input("Enter Your choice number: ")

num1 = float(input("Enter first number: " ))
num2 = float(input("Enter second  number: " ))


if choice =="1":
    print("result:", add(num1, num2))

elif choice =="2":
    print("result:", subtract(num1, num2))

elif choice =="3":
    print("result:", multiply(num1, num2))

elif choice =="4":
    print("result:", divide(num1, num2))

else:
    print("Invalid choice")