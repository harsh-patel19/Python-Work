
# Write a Python program to print custom exceptions..?

# Custom Exception class
class NegativeNumberError(Exception):
    def __init__(self, value, message="Number should not be negative"):
        self.value = value
        self.message = message
        super().__init__(self.message)

# Another Custom Exception
class ZeroNotAllowedError(Exception):
    def __init__(self, message="Zero is not allowed"):
        self.message = message
        super().__init__(self.message)

# Function that raises custom exceptions
def check_number(num):
    if num < 0:
        raise NegativeNumberError(num)
    elif num == 0:
        raise ZeroNotAllowedError()
    else:
        print(f"Valid number: {num}")

# Main program
try:
    n = int(input("Enter a number: "))
    check_number(n)
except NegativeNumberError as e:
    print(f"Custom Exception: {e.message} -> {e.value}")
except ZeroNotAllowedError as e:
    print(f"Custom Exception: {e.message}")
except Exception as e:
    print(f"General Exception: {e}")
