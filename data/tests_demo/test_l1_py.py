import unittest
from calculator import Calculator ##were able to load this in because we declared it in calculator

class TestOperations(unittest.TestCase): ##here when you do x.y - it looks up an external python file
    ##class inheritance when you initialise a cunit the this means that when you inherit, due to the importing you can still use the original  class in the new notebook/application
    
    ## ARRANCE, ACT and ASSERT <-- General template

    def test_sum(self):
        #arrange
        testCal = Calculator(8,2)
        #act & assert
        self.assertEqual(testCal.get_sum(),10, "sum is wrong")

    ### write the remaining tests for the other calc types

    def test_deduct(self):
        testCal = Calculator(8,2)
        self.assertEqual(testCal.get_deduct(),6,"deduction error")

    def test_multi(self):
        testCal = Calculator(8,2)
        self.assertEqual(testCal.multiply(),16,"ha")

if __name__ == "__main__":
    unittest.main()