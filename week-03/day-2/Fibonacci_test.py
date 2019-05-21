from Fibonacci import fibonacci
import unittest

class fibonacci_test(unittest.TestCase):
    def test_len_0(self):
        self.assertEqual(fibonacci(0), 'Please enter a valid index')
    def test_len_1(self):
        self.assertEqual(fibonacci(1), [0])
    def test_len_2(self):
        self.assertEqual(fibonacci(2), [0,1])
    def test_len_6(self):
        self.assertEqual(fibonacci(6), [0,1,1,2,3,5,8])

if __name__ == '__main__':
    unittest.main()