from project.plantation import Plantation
import unittest


class TestPlantation(unittest.TestCase):
    def setUp(self):
        self.plantation = Plantation(10)

    def test_init(self):
        self.assertEqual(self.plantation.size, 10)
        self.assertEqual(self.plantation.plants, {})
        self.assertEqual(self.plantation.workers, [])

    def test_size_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        self.assertEqual(str(ve.exception), "Size must be positive number!")

    def test_hire_worker(self):
        self.assertEqual(self.plantation.hire_worker("worker1"), "worker1 successfully hired.")
        self.assertEqual(self.plantation.hire_worker("worker2"), "worker2 successfully hired.")
        self.assertEqual(self.plantation.workers, ["worker1", "worker2"])
        self.assertEqual(str(self.plantation), "Plantation size: 10\nworker1, worker2")
        self.assertEqual(repr(self.plantation), "Size: 10\nWorkers: worker1, worker2")

    def test_hire_worker_already_exists(self):
        self.assertEqual(self.plantation.hire_worker("worker1"), "worker1 successfully hired.")
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("worker1")
        self.assertEqual(str(ve.exception), "Worker already hired!")
        self.assertEqual(str(self.plantation), "Plantation size: 10\nworker1")
        self.assertEqual(repr(self.plantation), "Size: 10\nWorkers: worker1")

    def test_planting(self):
        self.plantation.hire_worker("worker1")
        self.plantation.hire_worker("worker2")
        self.assertEqual(self.plantation.planting("worker1", "plant1"), "worker1 planted it's first plant1.")
        self.assertEqual(self.plantation.planting("worker1", "plant2"), "worker1 planted plant2.")
        self.assertEqual(self.plantation.planting("worker2", "plant3"), "worker2 planted it's first plant3.")
        self.assertEqual(self.plantation.planting("worker2", "plant4"), "worker2 planted plant4.")
        self.assertEqual(self.plantation.plants, {'worker1': ['plant1', 'plant2'], 'worker2': ['plant3', 'plant4']})
        self.assertEqual(str(self.plantation), "Plantation size: 10"
                                               "\nworker1, worker2"
                                               "\nworker1 planted: plant1, plant2"
                                               "\nworker2 planted: plant3, plant4")
        self.assertEqual(repr(self.plantation), "Size: 10\nWorkers: worker1, worker2")
        self.assertEqual(len(self.plantation), 4)

    def test_planting_worker_not_existing(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("worker1", "plant1")
        self.assertEqual(str(ve.exception), "Worker with name worker1 is not hired!")
        self.assertEqual(str(self.plantation), "Plantation size: 10\n")
        self.assertEqual(repr(self.plantation), "Size: 10\nWorkers: ")

    def test_planting_plantation_is_full(self):
        self.plantation.hire_worker("worker1")
        self.plantation.planting("worker1", "plant1")
        self.plantation.planting("worker1", "plant2")
        self.plantation.planting("worker1", "plant3")
        self.plantation.planting("worker1", "plant4")
        self.plantation.planting("worker1", "plant5")
        self.plantation.planting("worker1", "plant6")
        self.plantation.planting("worker1", "plant7")
        self.plantation.planting("worker1", "plant8")
        self.plantation.planting("worker1", "plant9")
        self.plantation.planting("worker1", "plant10")
        self.assertEqual(len(self.plantation), 10)
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("worker1", "plant11")
        self.assertEqual(str(ve.exception), "The plantation is full!")
        self.assertEqual(str(self.plantation), "Plantation size: 10"
                                               "\nworker1"
                                               "\nworker1 planted: plant1, "
                                               "plant2, plant3, plant4, "
                                               "plant5, plant6, plant7, "
                                               "plant8, plant9, plant10")
        self.assertEqual(repr(self.plantation), "Size: 10\nWorkers: worker1")


if __name__ == '__main__':
    unittest.main()

# https://judge.softuni.org/Contests/Practice/Index/3431#2
