
# import re

# k = re.match("a.b","fadbdfdfacb")
# k = re.search("a.b","fadbdfdfacb")
# k = re.findall("a.b","fadbdfdfacb")

# k = re.match("^Hello","Hello python")
# k = re.match("python","Hello python")

# k = re.search("ab*c","dffdfsabbbbbcdfds")
# k = re.search("a+c","dfffdfsaaaaacbbbbcdfds")

# k = re.match("^[a-z]{10}$","xccabcdffd")

# email = input("enter email: ")
# k = re.search("^[a-zA-Z0-9_-]+[a-z]+\\.[a-z]+\\.[a-z]{2,4}$",email)

# if k is None:
#     print("Invaild email")
# else:
#     print("valid")

# print(k)


# import re 
# txt = "the rain in spain"
# x = re.search("\s", txt)

# print("the first white-space character is located in position:",x.start())

# txt = "the rain in spain"
# x = re.split("\s",txt)
# print(x)

# txt = "The rain in spain"
# x = re.sub("\s","9","txt")
# print(x)

# txt = "the rain in spain"
# x = re.search("ai",txt)
# print(x)




import re
# k = re.match("a.b","hgsshgsacb")
# k = re.search("a.b","fadbjgjgacb")
k = re.findall("a.b","fadbjgjgacb")
print(k)


