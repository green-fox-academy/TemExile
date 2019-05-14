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
        if amno_storage >= self.max_amno:
            amno_storage -= self.max_amno
            self.amno = self.max_amno
        else:
            self.amno += amno_storage
            amno_storage = 0
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

class carrier(object):
    def __init__(self, amno_storage, hp):
        self.aircrafts = []
        self.amno = amno_storage
        self.hp = hp
    def add(self, aircraft):
        self.aircrafts.append(aircraft)
    def fill(self):
        if self.amno == 0:
            print('There is no amno to fill.')
        else:
            i = j = 0
            while self.aircrafts[i].amno == 0 and self.aircrafts[i].priority == True and self.amno != 0:
                self.aircrafts[i].refill(self.amno)
                i += 1
            while self.aircrafts[j].amno == 0 and self.amno != 0:
                self.aircrafts[i].refill(self.amno)
                j += 1
    def fight(self, otherCarrier):
        damage = 0
        for i in range(len(self.aircrafts)):
            damage += self.aircrafts[i].fight()
            otherCarrier.hp -= damage
    def getStatus(self):
        