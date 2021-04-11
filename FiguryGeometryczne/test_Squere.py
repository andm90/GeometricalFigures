import unittest

from Squere import Squere

class test_Squere(unittest.TestCase):

    def test_area(self):
        self.assertEqual(Squere(3).area(), 9)

    def test_perimeter(self):
        self.assertEqual(Squere(3).perimeter(), 12)
        

if __name__ == '__main__':
    unittest.main()
