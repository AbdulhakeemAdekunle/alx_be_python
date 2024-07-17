import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-2, 6), 4)
        self.assertEqual(self.calc.add(-3, -5), -8)
        self.assertEqual(self.calc.add(-9, 9), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 1), 2)
        self.assertEqual(self.calc.subtract(-2, 6), -8)
        self.assertEqual(self.calc.subtract(-3, -5), 2)
        self.assertEqual(self.calc.subtract(-9, 9), -18)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)
        self.assertEqual(self.calc.multiply(-2, 6), -12)
        self.assertEqual(self.calc.multiply(-3, -5), 15)
        self.assertEqual(self.calc.multiply(-9, 9), -81)

    def test_divide(self):
        self.assertEqual(self.calc.divide(16, 4), 4)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(-3, -1), 3)
        self.assertIsNone(self.calc.divide(3, 0))