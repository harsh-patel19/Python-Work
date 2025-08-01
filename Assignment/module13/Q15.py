
# Write a Python program to print "Hello" using a string..
def function(meassge):
    print("Hello",meassge)
function("world")


# Write a Python program to allocate a string to a variable and print it..
my_string = "WELOCME TO PYHTON PROGRAMMING!"
def print_mesaasge():
    print(my_string)
print_mesaasge()


# Write a Python program to print a string using triple quotes..
def print_multiline_message():
    message = """" HELLO HARSH 
    WHO ARE YOU ?
    WHAT ARE YOU DOING ?
    """
    print(message)
print_multiline_message()


# Write a Python program to access the first character of a string using index value..
text = "python"
first_char =text[0]
print(first_char)


# Write a Python program to access the string from the second position onwards using slicing..
text = "Python"
sliced_text = text[1:]
print("String from second position onwards:", sliced_text)


#  Write a Python program to access a string up to the fifth character..
text = "Python"
sliced_text = text[:5]
print("String from fifth position onwards:", sliced_text)


# Write a Python program to print the substring between index values 1 and 4..
text ="pythonprogramming"
substring = text[1:4]
print(substring)

# Write a Python program to print every alternate character from the string starting from index 1..
text ="pythonprogramming"
substring = text[1::2]
print(substring)

