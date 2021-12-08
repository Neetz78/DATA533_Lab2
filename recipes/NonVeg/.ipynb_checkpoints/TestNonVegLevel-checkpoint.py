import pandas as pd
import unittest
from unittest.mock import patch
import recipes.NonVeg.nveg as env

class TestNonVegLevel(unittest.TestCase):
    
    y = "Easy Medium Hard"
    @patch('builtins.input',return_value=y)
        
    def test_nonveg_level(self,mock_input):
        result= env.level()
        self.assertIn("Easy", result)
        
unittest.main(argv=[''], verbosity=2, exit=False)