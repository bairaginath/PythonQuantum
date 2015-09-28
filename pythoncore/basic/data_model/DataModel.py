__author__ = 'veradocs-web'

# Python's six constants living in the built-in namespace
# i.e  False, True, None, Ellipsis, __debug__,Ellipsis, NotImplemented, NotImplemented

# NotImplemented, then the runtime would fall back to the built-in behaviour for equality which is based on object identity
# which in CPython, is the object's address in memory.

print bool(None)

# Numeric methods and rich comparison methods may return this value if they do not implement the operation for the operands provided.

class Person:
     def __init__(self,name):
         self.name=name



NotImplemented="bairagi"
print NotImplemented
NotImplemented="raj"
print NotImplemented

print bool(NotImplemented)
print(NotImplemented.__eq__("raj"))
print(NotImplemented.__lt__("bairagi"))
print(NotImplemented.__add__("bairagi"))

p1=Person("bairagi")
p2=Person("kuna")
# p1.__eq__(p2) #AttributeError: Person instance has no attribute '__eq__'
# NotImplemented=p1
print(NotImplemented.__eq__(p2))


class TestEllipsis(object):
     def __getitem__(self, item):
         if item is Ellipsis:
             return "Returning all items"
         else:
             return "return %r items" % item

x = TestEllipsis()
print x[2]
print x[...]

print bool(Ellipsis)
print bool(TestEllipsis)

