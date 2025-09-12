
class MyException(Exception):
    def __init__(self,message):
        super().__init__(message)

class demo:
    def agecheck(self,age):
        if age < 18:
            raise MyException("Invaild Age..")
        
d = demo()
d.agecheck(19)