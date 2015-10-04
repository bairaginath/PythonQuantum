from collections import defaultdict
import itertools

__author__ = 'veradocs-web'


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
     d[k].append(v)

print(d.items())


d = {}
for k, v in s:
    d.setdefault(k, []).append(v)
    

print(d.items())

s = 'mississippi'
d = defaultdict(int)
for k in s:
     d[k] += 1

d.items()

def constant_factory(value):
    return itertools.repeat(value).next
d = defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
print('%(name)s %(action)s to %(object)s' % d)
