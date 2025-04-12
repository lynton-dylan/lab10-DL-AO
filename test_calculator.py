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
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
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
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()