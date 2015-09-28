__author__ = 'veradocs-web'

# Return a new frozenset object, optionally with elements taken from iterable. frozenset is a built-in class. See frozenset and Set Types set, frozenset for documentation
# about this class.


# frozensets are immutable (you cannot add or remove elements from them)

mylist = [0,1,2,3]
myset = set(mylist)
# sets are mutable, we can add and remove elements
myset.add(4)
print(myset)
myfrozenset = frozenset(mylist)
# frozensets are immutable, you cannot add or remove elements
try:
  myfrozenset.add(4)
except AttributeError,err:
    print str(err)



