
number = 12
flag = 0
for i in range(2,number):
    if number%i==0:
        flag = 1
        break
if flag==0:
    print("prime***")
else:
    print("not prime**") 


# number = 19
# flag = 0
# for i in range(1,number):
#     if number%i ==0:
#         flag = 1
#         break
#     if flag ==0:
#         print("prime")
#     else:
#         print("not prime")


