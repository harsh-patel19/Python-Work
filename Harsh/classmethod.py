
# class Method :- A class method is bound to class & receives the class as an implicit first argument.

class Person:
    name = "anonymous"

    @classmethod
    def changeName(self, name):
        # Person.name = name
        self.name = name

p1 = Person()
p1.changeName("Harsh Patel")
print(p1.name)
print(Person.name)