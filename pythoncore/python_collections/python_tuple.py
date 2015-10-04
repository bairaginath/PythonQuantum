__author__ = 'veradocs-web'


t = 12345, 54321, 'hello!'
print (t[2])

u = t, (1, 2, 3, 4, 5)
print u

try:
    t[0]="bairagi"
except TypeError, err:
    print str(err) +"   tuple is immutable object"