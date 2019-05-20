class Clownfish(object):
    def __init__(self):
        self.name = 'clownfish'
        self.weight = 8
        self.color = 'blue'
        self.memory = False
    def feed(self):
        self.weight += 1

class Tang(object):
    def __init__(self):
        self.name = 'tang'
        self.weight = 4
        self.color = 'red'
        self.memory = True
    def feed(self):
        self.weight += 1

class Kong(object):
    def __init__(self):
        self.name = 'Koi'
        self.weight = 8
        self.color = 'black'
        self.memory = False
    def feed(self):
        self.weight += 2

class aquarium(object):
    def __init__(self, fishlist = []):
        self.fishlist = fishlist
    def addfish(self, newfish):
        self.fishlist.append(newfish)
    def feed(self):
        for fish in self.fishlist:
            fish.feed()
    def rmbig(self):
        for fish in self.fishlist:
            if fish.weight >= 11:
                self.fishlist(fish)
    def getInfo(self):
        for fish in self.fishlist:
            print(f'{fish.name}, Weight: {fish.weight},'
            f'color: {fish.color}, short-term memory loss: {fish.memory}')
