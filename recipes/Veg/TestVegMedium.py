import pandas as pd
import unittest
from unittest.mock import patch
from recipes.Veg import easy as ev
class TestVegEasy(unittest.TestCase):
    def setUp(self):
        self.x=pd.read_csv("Recipes.csv")
        TestVegEasy.a=ev.easy(self.x)
    y = "Bread Milk Flour Rice Carrot Potato Brocolli Onion Cheese Oats Lentils Noodles Pasta Corn Spinach"
    @patch('builtins.input',return_value=y)
    def test_veg_select(self,mock_input):

        result1= TestVegEasy.a.select()
        
        self.assertIn("Bread", result1)
        self.assertIn("Flour", result1)
        self.assertIn("Rice", result1)
        self.assertIn("Potato", result1)
        self.assertIn("Lentils", result1)
    
    x=["Sandwich","Hot chocolate
Bread
Veg Sushi
Carrot paratha
French fries
Pasta
Onion rings
Mozerella Cheese sticks
Oats Upma
Indian Dal
Chopsuey
Arabiata pasta
Corn and cheese
Spinach paratha
Bread Manchurian
Milk Shake
Crepes
Fried rice
Carrot soup
Twisted potato
Brocolli paratha
Cheesy Onions
Cheese cake
"Health bar"
,"Dal soup","Fried noodles","White sauce pasta", "Corn Crackers","Palak paneer"]
    @patch('builtins.input',return_value=x)
    def test_veg_search(self,mock_input):
        result2= TestVegEasy.a.search()
        
        self.assertIn("Flavoured rice", result2)
        self.assertIn("Roti", result2)
        self.assertIn("Carrot Salad", result2)
        self.assertIn("Garlic bread", result2)
        self.assertIn("Flavoured rice", result2)