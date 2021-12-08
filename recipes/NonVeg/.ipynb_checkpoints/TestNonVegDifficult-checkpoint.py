import pandas as pd
import unittest
from unittest.mock import patch
from recipes.NonVeg import difficult as dnv
class TestNonVegDifficult(unittest.TestCase):
    def setUp(self):
        self.x=pd.read_csv("Recipes.csv")
        TestNonVegDifficult.a=dnv.difficult(self.x)
    y = "Chicken Eggs Fish Lamb"
    @patch('builtins.input',return_value=y)
    def test_nonveg_select(self,mock_input):

        result1= TestNonVegDifficult.a.select()
        
        self.assertIn("Chicken", result1)
        self.assertIn("Eggs", result1)
        self.assertIn("Fish", result1)
        self.assertIn("Lamb", result1)
        
    
    x=["Devils eggs","Egg Biryani","Chicken Biryani","Chicken lollipop","Sushi","Lebanese fish","Lamb ribs","BBQ Lamb"]
    @patch('builtins.input',return_value=x)
    def test_nonveg_search(self,mock_input):
        result2= TestNonVegDifficult.a.search()
        
        self.assertIn("BBQ Lamb", result2)
        self.assertIn("Chicken Biryani", result2)
        self.assertIn("Chicken lollipop", result2)
        self.assertIn("Sushi", result2)
        self.assertIn("Lamb ribs", result2)