from apple import Apple
import unittest

class Test_apple(unittest.TestCase):
    def test_apple(self):
        abc = Apple()
        self.assertEqual(abc.get_apple(), 'apple')
    
    def test_orange(self):
        ccc = Apple()
        self.assertEqual(ccc.get_apple(), 'orange')

if __name__ == '__main__':
    unittest.main()
