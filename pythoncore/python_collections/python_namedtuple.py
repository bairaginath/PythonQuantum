__author__ = 'veradocs-web'

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'], verbose=True)

# Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code.
# They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.



p = Point(11, y=22)     # instantiate with positional or keyword arguments
#Returns a new tuple subclass named typename. The new subclass is used to create tuple-like objects that have fields accessible by
# attribute lookup as well as being indexable and iterable.

print(p[0] + p[1])             # indexable like the plain tuple (11, 22)
x, y = p                # unpack like a regular tuple
print(x,y)
print(p.x + p.y )              # fields also accessible by name
                    # readable __repr__ with a name=value style
Point(x=11, y=22)

t = [11, 22]
print(Point._make(t))
print( p._asdict())

p = Point(x=11, y=22)
print(p._replace(x=33))

p._fields            # view the field names

Color = namedtuple('Color', 'red green blue')
Pixel = namedtuple('Pixel', Point._fields + Color._fields)
print(Pixel(11, 22, 128, 255, 0))

print(getattr(p, 'x'))

d = {'x': 11, 'y': 22}
print(Point(**d))


