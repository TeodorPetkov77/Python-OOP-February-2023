import unittest

from worker import Worker


class WorkerTests(unittest.TestCase):
    def test_initiation(self):
        worker = Worker("Teo", 600, 10)
        self.assertEqual(worker.name, "Teo")
        self.assertEqual(worker.salary, 600)
        self.assertEqual(worker.energy, 10)
        self.assertEqual(worker.money, 0)

    def test_rest(self):
        worker = Worker("Teo", 600, 10)
        worker.rest()
        self.assertEqual(worker.energy, 11)

    def test_negative_work(self):
        worker = Worker("Teo", 600, 0)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_salary_increase(self):
        worker = Worker("Teo", 600, 10)
        worker.work()
        self.assertEqual(worker.money, 600)

    def test_energy_decrease(self):
        worker = Worker("Teo", 600, 10)
        worker.work()
        self.assertEqual(worker.energy, 9)

    def test_get_info(self):
        worker = Worker("Teo", 600, 10)
        self.assertEqual(worker.get_info(), "Teo has saved 0 money.")


if __name__ == '__main__':
    unittest.main()

# https://judge.softuni.org/Contests/Practice/Index/1948#0


# 1.	Test Worker
# Create a class WorkerTests
# In judge you need to submit just the WokerTests class, with the unittest module imported.
# Create the following tests:
# •	Test if the worker is initialized with the correct name, salary, and energy
# •	Test if the worker's energy is incremented after the rest method is called
# •	Test if an error is raised if the worker tries to work with negative energy or equal to 0
# •	Test if the worker's money is increased by his salary correctly after the work method is called
# •	Test if the worker's energy is decreased after the work method is called
# •	Test if the get_info method returns the proper string with correct values
