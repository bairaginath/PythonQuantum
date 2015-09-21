__author__ = 'veradocs-web'


import weakref, gc
# The weakref module provides tools for tracking objects without creating a reference.
# When the object is no longer needed, it is automatically removed from a weakref table and a callback is triggered for weakref objects.
# Typical applications include caching objects that are expensive to create
class A:
     def __init__(self, value):
         self.value = value
     def __repr__(self):  # act as toString() same as java toString()
         return str(self.value)

a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
print d['primary']                # fetch the object if it is still alive

del a                       # remove the one reference
gc.collect()                # run garbage collection right away

# d['primary']                # entry was automatically removed #KeyError: 'primary'
