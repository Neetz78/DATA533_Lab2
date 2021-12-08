import pandas as pd
import unittest
from unittest.mock import patch
import recipes.Veg.veg as ev

class TestVegLevel(unittest.TestCase):
    
    y = "Easy Medium Hard"
    @patch('builtins.input',return_value=y)
        
    def test_veg_level(self,mock_input):
        result= ev.level()
        self.assertIn("Easy", result)
        
unittest.main(argv=[''], verbosity=2, exit=False)