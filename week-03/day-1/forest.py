class WhitebarkPine(object):
    def __init__(self, height = 0):
        self.height = height
        self.name = 'WhintebarPin'
    def irrigate(self):
        self.height += 2
    def getHeight(self):
        return self.height
class foxtailPin(object):
    def __init__(self, height = 0):
        self.height = height
        self.name = 'FoxtailPin'
    def irrigte(self):
        self.height += 1
    def getHeight(self):
        return self.height

class Lumberjack(object):
    def canCut(self, tree):
        if tree.height > 4:
            return True
        else:
            return False

class forest(object):
    def __init__(self, treelist = []):
        self.treelist = treelist
    def addTree(self, newtree):
        self.treelist.append(newtree)
    def rain(self):
        for tree in self.treelist:
            tree.irrigate()
    def cutTrees(self):
        for tree in self.treelist:
            a = Lumberjack()
            if a.canCut(tree):
                self.treelist.remove(tree)
    def isEmpty(self):
        return [True, False][len(self.treelist)!=0]
    def getStatus(self):
        statuslist = []
        for tree in self.treelist:
            info = f'There is a {tree.getHeight()} tall {tree.name} in the Forest.'
            statuslist.append(info)
        return statuslist