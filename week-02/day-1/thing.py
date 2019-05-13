class Thing:
    def __init__(self, name):
        self.name = name
        self.completed = False
    def complete(self):
        self.completed = True
    def __str__(self):
        return ("[x] " if self.completed else "[ ] ") + self.name

thing1 = Thing('Get milk')
thing2 = Thing('Remove the obstacles')
thing3 = Thing('Stand up')
thing4 = Thing('Eat lunch')
thing3.complete()
thing4.complete()
print(thing1,thing2, thing3, thing4)