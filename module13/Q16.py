
# Write a Python program to skip 'banana' in a list using the continue
# statement. List1 = ['apple', 'banana', 'mango']

list  = ["apple","banana","mango"]

for fruti in list:
    if fruti == "banana":
        continue
    print(fruti)
    


# Write a Python program to stop the loop once 'banana' is found using the break statement..


List1 = ['apple', 'banana', 'mango', 'orange']

for fruit in List1:
    if fruit == 'banana':
        break  
    print(fruit)

