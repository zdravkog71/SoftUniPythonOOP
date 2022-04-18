from project_real_exam.car.muscle_car import MuscleCar
from project_real_exam.car.sports_car import SportsCar
from project_real_exam.driver import Driver
from project_real_exam.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type, model, speed_limit):
        if car_type == "MuscleCar" or car_type == "SportsCar":
            for car in self.cars:
                if car.model == model:
                    raise Exception(f"Car {model} is already created!")
            if car_type == "SportsCar":
                car = SportsCar(model, speed_limit)
                self.cars.append(car)
                return f"{car_type} {model} is created."

            if car_type == "MuscleCar":
                car = MuscleCar(model, speed_limit)
                self.cars.append(car)
                return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        is_driver = False
        for driver in self.drivers:
            if driver.name == driver_name:
                is_driver = True
        if not is_driver:
            raise Exception(f"river {driver_name} could not be found!")
        sports_cars = [car for car in self.cars if car.__class__.__name__ == "SportsCar"]
        muscle_cars = [car for car in self.cars if car.__class__.__name__ == "MuscleCar"]
        if car_type == "SportsCar":
            if len(sports_cars) > 0:
                last_car = sports_cars.pop()
                if last_car.is_taken:
                    raise Exception(f"Car {car_type} could not be found!")
                for driver in self.drivers:
                    if driver.name == driver_name:
                        if driver.car == None:
                            driver.car = last_car
                            last_car.is_taken = True
                            return f"Driver {driver_name} chose the car {last_car.model}."
                        previous_car_model = driver.car.model
                        driver.car = last_car
                        last_car.is_taken = True
                        return f"Driver {driver_name} changed his car from {previous_car_model} to {last_car.model}."
            else:
                raise Exception(f"Car {car_type} could not be found!")

            if car_type == "MuscleCar":
                if len(muscle_cars) > 0:
                    last_car = muscle_cars.pop()
                    if last_car.is_taken:
                        raise Exception(f"Car {car_type} could not be found!")
                    for driver in self.drivers:
                        if driver.name == driver_name:
                            if driver.car == None:
                                driver.car = last_car
                                last_car.is_taken = True
                                return f"Driver {driver_name} chose the car {last_car.model}."
                            previous_car_model = driver.car.model
                            driver.car = last_car
                            last_car.is_taken = True
                            return f"Driver {driver_name} changed his car from {previous_car_model} to {last_car.model}."
                else:
                    raise Exception(f"Car {car_type} could not be found!")

    def add_driver_to_race(self, race_name, driver_name):
        is_race_exist = False
        current_race = None
        is_driver_exist = False
        current_driver = None
        for race in self.races:
            if race.name == race_name:
                is_race_exist = True
                current_race = race
        if not is_race_exist:
            raise Exception(f"Race {race_name} could not be found!")

        for driver in self.drivers:
            if driver.name == driver_name:
                is_driver_exist = True
                current_driver = driver
        if not is_driver_exist:
            raise Exception(f"Driver {driver_name} could not be found!")
        if current_driver.car == None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        #check if whether driver is in the race
        if current_driver in current_race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        current_race.drivers.append(current_driver)
        return f"Driver {driver_name} added in {race_name} race."



    def start_race(self, race_name):
        is_race_exists = False
        current_race = None
        for race in self.races:
            if race.name == race_name
                is_race_exists = True
                current_race = race
        if not is_race_exists:
            raise Exception(f"Race {race_name} could not be found!")
        if len(current_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        # Race can start - fist 3 cars are winners
        for

# controller = Controller()
# print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
# print(controller.cars)