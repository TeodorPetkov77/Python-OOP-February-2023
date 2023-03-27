import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(40, 200)

    def test_init(self):
        self.assertEqual(self.vehicle.fuel, 40)
        self.assertEqual(self.vehicle.horse_power, 200)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_drive(self):
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 27.5)
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(1000)
        self.assertEqual(str(context.exception), 'Not enough fuel')

    def test_refuel(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(2.5)
        self.assertEqual(self.vehicle.fuel, 30)
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(1000)
        self.assertEqual(str(context.exception), 'Too much fuel')

    def test_str(self):
        self.assertEqual(str(self.vehicle), "The vehicle has 200 "
                                            f"horse power with 40 fuel left and 1.25 fuel consumption")


if __name__ == '__main__':
    unittest.main()

# https://judge.softuni.org/Contests/Compete/Index/1949#1
