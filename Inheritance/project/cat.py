from Inheritance.project.animal import Animal

class Cat(Animal):
    def meow(self):
        return "meowing..."



catty = Cat()
print(catty.eat())