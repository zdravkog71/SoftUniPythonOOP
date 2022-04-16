from TestingExercise.mammal.project.mammal import Mammal
from unittest import TestCase, main

class TestMammal(TestCase):
    def setUp(self):
        self.animal = Mammal("Test", "cat", "Meaow")

    def test_init_mammal(self):
        self.assertEqual("Test",self.animal.name)
        self.assertEqual("cat", self.animal.type)
        self.assertEqual("Meaow", self.animal.sound)
        self.assertEqual("animals",self.animal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual("Test makes Meaow",self.animal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals",self.animal.get_kingdom())

    def test_get_info(self):
        self.assertEqual("Test is of type cat",self.animal.info())

if __name__ == "__main__":
    main()