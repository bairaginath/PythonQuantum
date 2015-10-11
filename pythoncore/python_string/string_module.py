__author__ = 'veradocs-web'


#string constants
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.letters)
print(string.octdigits)
print(string.punctuation)
print(string.printable)
print(string.uppercase)
print(string.whitespace)
from string import Formatter
print(Formatter().format("my name is {0}.I am from {state}",'bairagi',state='odisha'))
print(Formatter().vformat("my name is {0}.I am from {state}",['bairagi'],{"state":'odisha'}))
it=Formatter().parse(Formatter().vformat("my name is {0}.I am from {state}",['bairagi'],{"state":'odisha'}))
print(it.next())
#get_fields
#get_value


from string import Template
s = Template('$who likes $what')
print(s.substitute(who='tim', what='kung pao'))
d = dict(who='tim')
print(Template('$who likes $what').safe_substitute(d))


# String functions
print(string.capwords("bairagi nath"))

print(string.maketrans("kuna","imit"))

print(string.split(" bairagi nath  "))
print(string.splitfields("bairagi nath  "))

print(string.join('kpc',","))
print(string.joinfields('kpc',","))

print(string.translate("bairagi",string.maketrans("abcdefghijklm","nopqrstuvwxyz")))
