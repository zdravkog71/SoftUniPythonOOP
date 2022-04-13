class Worker:
    def __init__(self, name, salary, energy):

        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):

        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest
class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Zdravko",100, 10)

    def test_if_worker_init_properly_name(self):
        result = self.worker.name
        expected_result = "Zdravko"
        self.assertEqual(result, expected_result)

    def test_if_worker_init_properly_salary(self):
        result = self.worker.salary
        expected_result = 100
        self.assertEqual(result, expected_result)

    def test_if_worker_init_properly_energy(self):
        result = self.worker.energy
        expected_result = 10
        self.assertEqual(result, expected_result)

    def test_if_increase_energy_after_rest(self):
        self.assertEqual(self.worker.energy,10)
        self.worker.rest()
        self.assertEqual(self.worker.energy, 11)

    def test_if_worker_works_with_negative_energy_raises(self):
        self.worker = Worker("Zdravko", 100, 0)
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_if_worker_salary_increased_with_work(self):
        self.assertEqual(0,self.worker.money)
        self.worker.work()
        self.assertEqual(100,self.worker.money)

    def test_worker_energy_decreased_after_work(self):
        self.assertEqual(10,self.worker.energy)
        self.worker.work()
        self.assertEqual(9,self.worker.energy)

    def test_worker_get_info(self):
        result = self.worker.get_info()
        expected_result = "Zdravko has saved 0 money."
        self.assertEqual(expected_result,result)

if __name__ == "__main__":
    unittest.main()