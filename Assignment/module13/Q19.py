
# Write a Python program to apply the map() function to square a list of numbers..

numbers = [10,20,30,40,50]
squared_numbers = list(map(lambda x: x **2, numbers))

print(numbers)
print(squared_numbers)



# Write a Python program that uses reduce() to find the product of a list of numbers..

from functools import reduce

numbers = [10,20,30,40,50]
multiply = reduce(lambda x,y: x* y, numbers)

print(multiply)

# Write a Python program that filters out even numbers using the filter() function..

numbers = [1,2,3,4,5]
odd_numbers = list(filter(lambda x: x%2 != 0, numbers))

print(odd_numbers)