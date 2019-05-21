from Count_letter import count_letter
import unittest

class count_letter_test(unittest.TestCase):
    def test_words(self):
        self.assertEqual(count_letter('aaabbbccc'), {
            'a':3, 'b':3, 'c':3
        })
    def test_sentence(self):
        self.assertEqual(count_letter('I have apples'),{
            "I":1, 'h':1, 'a':2, 'v':1, 'e':2, 'p':2, 'l':1, 's':1
        })

if __name__ == '__main__':
    unittest.main()