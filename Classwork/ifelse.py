
#marks =50
marks = int(input("Enter value:"))
if marks>90 and marks<=100:
    print("A")
elif marks>70 and marks<=90:
    print("B")
elif marks>50 and marks<=70:
    print("c")
elif marks>35 and marks<=50:
    print("d")
elif marks>=0 and marks<=35:
    print("f")
else :
    print("invaild marks")
