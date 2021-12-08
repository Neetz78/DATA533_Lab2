import pandas as pd
import unittest
from unittest.mock import patch
from recipes.Veg import intermediate as mv
class TestVegMedium(unittest.TestCase):
    def setUp(self):
        self.x=pd.read_csv("Recipes.csv")
        TestVegMedium.a=mv.medium(self.x)
    y = "Bread Milk Flour Rice Carrot Potato Brocolli Onion Cheese Oats Lentils Noodles Pasta Corn Spinach"
    @patch('builtins.input',return_value=y)
    def test_veg_select(self,mock_input):

        result1= TestVegMedium.a.select()
        
        self.assertIn("Onion", result1)
        self.assertIn("Oats", result1)
        self.assertIn("Rice", result1)
        self.assertIn("Noodles", result1)
        self.assertIn("Corn", result1)
    
    x=["Sandwich","Hot chocolate","Bread","Veg Sushi","Carrot paratha","French fries","Pasta","Onion rings","Mozerella Cheese sticks","Oats Upma", "Indian Dal","Chopsuey","Arabiata pasta","Corn and cheese","Spinach paratha","Bread Manchurian","Milk Shake","Crepes","Fried rice","Carrot soup","Twisted potato","Brocolli paratha","Cheesy Onions","Cheese cake","Health bar","Dal soup","Fried noodles","White sauce pasta","Corn Crackers","Palak paneer"]
    @patch('builtins.input',return_value=x)
    def test_veg_search(self,mock_input):
        result2= TestVegMedium.a.search()
        
        self.assertIn("Sandwich", result2)
        self.assertIn("Bread", result2)
        self.assertIn("Corn and cheese", result2)
        self.assertIn("Fried noodles", result2)
        self.assertIn("White sauce pasta", result2)