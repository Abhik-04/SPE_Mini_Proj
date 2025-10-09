import unittest
import math

class TestCalc(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(math.sqrt(16), 4)

    def test_factorial(self):
        self.assertEqual(math.factorial(5), 120)

    def test_ln(self):
        self.assertAlmostEqual(math.log(math.e), 1)

    def test_power(self):
        self.assertEqual(math.pow(2, 3), 8)

if __name__ == "__main__":
    unittest.main()