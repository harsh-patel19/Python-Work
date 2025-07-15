
# Write a Python program to find a specific string in the list using a simple
# for loop and if condition.


List1 = ['apple', 'banana', 'mango']
a  = input("Enter the fruit to search: ")


found = False

for fruit in List1:
    if fruit == a:
        print("a, found in list!")
        found = True
        break

if not found:
    print("not found the list")



