import unittest
import math

from Circle import Circle

class test_Circle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(Circle(4).area(), 4*4*math.pi)

    def test_perimeter(self):
        self.assertEqual(Circle(4).perimeter(), 2*4*math.pi)

if __name__ == '__main__':
    unittest.main()
