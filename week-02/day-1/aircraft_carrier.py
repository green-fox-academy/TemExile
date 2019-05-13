class aircraft(object):
    def __init__(self, type, amno, base_damage, priority):
        self.type = type
        self.amno = amno
        self.base_damage = base_damage
        self.priority = priority
        self.max_amno = amno
    def fight(self):
        total_damage = self.base_damage * self.amno
        self.amno = 0
        return total_damage
    def refill(self,amno_storage):
        amno_storage -= self.max_amno
        self.amno = self.max_amno
        return amno_storage
    def getType(self):
        return f'{self.type}'
    def getStatus(self):
        return f'Type {self.type}, Amno: {self.amno}, Base Damage: {self.base_damage}, All Damage: {self.amno * self.base_damage}'
    def isPriority(self):
        return f'{self.priority}'

air1 = aircraft('F16', 8, 30, False)
air2 = aircraft('F35', 12, 50, True)
print(air1.getStatus())
air1.fight()
print(air1.getStatus())
air1.refill(500)
print(air1.refill(500))
print(air1.getStatus())

