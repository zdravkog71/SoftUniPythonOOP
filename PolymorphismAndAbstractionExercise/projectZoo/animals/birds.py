from PolymorphismAndAbstractionExercise.projectZoo.animals.animal import Bird
from PolymorphismAndAbstractionExercise.projectZoo.food import Meat, Vegetable, Fruit


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return f"Hoot Hoot"

    def feed(self, food):
        if type(food) == Meat:
            self.weight += (food.quantity * 0.25)
            self.food_eaten += food.quantity
            return
        return f"Owl does not eat {type(food).__name__}!"

class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.weight += (food.quantity * 0.35)
        self.food_eaten += food.quantity


hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)