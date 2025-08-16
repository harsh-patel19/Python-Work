
class  A:

    def display(self):
        print("A : display calling..")

#single
class B(A):
    pass

#multilevel
# class C(B):
#     pass


#Hierachical [B&C]
class c(A):
    pass

# b = B()
# b.display()

# C = C()
# C.display()