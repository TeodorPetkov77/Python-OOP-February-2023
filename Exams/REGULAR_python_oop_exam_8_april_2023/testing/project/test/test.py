from project.tennis_player import TennisPlayer
import unittest


class TestTennisPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = TennisPlayer("player1", 20, 100)
        self.player2 = TennisPlayer("player2", 30, 120)

    def test_init(self):
        self.assertEqual(self.player1.name, "player1")
        self.assertEqual(self.player1.age, 20)
        self.assertEqual(self.player1.points, 100)

    def test_name_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.player1.name = "pl"
        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_age_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.player1.age = 17
        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_add_new_wins(self):
        self.player1.add_new_win("Sofia")
        self.player1.add_new_win("Plovdiv")
        self.player1.add_new_win("Varna")
        self.assertEqual(self.player1.wins, ["Sofia", "Plovdiv", "Varna"])
        self.assertEqual(str(self.player1), "Tennis Player: player1\n"
                                            "Age: 20\n"
                                            "Points: 100.0\n"
                                            "Tournaments won: Sofia, Plovdiv, Varna")

    def test_add_new_wins_already_exists(self):
        self.player1.add_new_win("Sofia")
        self.assertEqual(self.player1.add_new_win("Sofia"), "Sofia has been already added to the list of wins!")
        self.assertEqual(self.player1.wins, ["Sofia"])
        self.assertEqual(str(self.player1), "Tennis Player: player1\n"
                                            "Age: 20\n"
                                            "Points: 100.0\n"
                                            "Tournaments won: Sofia")

    def test_lower_than(self):
        self.assertEqual(self.player1 < self.player2,
                         "player2 is a top seeded player and he/she is better than player1")
        self.assertEqual(self.player2 < self.player1, "player2 is a better player than player1")


if __name__ == '__main__':
    unittest.main()

# https://judge.softuni.org/Contests/Compete/Index/3911#2