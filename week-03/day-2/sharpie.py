class sharpie(object):
    def __init__(self, color, width, ink_amount = 100.00):
        self.color = color
        self.width = width
        self.ink_amount = ink_amount
    def use(self, amount):
        self.ink_amount -= amount