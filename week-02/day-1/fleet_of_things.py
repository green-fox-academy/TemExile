from fleet import Fleet
from thing import Thing

fleet = Fleet()
thing1 = Thing('Get milk')
thing2 = Thing('Remove the obstacles')
thing3 = Thing('Stand up')
thing4 = Thing('Eat lunch')
thing3.complete()
thing4.complete()
fleet.add(thing1)
fleet.add(thing2)
fleet.add(thing3)
fleet.add(thing4)
print(fleet)