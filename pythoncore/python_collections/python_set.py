__author__ = 'veradocs-web'


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print (set(basket))

a = set('abracadabra')
b = set('alacazam')
print a
print b

print ("set comprehension "+str({x  for x in "abcabrdacp"}))

print(set([1,3])> set([1,2]))
print(set([1,3,2])> set([1,2])) #Test whether the set is a proper superset of other, that is, set >= other and set != other.
print(set([1,3,2])>= set([1,2])) #Test whether every element in other is in the set.

print(set([1,2])<set([1,3]))
print(set([1,2])<set([1,3,2])) #Test whether the set is a proper subset of other, that is, set <= other and set != other.
print(set([1,2])<=set([1,3,2])) #Test whether every element in the set is in other.




A=set([1,2,3,4])
B=set([3,4,5,6])
C=set([7,8,9,10])
print(A.isdisjoint(B))
print(A.isdisjoint(C))
D=set([1,2])
print(D.issubset(A))
print(A.issuperset(D))
print(A.intersection(B))
print(A.union(B))
print(A.difference(B))
print(A.symmetric_difference(B))
print(A.copy()) #Return a new set with a shallow copy of s.

print(set('abc') == frozenset('abc'))

AU=set([1,2,3,4])
A=AU
BU=set([3,4,5,6])
AU.update(BU)
print AU
AU=A
AU.intersection_update(BU)
print AU,BU
AU=A
AU.difference_update(B)
print AU,B

AU=A
AU.symmetric_difference_update(B)
print AU,B

A.add(19)
print(A)
A.remove(19) #Raises KeyError if elem is not contained in the set.
print (A)

A.discard(3) #if elem is not contained in the set.it doesnot throws any error
print A

print(A.pop()) #Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.

A.clear()
print(A)

# To support searching for an equivalent frozenset, the elem set is temporarily mutated during the search and then restored.






