__author__ = 'veradocs-web'

for element in [1, 2, 3]:
    print element
for element in (1, 2, 3):
    print element
for key in {'one':1, 'two':2}:
    print key
for char in "123":
    print char

# The use of iterators pervades and unifies Python. Behind the scenes, the for statement calls iter() on the container object.
# The function returns an iterator object that defines the method next() which accesses elements in the container one at a time.
# When there are no more elements, next() raises a StopIteration exception which tells the for loop to terminate

s = 'abc'
it = iter(s)
print it

print it.next()
print it.next()
print it.next()
try:
  it.next()
except StopIteration:
    print "no next element"


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev=Reverse("spam")
for i in rev:
    print i
