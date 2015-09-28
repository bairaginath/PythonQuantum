__author__ = 'veradocs-web'

#this file is running successfully because execfile will import these method runtime


execfile('simple_functions.py')

print(is_perfect_square(144))

print(even_numbers_only([0,5,8,12,55,48]))

namespace = {}
execfile('simple_functions.py', namespace)
print(namespace['is_perfect_square'](144))