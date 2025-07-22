
from functools import reduce

# reduce(function, iterable)

# def add(x,y):
#     return x + y

# numbers = [1,2,3,4,5]
# result = reduce(add, numbers)
# print("sum:", result)

# # Multiply all numbers

# def multiply(x,y):
#     return x *y

# numbers = [2,3,4]
# result = reduce(multiply, numbers)
# print("product:", result)


# numbers =[1,2,3,4,5]
# result = reduce(lambda x,y: x + y, numbers)
# print("sum:", result)

# #FIND THE MAXIMUM NYMBER USING REDUCE() AND LAMBDA.....

# numbers = [5,3,8,6,2]
# max_value =reduce(lambda x,y: x if x>y else y, numbers)
# print("maximum:", max_value)


# Using a regular function with reduce():

# def get_max(x,y):
#     return x if x>y else y
# numbers = [10,20,30,40,50]

# maximum = reduce(get_max, numbers)
# print("maximum numbers is:", maximum)

# # Using a lambda function with reduce():

# numbers = [10,20,30,40,50]
# maximum = reduce(lambda x,y: x if x>y else y, numbers)
# print(maximum)





# Find the longest word in a list..

# words = ["cat","elephant","tiger","lion"]

# longest =reduce(lambda x,y :x if len(x) > len(y) else y, words)
# print("Longest word:", longest)

# # Find product of all even numbers in a list..

# numbers = [1,2,3,4,5,6,7,8]
# even_numbers = list(filter(lambda x: x%2 ==0,numbers))
# p = reduce(lambda x,y : x* y, even_numbers)
# print("p:",even_numbers)

# # Concatenate all strings in a list..

# words = ["python","is","awesome"]
# sentence = reduce(lambda x,y: x+""+ y, words)
# print("sentence:", sentence)

# #Count total characters in list of words..

# words = ["HELLO","HARSH","PATEL"]
# total_chars = reduce(lambda x,y:x +len(y),words,0)
# print("Total characters:",total_chars)

# # Find the smallest number in a list..

# numbers = [1,2,3,4,5,6,7,8]
# minimum = reduce(lambda x,y: x if x<y else y ,numbers)
# print("minimum numbers:", minimum)

# # Sum of squares..
# numbers = [1,2,3,4]
# number_sum = reduce(lambda x,y:x+y**2, numbers)
# print(number_sum)

# #Combine first letters of each word..

# words = ["hello", "world", "python", "rocks"]
# lettters = reduce(lambda x,y: x +y[0], words," ")
# print(lettters)

# Find the longest string (manually input)
# Ask the user to enter a list of strings, and use reduce() to find the longest string..

# user_input = input("Enter Words separated by space: ")
# words = user_input.split()
# longest = reduce(lambda x,y: x if len(x) > len(y) else y, words)
# print("Longest word is:", longest)


# Product of numbers excluding 0 Use reduce() and lambda to multiply only non-zero numbers..

# numbers = [1,0,3,4,5]
# non_zeronumbers = list(filter(lambda x: x != 0, numbers))

# output = reduce(lambda x,y :x*y,non_zeronumbers)
# print(output)


# Given a list of digits, join them using reduce() to form a full number..

# digits = [1,2,3,4]
# number = reduce(lambda x,y: x*10 + y, digits)
# print(number)

# Step 1: 1 * 10 + 2 = 12

# Step 2: 12 * 10 + 3 = 123

# Step 3: 123 * 10 + 4 = 1234



