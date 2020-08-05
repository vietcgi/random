#!/usr/bin/env python
import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    calculator = Calculator()
    
    def test_add(self):
        self.assertEqual(4, self.calculator.add(2,2))

    def test_subtract(self):
        self.assertEqual(2, self.calculator.subtract(3,1))
        self.assertEqual(-2, self.calculator.subtract(1,3))

    def test_division(self):
        self.assertEqual(3, self.calculator.division(9,3))
        with self.assertRaises(ZeroDivisionError):
            self.calculator.division(3,0) 
    
if __name__ == "__main__":
    unittest.main()
