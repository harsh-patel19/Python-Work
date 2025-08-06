# Write a Python program to open a file in write mode, write some text, and then close it?


# open the file in write mode
file = open("example.txt", "w")


# write some text to the file
file.write("Hello, this ia a file.")
file.write("we are writing text using python.")

# close the file
file.close()
