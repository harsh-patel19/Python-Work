#  Write a Python program to update a value at a particular key in a
# dictionary.


# Original dictionary
employee = {
    "name": "Emma",
    "position": "Developer",
    "salary": 50000,
    "location": "Delhi"
}

print("Before Update:")
print(employee)

# Update the value of the 'salary' key
employee["salary"] = 60000

# Update the value of the 'location' key
employee["location"] = "Mumbai"

# print("\nAfter Update:")
print(employee)
