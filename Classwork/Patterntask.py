#  1. Reverse Half Pyramid Pattern (Right-Sided)

# *****
# ****
# ***
# **
# *

# n = 5
# for i in range(n):

for j in range(i+1):
        print('',end='')
    for j in range(i,n):
        print('*',end='')
    print()

for i in range(5):
    for j in range(i,5):
        print("*", end="")
    print()
# 2. Square Pattern

#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *

# for i in range(1,6):
#     for j in range(1,6):
#         print("*", end=" ")
#     print()
 
#3.Right Triangle Pattern

# * 
# * * 
# * * * 
# * * * * 
# * * * * *

# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# 4. Pyramid Pattern

#        * 
#       ***
#      *****
#     *******
#    *********

# n = 5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         print("*",end=" ")
#     print()

# 5. 
#     *
#    * *
#   * * *
#    * *
#     *


    #   *
    #  * *
    # *   *
    #  * *
    #   *
 


#7. Reverse Half Pyramid Pattern (Left-Sided)

# *****
#  ****
#   ***
#    **
#     *

# n = 5 
# for i in range(n,0,-1):
#     for j in range(0,n-i+1):
#         print(" ",end=" ")
#     for k in range(0,i):
#         print("*",end=" ")
# print()

#8. number pattern

# 1
# 12
# 123
# 1234
# 12345

# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#        print(j,end=" ")
#     print()


# 9 . Number Pattern 1

# 1
# 23
# 456
# 78910

# n = 4
# num =1
# for i in range(n):
#     for j in range(i + 1):
#          print(num, end=" ")
#          num += 1
#     print()
 
# 10 . 

# 5
# 45
# 345
# 2345
# 12345

# n = 5
# l = 1

# for i in range(n):
#     for j in range(i +1):
#        print(l,end=" ")


# 0
# 10
# 010
# 1010
# 01010


# n = 5
# print("*"*n)

