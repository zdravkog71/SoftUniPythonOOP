from PolymorphismAndAbstractionExercise.projectZoo.animals.animal import Mammal
from PolymorphismAndAbstractionExercise.projectZoo.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if type(food) == Vegetable or type(food) == Fruit:
            self.weight += (food.quantity * 0.1)
            self.food_eaten += food.quantity
            return
        return f"Mouse does not eat {type(food).__name__}!"

class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if type(food) == Meat:
            self.weight += (food.quantity * 0.4)
            self.food_eaten += food.quantity
            return
        return f"Dog does not eat {type(food).__name__}!"

class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if type(food) == Vegetable or type(food) == Meat:
            self.weight += (food.quantity * 0.3)
            self.food_eaten += food.quantity
            return
        return f"Cat does not eat {type(food).__name__}!"

class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if type(food) == Meat:
            self.weight += food.quantity
            self.food_eaten += food.quantity
            return
        return f"Tiger does not eat {type(food).__name__}!"