import random
class DiceSet(object):
    def __init__(self):
        self.dices = [0, 0, 0, 0, 0, 0]
    def roll(self):
        for i in range(len(self.dice)):
            self.dices[i] = random.randint(1, 6)
        return self.dices
    def get_current(self, index = None):
        if index != None:
            return self.dices[index]
        else:
            return self.dices
    def reroll(self, index = None):
        if index != None:
            self.dices[index] = random.randint(1, 6)
        else:
            self.roll()
    def getnum(self, num = 6):
        for j in range(len(self.dices)):
            while self.dices[j] != num:
                self.reroll(j)
        return self.dices

a = DiceSet()
a.getnum()
print(a.dices)
