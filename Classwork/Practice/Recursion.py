
# WHEN A FUNCTION CALLS ITSELF REPEATEDLY.

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    
