

# Write a generator function that generates the first 10 even numbers..

def gernrate_Even():
    num = 2
    count = 0
    while count < 10:
        yield num 
        num += 2
        count +=1

for even in gernrate_Even():
    print(even)


# Write a Python program that uses a custom iterator to iterate over a list of integers.
