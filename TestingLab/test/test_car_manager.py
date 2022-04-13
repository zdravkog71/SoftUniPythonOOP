from TestingLab.car_manager import Car

from unittest import TestCase, main

class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Opel","Insignia",10,60)

    def test_car_make(self):
        self.assertEqual("Opel",self.car.make)

    def test_car_model(self):
        self.assertEqual("Insignia", self.car.model)

    def test_car_consumption(self):
        self.assertEqual(10, self.car.fuel_consumption)

    def test_car_tank_fuel(self):
        self.assertEqual(60, self.car.fuel_capacity)

    def test_init_fuel_amount(self):
        self.assertEqual(0, self.car.fuel_amount)

    def test_init_empty_make_raises(self):
        with self.assertRaises(Exception) as ex:
            new_car = Car("","Insignia",10,60)
        self.assertEqual("Make cannot be null or empty!",str(ex.exception))

    def test_init_empty_model_raises(self):
        with self.assertRaises(Exception) as ex:
            new_car = Car("Opel","",10,60)
        self.assertEqual("Model cannot be null or empty!",str(ex.exception))

    def test_fuel_consumption_to_be_less_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            new_car = Car("Opel","Insignia",0,60)
        self.assertEqual("Fuel consumption cannot be zero or negative!",str(ex.exception))

    def test_tank_capacity_to_be_less_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            new_car = Car("Opel","Insignia",10,0)
        self.assertEqual("Fuel capacity cannot be zero or negative!",str(ex.exception))

    def test_fuel_amount_to_be_less_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!",str(ex.exception))

    def test_refuel_add_fuel_correctly(self):
        self.car.refuel(10)
        self.assertEqual(10,self.car.fuel_amount)

    def test_refuel_add_negative_zero_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!",str(ex.exception))

    def test_fuel_amount_larger_than_capacity_return_amount(self):
        self.car.refuel(70)
        self.assertEqual(60,self.car.fuel_amount)

    def test_if_can_drive_more_than_fuel_allow_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!",str(ex.exception))

    def test_if_fuel_reduced_after_drive(self):
        self.car.refuel(60)
        self.car.drive(10)
        self.assertEqual(59.0,self.car.fuel_amount)



if __name__ == "__main__":
    main()