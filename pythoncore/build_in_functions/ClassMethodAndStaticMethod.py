__author__ = 'veradocs-web'

class MyClass(object):
     x = 10
     @classmethod
     def f1(cls):
         return 2 * cls.x
     @staticmethod
     def f2():
         return 2 * MyClass.x




print (MyClass.f1())
print (MyClass.f2())


class MySubClass(MyClass):
      x = 20


# if we were to subclass MyClass and change the value of x, the class method f1() would automatically account for it while the static method f2()
# would still refer to the old x.



print (MySubClass.f1())
print (MySubClass.f2())