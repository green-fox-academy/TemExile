import unittest
from extension_modified import add, max_of_three, median, is_vovel, translate

class TestExtend(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,2), 4)
    
    def test_max_of_three(self):
        self.assertEqual(max_of_three(3,1,8), 8)
    
    def test_median(self):
        self.assertEqual(median([2,3,1,5,6]), 3)
    
    def test_is_vovel(self):
        self.assertEqual(is_vovel('f'), False)
    
    def test_translate(self):
        self.assertEqual(translate('apple'), 'avappleve')

if __name__ == '__main__':
    unittest.main()