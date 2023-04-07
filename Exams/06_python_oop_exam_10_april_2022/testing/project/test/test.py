from project.movie import Movie
import unittest


class TestMovie(unittest.TestCase):
    def setUp(self):
        self.movie1 = Movie("movie1", 2000, 10)
        self.movie2 = Movie("movie2", 1970, 20)

    def test_init(self):
        self.assertEqual(self.movie1.name, "movie1")
        self.assertEqual(self.movie1.year, 2000)
        self.assertEqual(self.movie1.rating, 10)
        self.assertEqual(self.movie1.actors, [])

    def test_name_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.movie1.name = ""
        self.assertEqual(str(ve.exception), "Name cannot be an empty string!")

    def test_year_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.movie1.year = 1886
        self.assertEqual(str(ve.exception), "Year is not valid!")

    def test_add_actor(self):
        self.movie1.add_actor("actor1")
        self.movie1.add_actor("actor2")
        self.assertEqual(self.movie1.actors, ["actor1", "actor2"])
        self.assertEqual(repr(self.movie1), "Name: movie1\n"
                                            "Year of Release: 2000\n"
                                            "Rating: 10.00\n"
                                            "Cast: actor1, actor2")

    def test_add_actor_already_added(self):
        self.movie1.add_actor("actor1")
        self.assertEqual(self.movie1.add_actor("actor1"), "actor1 is already added in the list of actors!")
        self.assertEqual(self.movie1.actors, ["actor1"])
        self.assertEqual(repr(self.movie1), "Name: movie1\n"
                                            "Year of Release: 2000\n"
                                            "Rating: 10.00\n"
                                            "Cast: actor1")

    def test_greater_than_overwrite(self):
        self.assertEqual(self.movie1 > self.movie2, '"movie2" is better than "movie1"')
        self.movie1.rating = 30
        self.assertEqual(self.movie1 > self.movie2, '"movie1" is better than "movie2"')


if __name__ == '__main__':
    unittest.main()

# https://judge.softuni.org/Contests/Practice/Index/3426#2
