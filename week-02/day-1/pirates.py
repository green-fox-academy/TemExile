class pirate(object):
    def __init__(self, rum_amount = 0):
        self.rum_amount = rum_amount
    def drink_some_rum(self):
        self.rum_amount += 1
        return self.rum_amount
    def hows_it_going_mate(self):
        return ['Pour me anudder!', 'Arghh, I\'m a Pirate. How d\'ya d\'ink its goin?'][self.rum_amount >= 5]
