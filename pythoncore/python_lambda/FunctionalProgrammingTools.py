__author__ = 'veradocs-web'


def f(x): return x % 3 == 0 or x % 5 == 0

# filter(function, sequence) returns a sequence consisting of those items from the sequence for which function(item) is true.
print "filter "+str(filter(f, range(2, 25)))
print "filter with lambda "+str(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(2, 25)))
print "filter on tuple "+str(filter(lambda x: x % 3 == 0 or x % 5 == 0, (1,2,3,4,5,6,7,)))


# map(function, sequence) calls function(item) for each of the sequence items and returns a list of the return values
print "map "+str(map(f, range(2, 25)))
print "map with lambda "+str(map(lambda x: x % 3 == 0 or x % 5 == 0, range(2, 25)))
print "map on tuple "+str(map(lambda x: x % 3 == 0 or x % 5 == 0, (1,2,3,4,5,6,7,)))

print "map with two squence "+str(map(lambda x,y:x+y,[1,2,3],[4,5,6]))


def add(x,y): return x+y
# reduce(function, sequence) returns a single value constructed by calling the binary function function on the first two items of the sequence, then on the result and the next item, and so on
print "reduce "+str(reduce(add, range(1,11),5))
print "reduce "+str(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])) #calculates  ((((1+2)+3)+4)+5)


print "list comprehensions "+str([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12,25],]

#convert two dimension to one dimension
print ([row[column] for row in matrix for column in range(len(row))])

#transpose of matrix
print ([[row[i] for row in matrix] for i in range(4)])

print ("zip "+str(zip(*matrix)))

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print ("del first index "+str(a))
del a[2:4]
print ("del 2:4 index "+str(a))
del a[:]
print ("del all "+str(a))
try:
  del a
  print ("del object"+str(a))
except NameError,err:
    print (str(err))

