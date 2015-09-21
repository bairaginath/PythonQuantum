__author__ = 'veradocs-web'


class Person:
     __mySal=None #private static variable
     _myAge=None  #protected static variable
     def __init__(self,name,age,sal):
         self.name=name
         self._age=age #protected instance variable
         self.__sal=sal #private instance variable
         self._myAge=age # initialize protected static variable
         self.__mySal=sal

     # private method
     def __double_underscore_method(self):
         return self.__sal,self.__mySal

     def _single_underscore_method(self):
         return self._age,self._myAge
     def get_details(self):
         return self.name,self._age,self._myAge,self.__sal,self.__mySal,self._single_underscore_method(),self.__double_underscore_method()




person=Person("bairagi",28,56000)

print person.get_details()
print person._age
# print Person._age #AttributeError: class Person has no attribute '_age'
print person._myAge
print Person._myAge
print person._single_underscore_method()
# print person.__sal #AttributeError: Person instance has no attribute '__sal'
# print Person.__mySal #AttributeError: Person instance has no attribute '__mySal'
# print person.__double_underscore_method() #AttributeError: Person instance has no attribute '__get_salary'

print person._Person__double_underscore_method()

