import pandas as pd
import unittest
import recipes.NonVeg.nutrition as n

class TestNutrition(unittest.TestCase):
    def setUp(self):
        self.x=pd.read_csv("/Users/dishadh/Desktop/data533 collaborative soft dev/DATA533_Lab2/Recipes.csv")
    def test_easy_cal(self):
        self.assertEqual(n.edisplay(self.x, "Boiled eggs", 0), 155)
        self.assertEqual(n.edisplay(self.x, "Tea", 2), 1)
        self.assertEqual(n.edisplay(self.x, "Pan fried fish", 6), 233)
        self.assertEqual(n.edisplay(self.x, "Stir fried brocolli", 9), 99)
        self.assertEqual(n.edisplay(self.x, "Sprouts", 13), 43)
    def test_medium_cal(self):
        self.assertEqual(n.mdisplay(self.x, "Sandwich", 1), 497)
        self.assertEqual(n.mdisplay(self.x, "Crepes", 3), 90)
        self.assertEqual(n.mdisplay(self.x, "Fish fingers", 6), 249)
        self.assertEqual(n.mdisplay(self.x, "Twisted potato", 8), 606)
        self.assertEqual(n.mdisplay(self.x, "Chopsuey", 14), 290)
    def test_diff_cal(self):
        self.assertEqual(n.ddisplay(self.x, "Devils eggs", 0), 200)
        self.assertEqual(n.ddisplay(self.x, "Kulfi", 2), 206)
        self.assertEqual(n.ddisplay(self.x, "Chicken Biryani", 5), 400)
        self.assertEqual(n.ddisplay(self.x, "Cajun spiced potato", 8), 165)
        self.assertEqual(n.ddisplay(self.x, "Lasagna", 15), 302)

unittest.main(argv=[''], verbosity=2, exit=False)