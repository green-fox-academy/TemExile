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