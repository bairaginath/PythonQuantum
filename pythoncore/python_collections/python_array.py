__author__ = 'veradocs-web'

# The array module provides an array() object that is like a list that stores only homogeneous data and stores it more compactly.
# The following example shows an array of numbers stored as two byte unsigned binary numbers (typecode "H") rather than
# the usual 16 bytes per entry for regular lists of Python int objects:


from array import array
a = array('H', [4000, 10, 700, 22222])
print sum(a)

print a

print a[1:3]


