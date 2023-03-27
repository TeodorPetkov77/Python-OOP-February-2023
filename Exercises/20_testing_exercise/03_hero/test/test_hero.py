import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("teo", 60, 100, 100)

    def test_init(self):
        self.assertEqual((self.hero.username, self.hero.level,
                          self.hero.health, self.hero.damage),
                         ("teo", 60, 100, 100))

    def test_battle_exceptions(self):
        enemy = Hero("teo", 60, 100, 100)
        with self.assertRaises(Exception) as context:
            self.hero.battle(enemy)
        self.assertEqual(str(context.exception), "You cannot fight yourself")
        hero_zero = Hero("zero", 60, 0, 100)
        with self.assertRaises(ValueError) as context:
            hero_zero.battle(enemy)
        self.assertEqual(str(context.exception), "Your health is lower than or equal to 0. You need to rest")
        enemy_zero = Hero("enemy_zero", 60, 0, 100)
        with self.assertRaises(ValueError) as context:
            self.hero.battle(enemy_zero)
        self.assertEqual(str(context.exception), "You cannot fight enemy_zero. He needs to rest")

    def test_battle_draw(self):
        enemy = Hero("enemy", 60, 100, 100)
        self.assertEqual(self.hero.battle(enemy), "Draw")

    def test_you_win(self):
        enemy = Hero("enemy", 1, 1, 1)
        self.assertEqual(self.hero.battle(enemy), "You win")
        self.assertEqual(self.hero.level, 61)
        self.assertEqual(self.hero.health, 104)
        self.assertEqual(self.hero.damage, 105)

    def test_you_lose(self):
        enemy = Hero("enemy", 60, 100, 100)
        hero = Hero("hero", 1, 1, 1)
        self.assertEqual(hero.battle(enemy), "You lose")
        self.assertEqual(enemy.level, 61)
        self.assertEqual(enemy.health, 104)
        self.assertEqual(enemy.damage, 105)

    def test_str(self):
        self.assertEqual(str(self.hero), "Hero teo: 60 lvl\n"
                                         "Health: 100\n"
                                         "Damage: 100\n")


if __name__ == '__main__':
    unittest.main()

# https://judge.softuni.org/Contests/Compete/Index/1949#3
