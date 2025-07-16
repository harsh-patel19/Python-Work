
# Write a Python program to separate keys and values from a dictionary using
# keys() and values.

car = {
    "brand": "Tesla",
    "Model": "Y",
    "Year" : 2025,
    "color": "Red"
}

# separate keys and values
keys = car.keys()
values = car.values()


print("keys in the dictionary: ")
print(keys)

print("\nvalues in the dictionary:")
print(values)