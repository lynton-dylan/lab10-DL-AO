#https://github.com/lynton-dylan/lab10-DL-AO.git
#Partner 1: Dylan Lynton
#Partner 2: Aaliyah Otto

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(0.6, 0.8), 1.4)
        self.assertEqual(add(-7, -9), -16)
        self.assertEqual(add(-30, 10), -20)

    def test_subtract(self): # 3 assertions
        self.assertAlmostEqual(subtract(0.78, 0.08), 0.7)
        self.assertEqual(subtract(-78, -10), -68)
        self.assertEqual(subtract(-30, 10), -40)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(6, 3), 18)
        self.assertEqual(mul(4, 94), 376)
        self.assertAlmostEqual(mul(7.6, 8.3), 63.08)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(7, 56), 8)
        self.assertAlmostEqual(div(3.6, 472.5), 131.25)
        self.assertEqual(div(5, 2025), 405)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 67)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(0.2, 1), -0)
        self.assertAlmostEqual(logarithm(0.8, 0.6), 2.2892242269941)
        self.assertAlmostEqual(logarithm(78, 0.2), -0.3694159918548)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 67)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, -1)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(9, 12), 15)
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-9)
        self.assertEqual(square_root(2025), 45)
        self.assertEqual(square_root(196), 14)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()