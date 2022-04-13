class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


import unittest
class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Kuku")

    def test_cat_increase_after_eat(self):
        self.assertEqual(0,self.cat.size)
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_if_cat_is_fed_after_eat(self):
        self.assertEqual(False, self.cat.fed)
        self.cat.eat()
        self.assertEqual(True,self.cat.fed)

    def test_cat_cant_eat_after_fed_raises(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual("Already fed.",str(ex.exception))

    def test_cat_cant_sled_without_eat_raises(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual("Cannot sleep while hungry",str(ex.exception))

    def test_cat_isnt_sleepy_after_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertEqual(False,self.cat.sleepy)

if __name__ == "__main__":
    unittest.main()