# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input.\


# FILE HANDLE EXCEPTIONS...
def simple_calculator():
    print("...Welcomw to the simple Calculator...")
    print("operations: +, -, *, /")

try:
    num1 = float(input("Enter a First number: "))
    num2 = float(input("Enter a secound number: "))

    operators = input("Enter operator (+, - , *, /): ")
    if operators == "+":
        result  = num1+num2
    elif operators == "-":
        result = num1-num2
    elif operators == "*":
        result = num1*num2
    elif operators == "/":
        if num2 == 0:
            raise ZeroDivisionError("cannot divide by zero")
        result = num1 / num2
    else:
        raise ValueError("Invalid operator entered")
    print(f"result: {result}")

except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
    
simple_calculator()