# Write a Python program to create a file and write a string into it.

file = open("myfile.txt", "w")
text = "This is a python programming in tops surat."
file.write(text)
file.close()

with open("myfile.txt","w") as file:
    file.write("This is a pyhton programming in tops surat")