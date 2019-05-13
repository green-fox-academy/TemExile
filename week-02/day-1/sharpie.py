class sharpie(object):
    def __init__(self, color, width, ink_amount = 100.00):
        self.color = color
        self.width = width
        self.ink_amount = ink_amount
    def use(self, amount):
        self.ink_amount -= amount

exp1 = sharpie(color = 'white', width = 2.3)
exp1.use(31.3)
print(exp1.ink_amount)

class sharpieset(object):
    def __init__(self):
        self.list = []
    def adding(self):
        self.list.append(sharpie('white',1.2,23))
        self.list.append(sharpie('black',5.0,12))
        self.list.append(sharpie('yellow',12.0,0))
        self.list.append(sharpie('black',2.0,40))
        self.list.append(sharpie('blue',1.0,0))
    def count_usable(self):
        a = 0
        for i in range(len(self.list)):
            if self.list[i].ink_amount > 0:
                a += 1
        return a
    def remove_trash(self):
        b = []
        for i in range(len(self.list)):
            if self.list[i].ink_amount > 0:
                b.append(self.list[i])
            return b

aaa = sharpieset()
aaa.adding()
print(aaa.count_usable())


