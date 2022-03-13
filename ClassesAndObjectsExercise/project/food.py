from project.product import Product
from project.constants import FOOD_QUANTITY


class Food(Product):
    def __init__(self, name):
        super().__init__(name, FOOD_QUANTITY)