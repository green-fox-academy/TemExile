class Person(object):
    def __init__(self, name = 'Jane Doe', age = 30, gender = 'female'):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        return f'Hi, I\'m {self.name}, a {self.age} year old {self.gender}.'
    def get_goal(self):
        return f'My goal is :Live for the moment!'

class
