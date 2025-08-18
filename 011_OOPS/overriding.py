
# class A :
#     def display(self):
#         print("running display of class A")


# class B:
#     def display(self):
#         print("running display of class B")

# b = B(A)
# b.display()

class A:
    def __init__(self,id,name):
        self.id = id
        self.name = name 

    def display(self):
        print(self.id,self.name)

class B(A):

    def __init__(self, id, name,phone):
        super().__init__(id, name)
        self.phone = phone
    def sample(self):
        print(self.id,self.name,self.phone)


b = B(20,"Harsh","0133456789")
b.sample()