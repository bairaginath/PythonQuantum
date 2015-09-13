__author__ = 'veradocs-web'

t = 12345, 54321, 'hello!'
print (t[2])

u = t, (1, 2, 3, 4, 5)
print u

try:
    t[0]="bairagi"
except TypeError, err:
    print str(err) +"   tuple is immutable object"

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print (set(basket))

a = set('abracadabra')
b = set('alacazam')
print a
print b

print ("set comprehension "+str({x  for x in "abcabrdacp"}))

mydict=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print mydict

print ("dict comprehension "+str({x: x**2 for x in (2, 4, 6,2)}))

print ("dict string pair "+str(dict(sape=4139, guido=4127, jack=4098)))

