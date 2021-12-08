import pandas as pd
import unittest
from unittest.mock import patch
from recipes.NonVeg import easy as env
class TestNonVegEasy(unittest.TestCase):
    def setUp(self):
        self.x=pd.read_csv("Recipes.csv")
        TestNonVegEasy.a=env.easy(self.x)
    y = "Chicken Eggs Fish Lamb"
    @patch('builtins.input',return_value=y)
    def test_nonveg_select(self,mock_input):

        result1= TestNonVegEasy.a.select()
        
        self.assertIn("Chicken", result1)
        self.assertIn("Eggs", result1)
        self.assertIn("Fish", result1)
        self.assertIn("Lamb", result1)
        
    
    x=["Boiled eggs","Scrambled eggs","Pan tossed chicken","Chicken shawarma","Pan fried fish","Oven roasted fish","Stir fried lamb","Baked lamb"]
    @patch('builtins.input',return_value=x)
    def test_nonveg_search(self,mock_input):
        result2= TestNonVegEasy.a.search()
        
        self.assertIn("Boiled eggs", result2)
        self.assertIn("Chicken shawarma", result2)
        self.assertIn("Oven roasted fish", result2)
        self.assertIn("Stir fried lamb", result2)
        self.assertIn("Scrambled eggs", result2)