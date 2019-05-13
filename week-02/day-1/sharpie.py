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
    def __init__(self, list):
        self.list = list
    def count_usable(self):
        a = 0
        for i in range(len(self.list)):
            if sharpie.ink_amount(self.list[i]) > 0:
                a += 1
        return a
    def remove_trash(self):
        b = []
        for i in range(len(self.list)):
            if sharpie.ink_amount(self.list[i]) > 0
                b.append(self.list[i])
        return b

