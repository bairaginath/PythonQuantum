import itertools

__author__ = 'veradocs-web'


# The collections module provides a deque() object that is like a list with faster appends and pops from the left side but slower lookups in the middle.
# These objects are well suited for implementing queues and breadth first tree searches:

from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print "Handling", d.popleft()


# unsearched = deque([starting_node])
# def breadth_first_search(unsearched):
#     node = unsearched.popleft()
#     for m in gen_moves(node):
#         if is_goal(m):
#             return m
#         unsearched.append(m)


# Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.


d = deque('ghi')                 # make a new deque with three items
for elem in d:                   # iterate over the deque's elements
     print elem.upper()


d.append('j')                    # add a new entry to the right side
d.appendleft('f')                # add a new entry to the left side
print(d)                                # show the representation of the deque


print(d.pop())                          # return and remove the rightmost item
print(d.popleft())                      # return and remove the leftmost item

print(list(d))                          # list the contents of the deque


print(list(reversed(d)))                # list the contents of a deque in reverse

'h' in d                         # search the deque

d.extend('jkl')                  # add multiple elements at once
print d

d.rotate(1)                      # right rotation i.e d.appendleft(d.pop()).
print(d)
d.rotate(-1)                     # left rotation
print(d)

deque(reversed(d))               # make a new deque in reverse order
deque(['l', 'k', 'j', 'i', 'h', 'g'])
d.clear()                        # empty the deque

try:
    d.pop()  # cannot pop from an empty deque
except IndexError,err:
    print("pop from an empty deque")

d.extendleft('abc')              # extendleft() reverses the input order
print(d)


def tail(filename, n=10):
    'Return the last n lines of a file'
    return deque(open(filename), n)




def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / float(n)


print(list(moving_average([40, 30, 50, 46, 39, 44])))


def delete_nth(d, n):
    d.rotate(-n)
    d.popleft()
    d.rotate(n)

d=deque([1,2,3,4,5])
delete_nth(d,2) # equivalence to del d[n]
print(d)