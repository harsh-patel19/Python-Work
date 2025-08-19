
# Write Python programs to demonstrate different types of inheritance (single, multiple,
# multilevel, etc.

# 1. single inheritance
class A:
    def display_parent(self):
        print("This is the Parent class")

class B(A):
    def display_child(self):
        print("This is the child class")

obj = B()
obj.display_parent()
obj.display_child()



# 2. Multiple inheritance
class A:
    def display(self):
        print("This is Father")

class B:
    def display_m(self):
        print("This is Mother")

class C(A,B):
    def display_s(self):
        print("This is child")


obj = C()
obj.display()
obj.display_m()
obj.display_s()


# 3. Multilevel inheritance
class A:
    def display(self):
        print("This is Grandparent")

class B(A):
    def display_s(self):
        print("This is parent")

class C(B):
    def display_m(self):
        print("This is child")
        

obj = C()
obj.display()
obj.display_m()
obj.display_s()
       


# Hierarchical inheritance
class A:
    def display(self):
        print("This is parent")

class B1(A):
    def display_b1(self):
      print("This is child 1")

class B2(A):
    def display_b2(self):
        print("This is child 2")

obj1 =B1()
obj2 =B2()
       
obj1.display()
obj1.display_b1()

obj2.display()
obj2.display_b2()


# Hybrid inheritance

class A:
    def show_A(self):
        print("Class A")
class B(A):
    def show_B(self):
       print("Class B")
class C(A):
    def show_C(self):
        print("class c")
class D(B,C):
    def show_D(self):
        print("Class D")


obj = D()
obj.show_A()
obj.show_B()
obj.show_C()
obj.show_D()