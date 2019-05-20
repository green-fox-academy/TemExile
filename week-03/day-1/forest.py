class WhitebarkPine(object):
    def __init__(self, height = 0):
        self.height = height
    def irrigate(self):
        self.height += 2
    def getHeight(self):
        return self.height
class foxtailPin(object):
    def __init__(self, height = 0):
        self.height = height
    def irrigte(self):
        self.height += 1
    def getHeight(self):
        return self.height

class Lumberjack(object):
    def __init__(self, tree):
        self.tree = tree
    def canCut(self, tree):
        if tree.height > 4:
            return True
        else:
            return False

class forest(object):
    
