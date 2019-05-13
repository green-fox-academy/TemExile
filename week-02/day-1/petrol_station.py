class Car(object):
    def __init__(self, gas_amount = 0, capacity = 100):
        self.gas_amount = gas_amount
        self.capacity = capacity


class station(object):
    def __init__(self, gas_amount):
        self.gas_amount = gas_amount
    def refill(self,car):
        self.gas_amount -= (car.capacity - car.gas_amount)
        car.gas_amount = car.capacity

a = Car()
b = station(500)
b.refill(a)
print(b.gas_amount)