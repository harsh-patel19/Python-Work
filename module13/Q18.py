
# Write a Python program that manipulates and prints strings using various string methods.

text = "Hello, world! welcome to python programming."

print("original string:")
print(text)

# remove leading and trailing spaces
stripped = text.strip()
print("n\After strip():")
print(stripped)

replaced = stripped.replace("python", "java")
print("\nAfter replace():")
print(replaced)

position = stripped.find("welcome")
print("\nposition of 'welsome':", position)