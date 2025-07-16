
#  Write a Python program to count how many times each
# character appears in a string.

# Program to count character frequency in a string

# Input from user
input_string = input("Enter a string: ")

# Create an empty dictionary to store character counts
char_count = {}

# Loop through each character in the string
for char in input_string:
    if char in char_count:
        char_count[char] += 1  # Increment count if character already exists
    else:
        char_count[char] = 1   # Initialize count if character appears first time

# Print the result
print("Character frequency:")
for char, count in char_count.items():
    print(f"'{char}': {count}")
