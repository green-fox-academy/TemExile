import random
class pirate(object):
    def __init__(self, rum_amount = 0, status):
        self.rum_amount = rum_amount
        self.status = status
    def drink_some_rum(self):
        self.rum_amount += 1
        return self.rum_amount
    def hows_it_going_mate(self):
        if self.rum_amount >= 5:
            self.status = 'pass out'
        return ['Pour me anudder!', 'Arghh, I\'m a Pirate. How d\'ya d\'ink its goin?'][self.rum_amount >= 5]
    def die(self):
        self.status = 'dead'
    def brawl(self, otherPirate):
        a = random.randint(0,2)
        if a == 0:
            self.status = 'dead'
        elif a == 1:
            otherPirate.status = 'dead'
        else:
            self.status = 'dead'
            otherPirate.status = 'dead'
