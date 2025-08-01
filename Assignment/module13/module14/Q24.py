

# Write a Python program to generate random numbers using the random module..

import random

# Generate a random integer between 1 and 100
random_integer = random.randint(1, 100)
print(f"Random Integer (1 to 100): {random_integer}")

# Generate a random float between 0 and 1
random_float = random.random()
print(f"Random Float (0 to 1): {random_float}")

# Generate a random float between a specific range
random_uniform = random.uniform(10, 50)
print(f"Random Float (10 to 50): {random_uniform}")

# Generate a random number from a list
sample_list = [10, 20, 30, 40, 50]
random_choice = random.choice(sample_list)
print(f"Random Choice from list: {random_choice}")
