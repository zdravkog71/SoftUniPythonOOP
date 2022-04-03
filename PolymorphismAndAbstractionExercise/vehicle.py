from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    SUMMER_FUEL_CONSUMTION = 0.9
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity - distance * (self.fuel_consumption + self.SUMMER_FUEL_CONSUMTION) > 0:
            self.fuel_quantity -= distance * (self.fuel_consumption + self.SUMMER_FUEL_CONSUMTION)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    SUMMER_FUEL_CONSUMTION = 1.6
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity - distance * (self.fuel_consumption + self.SUMMER_FUEL_CONSUMTION) > 0:
            self.fuel_quantity -= distance * (self.fuel_consumption + self.SUMMER_FUEL_CONSUMTION)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95



truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
