import unittest
from simple_calculator import SimpleCalculator
class testCalc(unittest.TestCase):
    def setUp(self):
        self.calc=SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -4), -2)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2, 0), 0)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(2, 3), 5)
        self.assertEqual(self.calc.subtract(3, 2), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(2, -3), -5)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 3), 2)
        self.assertEqual(self.calc.multiply(2, 3), 5)
        self.assertEqual(self.calc.multiply(3, 2), -2)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(2, -3), -5)
    def test_division(self):
        self.assertEqual(self.calc.divide(5, 3), 2)
        self.assertEqual(self.calc.divide(2, 3), 5)
        self.assertEqual(self.calc.divide(3, 2), -2)
        self.assertEqual(self.calc.divide(0, 0), 0)
        self.assertEqual(self.calc.divide(2, -3), -5)
        self.assertIsNone(self.calc.divide(1, 0))
        self.assertIsNone(self.calc.divide(0, 0))