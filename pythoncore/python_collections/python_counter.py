__author__ = 'veradocs-web'

from collections import Counter


# Tally occurrences of words in a list
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1

print(cnt)


c = Counter()                           # a new, empty counter
c = Counter('gallahad')                 # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
c = Counter(cats=4, dogs=8)             # a new counter from keyword args

c = Counter(['eggs', 'ham'])
print(c['bacon'])                              # count of a missing element is zero

# Setting a count to zero does not remove an element from a counter. Use del to remove it entirely
c['sausage'] = 0                        # counter entry with a zero count
del c['sausage']                        # del actually removes the entry


# Return an iterator over elements repeating each as many times as its count. Elements are returned in arbitrary order.
#  If an elements count is less than one, elements() will ignore it.

c = Counter(a=4, b=2, c=0, d=-2)
print(list(c.elements()))

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print (c)




