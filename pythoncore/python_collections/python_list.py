__author__ = 'veradocs-web'

appendlist=[1,2,3]
list=[4,5,6]
extendlist=[1,2,3]
appendlist.append(list)
print appendlist
extendlist.extend(list)
print extendlist

list.insert(2,2)
print list

list.insert(10,87)
print(list)
try:
  list.remove(25)
except ValueError,err:
  print str(err)

list=[1,2,3,4,5,6,7,8,9,10,7,7,99]
print(list.pop()) #Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
print(list.pop(7))

print(list.index(5))
try:
  list.index(25)
except ValueError,err:
  print str(err)

print(list.count(7))
print(list.count(1))
print(list.count(55))
list=[1,2,3]
list.reverse()
print list
