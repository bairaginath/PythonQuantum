__author__ = 'veradocs-web'

print "Container Abstract Base Class"
from collections import Container
print(Container.__subclasshook__(list))
print(Container.__subclasshook__(dict))
print(Container.__subclasshook__(set))
print(Container.__subclasshook__(tuple))
import string
print(Container.__subclasshook__(string))

class WorldContainer(Container):
    def __contains__(self, item):
        return False

print(Container.__subclasshook__(WorldContainer))
print(WorldContainer().__contains__(4))

print "Hashable Abstract Base Class"

from collections import Hashable
print(Hashable.__subclasshook__(string))

class WorldCHashable(Hashable):
    def __hash__(self, item):
        return id(item)

print(Hashable.__subclasshook__(WorldCHashable))
print(WorldCHashable().__hash__(4))


# to read more details https://docs.python.org/2/library/collections.html