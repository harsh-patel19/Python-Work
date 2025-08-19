
# Write a Python program to demonstrate the use of local and global variables in a class.


# Global variable
x = 100

class Demo:
    #class variable
    class_var = "I am a class variable"

    def __init__(self, value):
        self.value = value
        
    def show_variables(self):
        local_var = "I am local to this method"

obj = Demo(50)
obj.show_variables()