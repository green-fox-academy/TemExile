class Sum(object):
    def __init__(self, numberlist):
        self.numberlist = numberlist
    def get_sum(self):
        a = 0
        if None in self.numberlist:
            return None
        elif len(self.numberlist) == 0:
            return 0
        else:
            return sum(self.numberlist)
    
