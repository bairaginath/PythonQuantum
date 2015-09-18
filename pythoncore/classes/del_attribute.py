__author__ = 'veradocs-web'



class Person():
    country="india"
    def __init__(self,age,name):
        self.age=age
        self.name=name

    def delete_country(self):
        del Person.country

    def get_country(self):
        try:
           return Person.country
        except AttributeError,err:
           return "country deleted"




p=Person(age=55,name='bairagi')
print (p.__dict__)

del p.age
print (p.__dict__)
print "person country "+p.country
p.delete_country()
print (p.get_country())
try:
   print (Person.country)
except AttributeError,err:
    print "Country already deleted "

