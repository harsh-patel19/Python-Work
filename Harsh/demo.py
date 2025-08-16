# ********************************** Basic *****************************************

# PYTHON PROGRAM TO CHECK IF A NUMBER IS A PALINDROME....?

# num = input("Enter a number: ")

# if num == num[::-1]:
#     print(f"{num} is a palindrome..")
# else:
#     print(f"{num} is not a palindrome..")


# LIST COMPREHNSION CHALLENGE....?
# GENRATE SQUARES USING LIST: -

# squares = [x**2 for x in range(1,11)]
# print(squares)


# ARMSTORNG NUMBER CHECKER....?

# def is_armstrong(n):
#     num = str(n)
#     power = len(num)
#     return n == sum(int(digit) ** power for digit in num)
# print(is_armstrong(153))

# LAMBDA FUNCTION USAGE....?

# square = lambda x: x ** 2
# print(square(15))

# FIZZBUZZ IMPLEMENTATION....?

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FIzzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# MAP FUNCTION IMPLEMENTATION....?
# using map () to double values in a list

# nums = [1,2,3,4]
# dobled =list(map(lambda x: x * 2, nums))
# print(dobled)


# ********************************** Advanced *****************************************

# CHARACTER FREQUENCY IN A STRING....?

# def char_frequency(text):
#     freq = {}
#     for char in text.lower():
#         freq[char] = freq.get(char, 0) + 1
#     return freq
# print(char_frequency("Hello world"))


# REVERSE WORDS IN A SENTENCE....?

# def reverse_words(sentence):
#     words = sentence.split()
#     reverse_words = [word[:: -1] for word in words]
#     return" ".join(reverse_words)
# print(reverse_words("Hello world"))


# COMMON ELEMEMNTS OF TWO LISTS....?

# list1 = [1,2,3,4]
# list2 = [3,4,5,6]
# print(list(set(list1) & set(list2)))

# ITERATE OVER A DICTIONARY....?

# fruits = {"apple": 2, "banana": 3, "cherry": 1}
# total_quantity = 0
# for fruit, quantitly in fruits.items():
#     print(fruit, quantitly)
#     total_quantity += quantitly
# print("total:", total_quantity)

# REMOVE DUPLICATES....?

# my_list = [1,2,3,4,2,5,3,6,3]
# from collections import Counter
# count = Counter(my_list)
# duplicates = {item: freq for item, freq in count.items() if freq > 1}



# ********************************** INTERMEDIATE *****************************************

# FILTER FUNCTION USAGE...?
# filter even numbers using filter()

# nums = [1,2,3,4,5,6]
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)

# REMOVE DUPLICATES FROM LIST...?

# duplist = [1,2,3,4,5,5,4]
# uniqe_list = list(set(duplist))
# print(uniqe_list)

# VOWEL COUNTER...?

# def count_vowels(s):
#     return sum(1 for char in s.lower() if char in "aeiou")
# print(count_vowels("Hello World"))

# ANAGRAM CHECHER...?

# def check_anagram(s1, s2):
#     return sorted(s1.lower() == sorted(s2.lower()))
# print(check_anagram("listen", "silent"))

# MISSING NUMBER FINDER...?

# def find_misiing(nums, n):
#     return n *(n +1) // 2 -sum(nums)
# print(find_misiing([1,2,4,5], 5))

# ********************************** EXPERT *****************************************

# PRINT PYRAMID PATTERN ...?

# n = 5
# for i in range(1, n + 1):
#     print(" " *(n-i) + "*" * (2 * i-1))

# SECOND LARGEST ELEMENT...?

# def second_largest(nums):
#     nums = list(set(nums))
#     nums.sort(reverse=True)
#     return nums[1] if len(nums) > 1 else None
# print(second_largest([10,20,30,50,40]))

# NUMBER REVERSAL...?

# def reverse_number(n):
#     reversed_num = 0
#     while n > 0:
#         digit = n % 10
#         reversed_num = reversed_num * 10 +digit
#         n = n // 10
#     return reversed_num
# print(reverse_number(10203040))

# TWO SUM PROBLEM...?

