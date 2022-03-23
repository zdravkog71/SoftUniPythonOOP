from ClassesAndObjectsExercise.project.product import Product
from ClassesAndObjectsExercise.project.constants import DRINK_QUANTITY


class Drink(Product):
    def __init__(self, name):
        super().__init__(name, DRINK_QUANTITY)