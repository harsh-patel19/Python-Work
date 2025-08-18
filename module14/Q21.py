
#Write a Python program to print a string using a function

def tops_surat(message):
    print("The message is:",message)

tops_surat("Hello, welcome to pyhton in Tops Surat..")




#Write a Python program to create a parameterized function that takes two arguments and prints their
#sum.

def add_number(a, b):
    result = a + b 
    print("The sum of",a,"and",b,"is",result)

add_number(10,20)




# Write a Python program to create a lambda function with one expression

square = lambda x: x* x
print("The square of 10 is:",square(10))


# Write a Python program to create a lambda function with two expressions.

add = lambda x,y: x+y
print("The sum is:",add(10,15))

