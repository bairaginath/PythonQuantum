__author__ = 'veradocs-web'

MyString="bairagira"
print(MyString.capitalize())
print(MyString.center(10))
print(MyString.count("ra"))
print(MyString.encode("base64")) #The default is 'strict', meaning that encoding errors raise UnicodeError
base64String=MyString.encode('base64')
print(base64String.decode('base64'))

#read more methods go to  https://docs.python.org/2/library/stdtypes.html

MyString='bairagi'
print(MyString.rpartition('a'))
