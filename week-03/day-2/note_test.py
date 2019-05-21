from note_function import add
import unittest

print(add(2,3))
assert add(2,3), 5

class TestMynotefunction(uittest.TestCase):
    def test_add(self):
        actual  = add (2,3)
        expected = 5
        self.asserteQUAL(AttributeError, expected, '2 + 3 must be 5')
    def test_nagative(self):
        self.asserteQUAL(add(-2.5, -1.0), -3.5)
    def tet compe:

if __name__'__main':
    unittest.main()