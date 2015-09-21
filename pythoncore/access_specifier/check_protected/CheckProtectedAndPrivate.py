__author__ = 'veradocs-web'

from pythoncore.access_specifier.protected_private.ProtectedAndPrivateAccess import Person


# print "In side CheckProtected file for Person._age ",Person._age #AttributeError: class Person has no attribute '_age'
print "In side CheckProtected file for Person._myAge ",Person._myAge
person=Person("tapan",23,54000)

print "In side CheckProtected file for person._age ",person._age
print "In side CheckProtected file for person._myAge ",person._myAge


# print person.__sal #AttributeError: Person instance has no attribute '__sal'
# print Person.__mySal #AttributeError: Person instance has no attribute '__mySal'
# print person.__double_underscore_method() #AttributeError: Person instance has no attribute '__get_salary'

print "In side CheckProected file for Private access ",person._Person__double_underscore_method()

