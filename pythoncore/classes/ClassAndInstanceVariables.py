__author__ = 'veradocs-web'

class Dog:
    kind = 'canine'         # class variable shared by all instances
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


d=Dog('bibhu')
e=Dog('prakash')
print d.kind
print e.kind


class Dog:
    tricks = []       # mistaken use of a class variable

    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)


dd=Dog('world')
ee=Dog('india')
dd.add_trick("UK")
ee.add_trick("USA")

print dd.tricks

class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog
    def add_trick(self, trick):
        self.tricks.append(trick)



d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print d.tricks
print e.tricks



