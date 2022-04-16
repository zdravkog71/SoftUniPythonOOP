from TestingExercise.vehicle.project.vehicle import Vehicle
from unittest import TestCase, main

class TestVehicle(TestCase):
    def setUp(self):
        self.veh = Vehicle(60,165)

    def test_init_vehicle(self):
        self.assertEqual(60, self.veh.fuel)
        self.assertEqual(60, self.veh.capacity)
        self.assertEqual(165, self.veh.horse_power)
        self.assertEqual(1.25, self.veh.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_enough_fuel_is_reduced(self):
        self.veh.drive(10)
        self.assertEqual(47.5,self.veh.fuel)

    def test_drive_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.veh.drive(100)
        self.assertEqual("Not enough fuel",str(ex.exception))

    def test_refuel_with_right_quantity_fuel(self):
        self.veh.fuel -= 10
        self.veh.refuel(10)
        self.assertEqual(60,self.veh.fuel)

    def test_refuel_with_more_fuel_raises(self):
        self.veh.fuel -= 10
        with self.assertRaises(Exception) as ex:
            self.veh.refuel(20)
        self.assertEqual("Too much fuel",str(ex.exception))

    def test_str_representation(self):
        self.assertEqual("The vehicle has 165 horse power with 60 fuel left and 1.25 fuel consumption",self.veh.__str__())


if __name__ == "__main__":
    main()

