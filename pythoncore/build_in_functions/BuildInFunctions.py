__author__ = 'veradocs-web'


print abs(-33.56)

print (all([1,2,3]))
print (all([1,2,None,3]))

print (any([1,2]))
print (any([]))

# (Technically, basestring is the superclass of str and unicode, but it cannot be directly instantiated. Thus its direct use is mostly limited to type checking.)
a=u'aaaa'
print (isinstance(a, basestring))
print (isinstance(a, str))

# Convert an integer x to a binary string.

print (bin(10))

print (bool("bairagi"))
print (bool())
print (bool(None))

b = bytearray("Hello, world!")
print b[0]

# Return True if the object argument appears callable, False if not.

def summ(x,y):
    return x+y
print callable(summ)
x = 10
print callable(x)
class MyClass(object):
     pass
print callable(MyClass)

obj = MyClass()
print callable(obj)

print(chr(43))

print (cmp(8,4))
print (cmp(4,8))
print (cmp(4,4))

print (complex(4, 2))
print (complex("4+2j"))


class MyClass(object):
     def __init__(self):
         self.x = 10

obj = MyClass()
obj.x
delattr(obj, "x")
try:
  print obj.x
except AttributeError,err:
    print err



print(dict(x=2,y=3))
print(dict([['x',2],['y',5]]))

import struct
print(dir(struct))
class Shape(object):
        def __dir__(self):
            return ['area', 'perimeter', 'location']

print (dir(Shape()))


class Shape1(object):
      pass

print (dir(Shape1()))
print (divmod(5,2))

print(eval("5+5"))

myglobals = {"x": 2, "y": 3}
print(eval('x+y', myglobals))

# It is not recommended to use the file() function. Instead, use open().
f=file("simple_functions.py","r+")
print(isinstance(f, file))

print(float(10))
print(type(format(10.10)))

class MyClass(object):
     x = 0
     def getX(self):
         return self.x
obj=MyClass()
print(getattr(obj,"x"))
print(getattr(obj,"getX")())
print(hasattr(obj,'x'))
print(hasattr(obj,'y'))




print(hash("bairagi")) #Return the hash value of the object

# help([object]) Invoke the built-in help system

print hex(255) #Convert an integer number (of any size) to a lowercase hexadecimal string prefixed with '0x'

print(id(444))#Return the "identity" of an object.

print(int())
print(int(9))

print(isinstance("bairagi",str))
print(issubclass(str,basestring))

it=iter(range(3))
print it.next()
print it.next()
print it.next()
print("len "+str(len([1,2,3])))
print(list(iter([1,2,3])))


print(long(33))

def check_even(x,y):
    return x*y
print(map(check_even,range(10),range(10)))

print(max([1,2,3,4]))
print(max(5,3,[1,2,3,4])) #If two or more positional arguments are provided, the largest of the positional arguments is returned.

v = memoryview('abcefg')
print(v[1:4].tobytes())
data = bytearray('abcefg')
v = memoryview(data)


print(next(iter([1,2,3])))


print(oct(x)) # Convert an integer number (of any size) to an octal string. The result is a valid Python expression.

f=open("simple_functions.py")
print(type(f))

print(ord('A')) #Given a string of length one, return an integer representing the Unicode code point of the character

print(object())

print(pow(2,3))
print(pow(2,3,8))
print(2**3)

print(range(10))


import math
print(math.factorial(5))
r=reload(math)
print(r.factorial(5))

# Return a string containing a printable representation of an object
class ABC:
    pass
print(repr(ABC))
print(repr(ABC()))

print(list(reversed([1,2,3]))) #Return a reverse iterator

print(set([2,3,1,3]))

class ABCD:
    def __init__(self):
        self.footbar=None

abcd=ABCD()
setattr(abcd,'footbar',55)
print(abcd.footbar)






print(slice(6))
print(slice(1,6,2))
a=range(10)
print(a[slice(1,8,2)])


print(sorted([4,2,3,1,5]))

print(sum([1,2,3,4,5]))

print(tuple([1, 2, 3]))

# Return the Unicode string of one character whose Unicode code is the integer i. For example, unichr(97) returns the string u'a'.

print(unichr(97))

print(unicode(ABC))
print(unicode(ABC()))

#Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute.
# print(vars())
print(vars(ABC))
print(vars(ABC()))



x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(zipped)

p=__import__("math")
print(p.factorial(5))


# Non-essential Built-in Functions
#apply,buffer,coerce,intern

