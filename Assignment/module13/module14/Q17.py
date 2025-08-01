# Write a Python program to convert two lists into one
# dictionary using a for loop. 


keys = ["name","age","city"]
values = ["Patel",22,"London"]

my_dict = {}

for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print("combind dictionary:")
print(my_dict)

