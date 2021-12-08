import pandas as pd
import unittest
from unittest.mock import patch
from recipes.Veg import difficult as dv
class TestVegDifficult(unittest.TestCase):
    def setUp(self):
        self.x=pd.read_csv("Recipes.csv")
        TestVegDifficult.a=dv.difficult(self.x)
    y = "Bread Milk Flour Rice Carrot Potato Brocolli Onion Cheese Oats Lentils Noodles Pasta Corn Spinach"
    @patch('builtins.input',return_value=y)
    def test_veg_select(self,mock_input):

        result1= TestVegDifficult.a.select()
        
        self.assertIn("Potato", result1)
        self.assertIn("Milk", result1)
        self.assertIn("Spinach", result1)
        self.assertIn("Cheese", result1)
        self.assertIn("Flour", result1)
    
    x=["Bread pakoda","Rabdi","Tacos","Veg Biryani","Carrot Cake","Aloo paratha","Brocolli manchurian","French onion soup","Corn and cheese momos","Oats pancake","Dal paratha","Wonton noodle soup","Lasagna","Corn pakoda","Spinach ravioli","Bread Upma","Kulfi","Muffins","Dosa","Carrot halwa","Cajun spiced potato","Brocolli base pizza","Onion paratha","Cheesy Pizza","Oats cookie","Dal pakoda","Veggie garlic noodles","Ravioli pasta","Corn soup","Spinach chaat"]
    @patch('builtins.input',return_value=x)
    def test_veg_search(self,mock_input):
        result2= TestVegDifficult.a.search()
        
        self.assertIn("Bread pakoda", result2)
        self.assertIn("Spinach ravioli", result2)
        self.assertIn("Oats pancake", result2)
        self.assertIn("Ravioli pasta", result2)
        self.assertIn("Spinach chaat", result2)