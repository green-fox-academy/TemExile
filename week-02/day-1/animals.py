class Animal(object):
    def __init__(self, hunger = 50, thirst = 50):
        self.hunger = hunger
        self.thirst = thirst
    def eat(self):
        self.hunger -= 1
    def drink(self):
        self.thirst -= 1
    def play(self):
        self.hunger += 1
        self.thirst += 1

dog = Animal()
dog.play()
print(dog.hunger)

class Farm(object):
    def __init__(self, list, slots):
        self.list = list
        self.slots = slots
    def breed(self, animal):
        if self.slots > 0:
            self.list.append(animal)
            self.slots -= 1

    def slaughter(self):
        c = []
        for j in range(len(self.list)):
            c.append(self.list[j].hunger)
        self.list.pop(c.index(min(c)))
        return self.list
animal1 = Animal()
animal2 = Animal()
animal3 = Animal()
animal1.play()
animal2.eat()
animal2.eat()
animal3.eat()
a = [animal1, animal2, animal3]
print(len(a))
farm1 = Farm(a, slots=3)
farm1.slaughter()
print(farm1.list)
