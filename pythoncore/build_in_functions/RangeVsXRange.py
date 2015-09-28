__author__ = 'veradocs-web'

"""
    xrange(stop) -> xrange object
    xrange(start, stop[, step]) -> xrange object

    Like range(), but instead of returning a list, returns an object that
    generates the numbers in the range on demand.  For looping, this is
    slightly faster than range() and more memory efficient.
    """

print(range(10))
print(xrange(10))
print([x for x in xrange(10)])