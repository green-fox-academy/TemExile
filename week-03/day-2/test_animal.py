import unittest
from animals import Animal

class test_Animal(unittest.TestCase):
    def test_constructor(self):
        a = Animal()
        self.assertEqual(a.thirst, 50)
        self.assertEqual(a.hunger, 50)
    
    def test_activities(self):
        a = Animal()
        a.eat()
        self.assertEqual(a.hunger, 49)
        a.drink()
        self.assertEqual(a.thirst, 49)
        a.play()
        self.assertEqual(a.thirst, 50)
        self.assertEqual(a.hunger, 50)

if __name__ == '__main__':
    unittest.main()

