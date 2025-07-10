a = int(input("enter the number:"))

rem =''
while a > 0:
    rem = str(a % 2) + rem 
    a //= 2
print(rem)