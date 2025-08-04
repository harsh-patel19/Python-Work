# f = open("test.txt","w")
# f.write("This is my first file io practical")
# f.close()

# f = open("test.txt", "a")
# f.write("Hello Pyhton")
# f.close()

# f = open("test.txt","r")
# data = f.read()
# print(data)

# f = open("test.txt","r")
# data = f.readline()
# data1 = f.readline()
# print(data)
# print(data1)


# f = open("test.txt","r")
# while (True):
#     data = f.readline()
#     if data.startswith('P'):
#         print(data)
#     if not data:
#         break
# f.close()


# f = open("test.txt","r")
# data = f.readlines()
# print(data)
# f.close()

# with open("test.txt","w") as f :
#     f.writelines(["Test\n","Tech\n","pyhton"])

# with open('test.txt','r') as f : 
#     f.seek(5)
#     print(f.tell())
#     data = f.read()
#     print(f.tell())
#     print(data)

# with open("home.txt",'a+') as f:
#     f.write("\nHarsh, Patel")
#     f.seek(5)
#     data = f.read()
#     print(data)

# import json
# data = {"name":"Harsh Patel" ,"email":"Harsh@123.com","Phone":8487832287}
# l = ["Test","tech","pyhton"]
# with open("mydata.json","w") as f:
#    json.dump(l,f)


#get data form file if line in coains word'pyhton'..
#count words of each lines..