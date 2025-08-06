#Write a Python program to read a name and age from the user and print a formatted output.

name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hello,{name} You are {age} yeras old.")

#Write a Python program to read a string, an integer, and a float from
#the keyboard and display them?

text = input("Enter a string: ")
number = int(input("Enter an interger: "))
decimal = float(input("Enter a float: "))

print(f"\nYou entered:")
print(f"string: {text}")
print(f"integer: {number}")
print(f"float: {decimal}")