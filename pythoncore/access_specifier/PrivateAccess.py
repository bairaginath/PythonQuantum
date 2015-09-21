__author__ = 'veradocs-web'


class Person:
     def __init__(self,name,age,sal):
         self.name=name
         self.age=age
         self.__sal=sal #private variable

     # private method
     def __get_salary(self):
         return self.__sal

     def get_income(self):
         return self.name,self.__sal
     def get_details(self):
         return self.__get_salary()




person=Person("bairagi",33,56000)

print person.get_details()
print person.get_income()
# print person.__get_salary() #AttributeError: Person instance has no attribute '__get_salary'
# print person.__sal #AttributeError: Person instance has no attribute '__sal'

