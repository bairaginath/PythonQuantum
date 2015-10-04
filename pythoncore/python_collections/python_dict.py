__author__ = 'veradocs-web'


mydict=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print mydict

print ("dict comprehension "+str({x: x**2 for x in (2, 4, 6,2)}))

print ("dict string pair "+str(dict(sape=4139, guido=4127, jack=4098)))


a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)

p=iter(d)
print p.next()
print p.next()
print p.next()
# print p.next() #throws StopIteration

pp=d.iterkeys() #return keys as iterator

for k,v in d.iteritems():
    print k,v

#please visit more details go to https://docs.python.org/2/library/stdtypes.html







# The objects returned by dict.viewkeys(), dict.viewvalues() and dict.viewitems() are view objects.
#  They provide a dynamic view on the dictionary's entries, which means that when the dictionary changes, the view reflects these changes.


dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.viewkeys()
values = dishes.viewvalues()

# iteration
n = 0
for val in values:
     n += val
print(n)


# keys and values are iterated over in the same order
print(list(keys))
print(list(values))


# view objects are dynamic and reflect dict changes
del dishes['eggs']
del dishes['sausage']
print(list(keys))
print(list(values))

















