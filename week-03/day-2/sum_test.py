from Sum import Sum
import unittest

class test_Sum(unittest.TestCase):
    def test_list(self):
        a = Sum([1,2,3,4,5])
        self.assertEqual(a.get_sum(), 15)
    def test_empty(self):
        b = Sum([])
        self.assertEqual(b.get_sum(), 0)
    def test_one(self):
        c = Sum([1])
        self.assertEqual(c.get_sum(), 1)
    def test_none(self):
        d = Sum([None])
        self.assertEqual(d.get_sum(), None)


if __name__ == '__main__':
    unittest.main()