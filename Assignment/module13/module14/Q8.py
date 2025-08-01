
# Write a Python program to create a tuple with multiple data types.

# Creating a tuple with multiple data types
mixed_tuple = (25, "Python", 3.14, True, None, [1, 2, 3], (4, 5), {'key': 'value'})

# Display the tuple
print("Tuple with multiple data types:")
print(mixed_tuple)

# Print the type of each element
print("\nType of each element in the tuple:")
for item in mixed_tuple:
    print(f"{item} --> {type(item)}")
