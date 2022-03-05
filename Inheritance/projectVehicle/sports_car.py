from Inheritance.projectVehicle.car import Car


class SportsCar(Car):
    def race(self):
        return "racing..."



insignia = SportsCar()
print(insignia.move())
