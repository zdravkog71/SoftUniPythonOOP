from Inheritance.projectPerson.person import Person
from Inheritance.projectPerson.employee import Employee

class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."


shu = Teacher()
print(shu.get_fired())