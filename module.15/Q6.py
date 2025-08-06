#) Write a Python program to create a file and print the string into the
#file.

filename = "output.txt"
texttowrite = "Hello, this is a test string written to the file."

try:
    with open(filename,"w") as file:
        file.write(texttowrite)
    print(f"string sucessfully written to '{filename}'.")

except Exception as e:
    print(f"AN eoor occurred: {e}")