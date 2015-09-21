__author__ = 'veradocs-web'


country="india"

class Employee():
    dept_no=5444

    def __init__(self,eno,name):
        self.eno=eno
        self.name=name
    def get_details(self):
        print "in side first method ", self.dept_no,self.eno,self.name,country
        pass

    @staticmethod
    def get_details():
        print "in side first static method ",Employee.dept_no,country

    def get_details(self):
        print "in side second method ", self.dept_no,self.eno,self.name,country
        pass

# if this  method commented then this throuws  TypeError: unbound method get_details() must be called with Employee instance as first argument (got nothing instead)
    @staticmethod
    def get_details():
        print "in side second static method ",Employee.dept_no,country

emp=Employee(44,"bairagi")
emp.get_details() # it calls static method
Employee.get_details()


class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

x=MyClass()
fun=x.f #valid method reference
fun1=MyClass.f #valid function call









