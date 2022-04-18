from project_test_exam_18_Apr_2022.plantation import Plantation
from unittest import TestCase, main

class TestPlantation(TestCase):
    def setUp(self):
        self.plant = Plantation(100)

    def test_init(self):
        self.assertEqual(100, self.plant.size)
        self.assertEqual({},self.plant.plants)
        self.assertEqual([],self.plant.workers)

    def test_init_negative_size_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.negative_plant = Plantation(-5)
        self.assertEqual("Size must be positive number!",str(ex.exception))

    def test_hire_worker_exists_raises(self):
        self.plant.workers.append("Test")
        with self.assertRaises(ValueError) as ex:
            self.plant.hire_worker("Test")
        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_append_worker(self):
        self.plant.hire_worker("Zdr")
        self.assertEqual(["Zdr"], self.plant.workers)

    def test_hire_worker_return_messsage(self):
        self.assertEqual("Zdr successfully hired.", self.plant.hire_worker("Zdr"))

    def test_count_plants(self):
        self.plant.plants["plant1"] = "zdr"
        self.assertEqual(3,self.plant.__len__())

    def test_planting_worker_not_exists_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.plant.planting("Zdr","Plant")
        self.assertEqual("Worker with name Zdr is not hired!", str(ex.exception))

    def test_len_more_than_plant_size_raises(self):
        self.small_plant = Plantation(2)
        self.small_plant.workers.append("Zdr")
        self.small_plant.plants["plant1"] = "zdravko"
        with self.assertRaises(ValueError) as ex:
            self.small_plant.planting("Zdr", "Plant")
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_worker_in_plants(self):
        self.plant.plants["Zdr"] = "Plant1"
        self.plant.workers.append("Zdr")
        self.assertEqual("Zdr planted Plant1.",self.plant.planting("Zdr","test_exam_18_Apr_2022"))




if __name__ == "__main__":
    main()