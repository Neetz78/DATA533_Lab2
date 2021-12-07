import pandas as pd
import unittest
import recipes.Veg.nutrition as n

class TestNutrition(unittest.TestCase):
    def setUp(self):
        self.x=pd.read_csv("/Users/dishadh/Desktop/data533 collaborative soft dev/DATA533_Lab2/Recipes.csv")
    def test_easy_cal(self):
        self.assertEqual(n.edisplay(self.x, "Butter toast", 1), 310)
        self.assertEqual(n.edisplay(self.x, "Tea", 2), 1)
        self.assertEqual(n.edisplay(self.x, "Carrot Salad", 7), 238)
        self.assertEqual(n.edisplay(self.x, "Stir fried brocolli", 9), 99)
        self.assertEqual(n.edisplay(self.x, "Sprouts", 13), 43)
    def test_medium_cal(self):
        self.assertEqual(n.mdisplay(self.x, "Sandwich", 1), 497)
        self.assertEqual(n.mdisplay(self.x, "Crepes", 3), 90)
        self.assertEqual(n.mdisplay(self.x, "French fries", 8), 312)
        self.assertEqual(n.mdisplay(self.x, "Twisted potato", 8), 606)
        self.assertEqual(n.mdisplay(self.x, "Chopsuey", 14), 290)
    def test_diff_cal(self):
        self.assertEqual(n.ddisplay(self.x, "Rabdi", 2), 252)
        self.assertEqual(n.ddisplay(self.x, "Kulfi", 2), 206)
        self.assertEqual(n.ddisplay(self.x, "Veg Biryani", 4), 241)
        self.assertEqual(n.ddisplay(self.x, "Cajun spiced potato", 8), 165)
        self.assertEqual(n.ddisplay(self.x, "Lasagna", 15), 302)

unittest.main(argv=[''], verbosity=2, exit=False)