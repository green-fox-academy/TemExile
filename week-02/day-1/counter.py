class Counter(object):
    def __init__(self, value = 0):
        self.value = value
        self.ori = value
    def add(self, number = 1):
        self.value += number
    def get(self):
        return self.value
    def reset(self):
        self.value = self.ori
