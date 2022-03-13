from EncapsulationExercise.projectFood.product import Product


class Beverage(Product):
    def __init__(self, name, price, milliliters):
        self.__milliliters = milliliters
        super().__init__(name, price)

    @property
    def milliliters(self):
        return self.__milliliters

    @milliliters.setter
    def milliliters(self, value):
        self.__milliliters = value