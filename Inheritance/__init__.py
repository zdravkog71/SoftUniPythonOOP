class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Child(Parent):
    def __init__(self, name, age, alone):
        Parent.__init__(self, name, age)
        self.alone = alone



tom = Child("zdr",17,True)
print(tom.alone)

