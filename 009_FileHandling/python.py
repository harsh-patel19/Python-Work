f=  open("sample.txt","w")
f.write("hey python harsh here he was learning the programming..")
f.close()

# f = open("sample.txt","r")
# data = f.read()
# print(data)

f = open("sample.txt","r")
data = f.readlines()
print(data)