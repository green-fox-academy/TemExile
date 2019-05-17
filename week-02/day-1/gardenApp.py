class flower(object):
    def __init__(self, name, status, type = 'flower'):
        self.name = name
        self.status = status
        self.type = type
    def water(self, amount):
        self.status += 0.75 * amount

class tree(object):
    def __init__(self, name, status, type = 'tree'):
        self.name = name
        self.status = status
        self.type = type
    def water(self, amount):
        self.status += 0.4 * amount

class garden(object):
    def __init__(self, list, need_water = 0, needed = []):
        self.list = list
        self.need_water = need_water
        self.needed = needed
    def check(self):
        self.need_water = 0
        for i in range(len(self.list)):
            if self.list[i].type == 'flower':
                if self.list[i].status < 5:
                    self.need_water += 1
                    self.needed.append(self.list[i])
                    print(f'The {self.list[i].name} needs water')
                else:
                    print(f'The {self.list[i].name} dosent need water')
            else:
                if self.list[i].status < 10:
                    self.need_water += 1
                    self.needed.append(self.list[i])
                    print(f'The {self.list[i].name} needs water')
                else:
                    print(f'The {self.list[i].name} dosent need water')
    def water(self, amount):
        if self.need_water != 0:
            water_amount = amount/self.need_water
            for i in range(len(self.needed)):
                if self.needed[i].type == 'flower':
                    flower.water(self.needed[i], water_amount)
                else:
                    tree.water(self.needed[i], water_amount)
        self.needed = []
        print(f'Watering with {amount}')

flower1 = flower('yellow Flower', 4)
flower2 = flower('blue Flower', 4)
tree1 = tree('purple Tree', 9)
tree2 = tree('orange Tree', 9)

plant = [flower1, flower2, tree1, tree2]

garden1 = garden(list = plant)
print('\n')
garden1.check()
print('\n')
garden1.water(40)
print('\n')
garden1.check()
print('\n')
garden1.water(70)
print('\n')
garden1.check()

