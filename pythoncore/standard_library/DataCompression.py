__author__ = 'veradocs-web'


import zlib
s = 'witch which has which witches wrist watch'
print len(s)
t = zlib.compress(s)
len(t)
print t
print zlib.decompress(t)
