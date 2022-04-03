from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, weight, food_eaten = 0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        self.wing_size = wing_size
        super().__init__(name, weight)

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        self.living_region = living_region
        super().__init__(name, weight)

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"