from anagram import Anagram
import unittest

class anagram_test(unittest.TestCase):
    def test_str_right(self):
        self.assertEqual(Anagram('alllalla', 'allallla'), True)
    def test_str_wrong(self):
        self.assertEqual(Anagram('asdf', 'uiop'), False)

if __name__ == '__main__':
    unittest.main()