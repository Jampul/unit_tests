import unittest
from circle import circle_area
from math import pi

class testCircleArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(circle_area(3), pi*3**2)
        self.assertEqual(circle_area(1), pi)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(2.5), pi*2.5**2)

    def test_values(self):
        self.assertRaises(ValueError, circle_area, -2)
        self.assertRaises(ValueError, circle_area, -1)

    def test_types(self):
        self.assertRaises(TypeError, circle_area, 5+2j)
        self.assertRaises(TypeError, circle_area, 'five')
        self.assertRaises(TypeError, circle_area, [6, 4])
        self.assertRaises(TypeError, circle_area, [64])
        self.assertRaises(TypeError, circle_area, True)