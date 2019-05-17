import random
class pirate(object):
    def __init__(self):
        self.alcohol = 0
        self.sleep = False
        self.alive = True
    def drink_some_rum(self):
        if not self.alive:
            print('The pirate is dead')
        self.alcohol += 1
    def how_it_going_mate(self):
        if not self.alive:
            print('The pirate is dead')
            return None
        if self.alcohol < 5:
            print('Pour')
        else:
            self.sleep = True
            print('I\'m a Pirate. How d\'ya d\'ink its goin?')
    def die(self):
        self.alive = False
    def brawl(self, other):
        output = random.randint(0,2)
        if output == 0:
            other.die()
        elif output == 1:
            self.die()
        elif output == 2:
            self.sleep = True
            other.sleep = True

class ship:
    def __init__(self):
        self.pirates = []
        self.captain = None
    def fill_ship(self):
        self.captain = pirate()
        for i in range(randint(0,11)):
            self.piartes.append(pirate())
    def count_alive(self):
        return len(list(filter(lambda pirate: pirate.alive, self.pirates)))
    def false_not(self, boolean):
        if not boolean:
            return "not"
        return ""
    def __str__(self):
        alivepirateCount = self.count_alive()
        return f'The captain consumed {self.captain.alcohol} rum and he is {self.captain.sleep} '\
        f'passed out and {self.captain.alive} died. And the ship has {alivepirateCount} pirates'