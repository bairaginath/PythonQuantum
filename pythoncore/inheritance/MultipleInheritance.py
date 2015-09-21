__author__ = 'veradocs-web'


class Parent1():
      def __init__(self):
          pass
      # def display_parents(self):
      #     print "In Side Parent1"


class Parent2():
      def __init__(self):
          pass
      def display_parents(self):
          print "In Side Parent2"


class Parent3():
      def __init__(self):
          pass
      def display_parents(self):
          print "In Side Parent3"



class Child(Parent1,Parent2,Parent3):
    def __init__(self):
        pass
    def display_child(self):
        print "In Side Child"


if __name__ == '__main__':
     child=Child()
     child.display_parents()



