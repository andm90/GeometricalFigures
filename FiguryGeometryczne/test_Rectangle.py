import unittest

from Rectangle import Rectangle

class test_Rectangle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(Rectangle(2,4).area(), 8)

    def test_perimeter(self):
        self.assertEqual(Rectangle(2,4).perimeter(), 12)

if __name__ == '__main__':
    unittest.main()
