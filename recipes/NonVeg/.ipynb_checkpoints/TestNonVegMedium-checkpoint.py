import pandas as pd
import unittest
from unittest.mock import patch
from recipes.NonVeg import intermediate as mnv
class TestNonVegMedium(unittest.TestCase):
    def setUp(self):
        self.x=pd.read_csv("Recipes.csv")
        TestNonVegMedium.a=mnv.medium(self.x)
    y = "Chicken Eggs Fish Lamb"
    @patch('builtins.input',return_value=y)
    def test_nonveg_select(self,mock_input):

        result1= TestNonVegMedium.a.select()
        
        self.assertIn("Chicken", result1)
        self.assertIn("Eggs", result1)
        self.assertIn("Fish", result1)
        self.assertIn("Lamb", result1)
        
    
    x=["Sunny side up","Poached eggs","Barbeque chicken","Chicken gravy","Fish fingers","Fish gravy","Lamb curry","Lamb kabab"]
    @patch('builtins.input',return_value=x)
    def test_nonveg_search(self,mock_input):
        result2= TestNonVegMedium.a.search()
        
        self.assertIn("Poached eggs", result2)
        self.assertIn("Barbeque chicken", result2)
        self.assertIn("Chicken gravy", result2)
        self.assertIn("Fish gravy", result2)
        self.assertIn("Lamb kabab", result2)