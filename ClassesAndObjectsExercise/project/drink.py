from project.product import Product
from project.constants import DRINK_QUANTITY


class Drink(Product):
    def __init__(self, name):
        super().__init__(name, DRINK_QUANTITY)