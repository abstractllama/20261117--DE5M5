import unittest
from day_4_final_task.cleanup_v1 import na_clean, title_corrector, remove_formating
import pandas as pd
import numpy as np
import re

#as dataset is tiny, use actual as test?
#psuedo = pd.read_csv(r"C:\Users\Admin\Desktop\20261117--DE5M5\data\03_Library Systembook.csv")
#No actual approach needs to be to create a blank dataset which is just used for testing. 

# FEEDBACK
class TestOperations(unittest.TestCase): ##here when you do x.y - it looks up an external python file
    ##class inheritance when you initialise a cunit the this means that when you inherit, due to the importing you can still use the original  class in the new notebook/application
    
    ## ARRANGE, ACT and ASSERT <-- General template
    def setUp(self): 
        # Create a new dataframe which has na values with 3 random cols and at least one row with NAN values
        self.df = pd.DataFrame(
    {
        "name": ["Alfred", "Batman", "Catwoman"],
        "toy": [np.nan, "Batmobile", "Bullwhip"],
        "born": [pd.NaT, pd.Timestamp("1940-04-25"), pd.NaT],
    }
)
        # Run the above dataframe through the na_clean to get an output df_out

    def test_na(self):

        #act - run it against the sample
        sample = na_clean(self.df)
        self.assertFalse(sample.isna().any().any()) #i think this is testing the input df not the output of the na_clean

    #def speech_marks(self):
        #sample = remove_formating(self.df)
        #self.assertFalse(sample.re_match('"').any().any())  ##avoid re for large workloads as its not optimised for this use the pd searchstring/
    
   


if __name__ == "__main__":
    unittest.main()


