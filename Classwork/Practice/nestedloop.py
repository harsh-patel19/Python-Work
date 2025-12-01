#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *
#  * * * * *

# for i in range (1,6):
#     for j in range(1,6): 
#       print("*",end=" ")
#     print()


# *
# * *
# * * *
# * * * *
# * * * * *

# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1): #1, 1+1 ,1+2,1+3
#       print("*",end=" ")
#     print()                #new line


# * * * *
# * * *
# * *
# *

# n = 4
# for i in range(n,0,-1):
#   for j in range(i):
#     print("*",end=" ")
#   print()

# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 50




# * 
# * * 
# * * *
# * * * *
# * * * * *
# * * * * * *
 


# for i in range(7):
#     for j in range(i+1):
#      print("*" ,end=" ")
#     print()


# * * * * * * * 
# * * * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 


# for i in range(7):
#    for j in range(i,7):
#        print("*",end=" ")
#    print()

#         * 
#       * * 
#     * * *
#   * * * *
# * * * * *

# for i in range(5):
#     for j in range(i+1,5):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# * * * * * 
#   * * * * 
#     * * *
#       * *
#         *

# for i in range(5):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i,5):
#         print("*",end=" ")
#     print()
 
# for i in range(5):
#     for j in range(i,5):
#        print(" ",end=" ")
#     for j in range(i+1):
#        print("*",end=" ")
#     for i in range(i):
#        print("*",end=" ")  
#     print()



# for i in range (5):
#     for j in range(i+1):         
#         print(" ",end=" ")
#     for j in range(i+1,5):
#         print("*",end=" ")
#     for j in range(i,5):
#         print("*",end=" ")
#     print()


# for i in range(5):         
#     for j in range(i+1): # increment
#         print(" ",end=" ") 
#     for j in range(i+1,5): #decerment ,value
#         print("*",end=" ")
#     for j in range(i,5):   #decerment
#         print("*",end=" ")
#     print()
   
# LETS SEE HOW TO PRINT THR RIGHT TRIANGLE PATTERN OF NUMBERS.

# rows = 6

# for i in range(1, rows):
#     num = 1
#     for j in range(rows, 0, -1):
#         if j > i :
#             print(" ",end=" ")
#         else:
#             print(num, end=" ")
#             num += 1
#     print("")


# word ="python"
# x =""
# for i in word:
#     x += i
#     print(x)

# rows = 5
# for i in range(0,rows +1,1):
#     for j in range(i+1,rows+1,1):
#         print(j, end=" ")
#     print()

def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)

show(3)