import importlib

class ReflectionExample(object):
      def getMethod(self):
          print "inside get method"





if __name__ == '__main__':
    refObject=getattr(importlib.import_module('pythoncore.reflection.reflection_example'),"ReflectionExample")
    refObject().getMethod()