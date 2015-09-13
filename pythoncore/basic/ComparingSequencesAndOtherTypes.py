__author__ = 'veradocs-web'

plist=[1,2,3,4]
qlist=[1,2,3,4]
pset=set(plist)
qset=set(qlist)
print id(plist)
print id(qlist)
print id(pset)
print id(qset)
print (plist is qlist)
print (pset is qset)

qlist=plist
qset=qset

print id(plist)
print id(qlist)
print id(pset)
print id(qset)
# is operator compare with id of the object
print (plist is qlist)
print (pset is qset)




string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print non_null


print (1, 2, 3) < (1, 2, 4)
print [1, 2, 3] < [1, 2, 4]
print 'ABC' < 'C' < 'Pascal' < 'Python'
print (1, 2, 3, 4)< (1, 2, 4)
print (1, 2)< (1, 2, -1)
print (1, 2, 3)== (1.0, 2.0, 3.0)
print (1, 2, ('aa', 'ab'))< (1, 2, ('abc', 'a'), 4)


