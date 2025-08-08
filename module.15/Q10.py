# Write a Python program to demonstrate handling multiple exceptions.

def multiple_exception_demo():
    try:
        print("Multiple Exception Handling Demo")

        a = input("Enter first number: ")
        b = input("Enter second number: ")

        a = int(a)
        b = int(b)

        result = a/b 
        print(f"The result of {a} / {b} is : {result}")

    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print(e)
    except TypeError as e:
        print(e)

multiple_exception_demo()