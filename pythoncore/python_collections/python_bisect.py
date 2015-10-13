__author__ = 'veradocs-web'

 # bisect module with functions for manipulating sorted lists
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print scores

a=[8,3,5,1,6,4,9,2]

a.sort()
print a
#Locate the insertion point for x in a to maintain sorted order.
# If x is already present in a, the insertion point will be before (to the left of) any existing entries.
print(bisect.bisect_left(a,7))

print(bisect.bisect_right(a,7))
# Similar to bisect_left(), but returns an insertion point which comes after (to the right of) any existing entries of x in a.
print(bisect.bisect(a,7))

#Insert x in a in sorted order. This is equivalent to a.insert(bisect.bisect_left(a, x, lo, hi), x) assuming
# that a is already sorted. Keep in mind that the O(log n) search is dominated by the slow O(n) insertion step.
bisect.insort_left(a,7)
print(a)
bisect.insort_right(a,0)
print(a)
bisect.insort(a,99)
print(a)



def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect.bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect.bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


print(index(a,4))
print(find_le(a,4))
print(find_lt(a,4))
print(find_gt(a,4))
print(find_ge(a,4))


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
        i = bisect.bisect(breakpoints, score)
        return grades[i]

print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])


data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
data.sort(key=lambda r: r[1])
keys = [r[1] for r in data]         # precomputed list of keys
print(data[bisect.bisect_left(keys, 0)])

print(data[bisect.bisect_left(keys, 1)])

print(data[bisect.bisect_left(keys, 5)])

print(data[bisect.bisect_left(keys, 8)])

