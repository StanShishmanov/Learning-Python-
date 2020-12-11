import unittest
from project.car import Car


class TestCar(unittest.TestCase):
    #
    def setUp(self):
        self.car = Car(50, 5)

    def test_drive_sufficient_fuel_quantity(self):
        self.car.drive(2)
        result = self.car.fuel_quantity
        expected_result = 38.2
        self.assertEqual(result, expected_result)

    def test_drive_insufficient_fuel_quantity(self):
        self.car.drive(10)
        result = self.car.fuel_quantity
        expected_result = 50
        self.assertEqual(result, expected_result)

    def test_refuel_quantity(self):
        self.car.refuel(50)
        result = self.car.fuel_quantity
        expected_result = 100
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
