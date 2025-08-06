# Write a Python program to read the contents of a file and print them on the console?

filename = "sample.txt"
try: 
    with open(filename,"r") as file:
        contents = file.read()
        print("File contents:\n")
        print(contents)

except FileNotFoundError:
    print(f"Error: the file '{filename}'' was not found")

    
