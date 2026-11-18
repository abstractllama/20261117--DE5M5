##test 2

import unittest
from calculator import Calculator ##were able to load this in because we declared it in calculator

class TestOperations(unittest.TestCase): ##here when you do x.y - it looks up an external python file
    ##class inheritance when you initialise a cunit the this means that when you inherit, due to the importing you can still use the original  class in the new notebook/application
    
    ## ARRANCE, ACT and ASSERT <-- General template
    def setUp(self):
        self.calc = Calculator(8,2)

    def test_sum(self):
        self.assertEqual(self.calc.get_sum(),11, "sum wrong")

    def tearDown(self):
        ##destory self at end. gets rid of loaded assets
        pass
        

if __name__ == "__main__":
    unittest.main()