__author__ = 'veradocs-web'

# The heapq module provides functions for implementing heaps based on regular lists.
# The lowest valued entry is always kept at position zero. This is useful for applications which repeatedly access the smallest element
# but do not want to run a full list sor

from heapq import heapify, heappop, heappush,heappushpop
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
# Push the value item onto the heap, maintaining the heap invariant.
heappush(data, -5)                 # add a new entry
print [heappop(data) for i in range(3)]  # fetch the three smallest entries

print(heappushpop(data,32))

# Pop and return the smallest item from the heap, and also push the new item. The heap size doesnot change.
# If the heap is empty, IndexError is raised.
import heapq
print(heapq.heapreplace(data,19))
print(heapq.heapreplace(data,1)) #The value returned may be larger than the item added. If that isnot desired, consider using heappushpop() instead.


# Merge multiple sorted inputs into a single sorted output (for example,
# merge timestamped entries from multiple log files).
# Returns an iterator over the sorted values.
pp=heapq.merge([1,3,5,7],[2,4,6,8])
# Return a list with the n largest elements from the dataset defined by iterable.print(list(pp))
#Equivalent to: sorted(iterable, key=key, reverse=True)[:n]
print(heapq.nlargest(5,data))
# Return a list with the n smallest elements from the dataset defined by iterable.
#Equivalent to: sorted(iterable, key=key)[:n]
print(heapq.nsmallest(3,data))

def heapsort(iterable):
     h = []
     for value in iterable:
         heappush(h, value)
     return [heappop(h) for i in range(len(h))]
print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

# Heap elements can be tuples. This is useful for assigning comparison values (such as task priorities) 
# alongside the main record being tracked:

h = []
heappush(h, (5, 'write code'))
heappush(h, (7, 'release product'))
heappush(h, (1, 'write spec'))
heappush(h, (3, 'create tests'))
print(heappop(h))



