from abc import ABC,abstractmethod


class bardoli(ABC):
    student = "vidhyabharti trust collge"

    @abstractmethod
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        return f"{self.name,self.id}"
    
s1 = bardoli("Umrakh",20)
s1.display()
print(bardoli)