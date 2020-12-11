import unittest

from project.truck import Truck


class TestTruck(unittest.TestCase):

    def setUp(self) -> None:
        self.truck = Truck(80, 3)

    def test_drive_sufficient_fuel_quantity(self):
        self.truck.drive(2)
        result = self.truck.fuel_quantity
        expected_result = 70.8
        self.assertEqual(result, expected_result)

    def test_drive_insufficient_fuel_quantity(self):
        self.truck.drive(100)
        result = self.truck.fuel_quantity
        expected_result = 80
        self.assertEqual(result, expected_result)

    def test_refuel_quantity(self):
        self.truck.refuel(50)
        result = self.truck.fuel_quantity
        expected_result = 127.5
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()