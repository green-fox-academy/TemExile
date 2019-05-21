import unittest
from sharpie import sharpie

class test_Sharpie(unittest.TestCase):
    def test_use_twice_with_defult(self):
        a = sharpie('black', 1.2)
        self.assertEqual(a.ink_amount, 100)
        a.use(10)
        a.use(10)
        self.assertEqual(a.ink_amount, 80)
        self.assertEqual(a.width, 1.2)
        self.assertEqual(a.color, 'black')
        
    def test_different_initial_ink_with_use(self):
        a = sharpie('black', 1.5, 80)
        self.assertEqual(a.ink_amount, 80)
        a.use(5)
        self.assertEqual(a.ink_amount, 75)

if __name__ == '__main__':
    unittest.main()
