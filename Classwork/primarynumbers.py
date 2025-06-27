
# PRINT NUMBERS FORM 1 TO 100 IN PRIMR NUMBERS IN USING RANGE ...

for i in range (1,101):
    for j in range (2,i):
        if i % j ==0:
            break
    else:
        print(i)
