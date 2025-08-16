
class Animal:
    
    def __init__(self):
        print("animal class calling...")


    def voice(self):
        print("animal voice ...")


class Dog(Animal):
       
    def voice(self):
        print("wow...wow")


class cat(Animal):
     
    def voice(self):
        print("auhh..auhhh")


d = Dog()
c = cat()

d.voice()
c.voice()