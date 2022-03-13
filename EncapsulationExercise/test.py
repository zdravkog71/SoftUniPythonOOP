class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "I'm animal"

animal = Animal("zdr", 12)
print(type(animal))
message = repr(animal)
message.extend(" Zdravko")
if type(animal).__name__ == "Animal":
    print("good")
else:
    print("not good")

print(message)