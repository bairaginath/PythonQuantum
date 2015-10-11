__author__ = 'veradocs-web'

MyStr=str("baAiragi")

#The concatenation of x and y.
print(MyStr.__add__('nath'))

#n shallow copies of x concatenated.
print(MyStr.__mul__(3))
#x%y

# print(MyStr.__mod__(2))
# n shallow copies of x concatenated.
print(MyStr.__rmul__(4))
# y-th item of x, origin 0.
print(MyStr.__getitem__(2)) #Index Error in n item is not there
# Iterator over bytes.
# it=MyStr.__iter__()
# print(it.next())

# Return a copy of the string with its first character capitalized and the rest lowercased.
print(MyStr.capitalize())
#Return centered in a string of length width.
print(MyStr.center(15,"*"))
# Return the number of non-overlapping occurrences of substring sub in the range [start, end].
print(MyStr.count('gi'))

print(MyStr.encode("base64")) #The default is 'strict', meaning that encoding errors raise UnicodeError
base64String=MyStr.encode('base64')
print(base64String.decode('base64'))
#Return True if the string ends with the specified suffix,otherwise return False.
print(MyStr.endswith('gi'))
print(MyStr.endswith('ag'))
# Return a copy of S where all tab characters are expanded using spaces.If tabsize is not given, a tab size of 8 characters is assumed.
print(str("bairagi\tnath").expandtabs(15))


#Return the lowest index in the string where substring sub is found, such that sub is contained in the slice s[start:end].
print(MyStr.find('ir'))
print(MyStr.find('ier')) #if not present it return -1
#Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end].
print(str('bairagi').rfind('a'))
print(str('bairagi').rfind('e'))
#Like find(), but raise ValueError when the substring is not found.
print(MyStr.index('ir'))
# print(MyStr.index('ier')) #trows Value Error
#Like rfind(), but raise ValueError when the substring is not found.
print(str('bairagi').rindex('a'))
#print(str('bairagi').rindex('e')) #ValueError

# Return a formatted version of S, using substitutions from args and kwargs.The substitutions are identified by braces ('{' and '}').
print("My name is {0}.I am from {state}".format('bairagi',state='odisha'))

#Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise.
print(MyStr.isalnum())
print(str('3432').isalnum())
print(str('.#@1as').isalnum())
#Return true if all characters in the string are alphabetic and there  is at least one character, false otherwise.
print(str('.#1').isalpha())
print(str('ae').isalpha())
#Return true if all characters in the string are digits and there is at least one character, false otherwise.
print(str('343e').isdigit())
print(str('343').isdigit())
#Return true if all cased characters in the string are lowercase and there is at least one cased character, false otherwise.
print(str('aserAsdfe')).islower()
print(str('asersdfe')).islower()

#Return true if there are only whitespace characters in the  string and there is at least one character, false otherwise.
print(str('aser dse').isspace())
print(str('aserdse').isspace())
print(str(' ').isspace())
#Return true if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones.
print(str('aserAser').istitle())
print(str('Aserser').istitle())

#Return true if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones.
print(str('AUPM').isupper())
print(str('AUPMa').isupper())
# Return a string which is the concatenation of the strings in the iterable
print(str(',').join(['bairagi','nath','behera']))
#Return the string left justified in a string of length width.Padding is done using the specified fillchar (default is a space).
print(MyStr.ljust(15,'*'))

#Return a copy of the string with all the cased characters converted to lowercase.
print(MyStr.lower())
#Return a copy of the string with left leading characters removed. default space
print(str('   bairagi').lstrip())
print(str(',,bairagi').lstrip(','))
#Return a copy of the string with right leading characters removed. default space
print(str('bairagi  ').rstrip())
print(str('bairagi,,').rstrip(','))
#Return a copy of the string with left and right leading characters removed. default space
print(str('  bairagi  ').strip())
print(str(',,,bairagi,,,').strip(','))
#Split the string at the first occurrence of sep, and
# return a  3-tuple containing the part before the separator, the separator itself, and the part after the separator.
print(str('bairagi').partition('a'))
#Return a copy of the string with all occurrences of substring old replaced by new.
print(str('bairagi').replace('a','e'))
print(str('bairagi').replace('l','e'))
# Return the string right justified in a string of length width.Padding is done using the specified fillchar (default is a space).
print(str('bairagi').rjust(15,"*"))

# Split the string at the last occurrence of sep, and return a
#     3-tuple containing the part before the separator, the separator
#     itself, and the part after the separator.
print(str('bairagi').rpartition('a'))

# Return a list of the words in the string, using sep as the
    #     delimiter string.
print(str('bairagi').rsplit('a'))
# Return a list of the words in the string, using sep as the
    #     delimiter string.
print(str('bairagi').split('a'))
# Return a list of the lines in the string, breaking at line boundaries.
print(str('bairagi\nnath').splitlines())
# Return True if string starts with the prefix, otherwise return False.
print(str('bairagi').startswith('a'))
print(str('Bairagi').startswith('b'))
print(str('Bairagi').startswith('B'))
# Return a copy of the string with uppercase characters converted  to lowercase and vice versa.
print(str('BaIrAGi')).swapcase()

# Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.
print(str('bairagi nath').title())

#Return a copy of the string with all the cased characters converted to uppercase.
print(str('bairagi').upper())

#Return the numeric string left filled with zeros in a string of length width.
print(str('bairagi').zfill(15))








