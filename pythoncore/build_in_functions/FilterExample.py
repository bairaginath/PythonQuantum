__author__ = 'veradocs-web'

def starts_with_vowel(the_str):
     vowels = ['a', 'e', 'i', 'o', 'u']
     if len(the_str) == 0:
             return False
     return the_str[0].lower() in vowels


words = ["hello", "apple", "excellent", "dictionary", "our"]
print(filter(starts_with_vowel, words))

items = ["", {}, "hi", {"x": 10}, [], [""], None, False, True]

print(filter(None, items))

from itertools import ifilter
x=ifilter(lambda x: x%2, range(10))
print (x.next())
print (x.next())
print (x.next())
print (x.next())
print (x.next())

from itertools import ifilterfalse
x=ifilterfalse(lambda x: x%2, range(10))
print (x.next())
print (x.next())
print (x.next())
print (x.next())
print (x.next())




