# Write a Python program to read a file and print the data on the console.

filename = "output.txt"

try:
    with open(filename,"r") as file:
        print("File contents:\n")
        for line in file:
            print(line, end="")

except FileNotFoundError:
    print(f"error: The file '{filename} was not found.")

except Exception as e:
    print(f"an error: {e}")