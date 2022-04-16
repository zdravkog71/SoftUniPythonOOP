from TestingExercise.hero.project.hero import Hero
from unittest import TestCase, main

class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Zdr", 100, 200, 300)
        self.enemy = Hero("Kuku", 100, 200, 300)
        self.strong_hero = Hero("StrongMan", 150, 50000, 5000)

    def test_hero_init(self):
        self.assertEqual("Zdr",self.hero.username)
        self.assertEqual(100,self.hero.level)
        self.assertEqual(200,self.hero.health)
        self.assertEqual(300,self.hero.damage)

    def test_batle_with_himself_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself",str(ex.exception))

    def test_batle_health_hero_zero_or_less_raises(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest",str(ex.exception))

    def test_batle_health_enemy_zero_or_less_raises(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Kuku. He needs to rest",str(ex.exception))

    def test_batle_equal(self):
        self.assertEqual("Draw",self.hero.battle(self.enemy))

    def test_batle_hero_win(self):
        res = self.strong_hero.battle(self.enemy)
        self.assertEqual("You win",res)
        self.assertEqual(151,self.strong_hero.level)
        self.assertEqual(20005,self.strong_hero.health)
        self.assertEqual(5005,self.strong_hero.damage)

    def test_batle_hero_lose(self):
        res = self.enemy.battle(self.strong_hero)
        self.assertEqual("You lose",res)
        self.assertEqual(151, self.strong_hero.level)
        self.assertEqual(20005, self.strong_hero.health)
        self.assertEqual(5005, self.strong_hero.damage)

    def test_string(self):
        self.assertEqual("Hero Zdr: 100 lvl\nHealth: 200\nDamage: 300\n",str(self.hero))


if __name__ == "__main__":
    main()