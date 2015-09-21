__author__ = 'veradocs-web'


class GrandParents:
      def __init__(self):
          pass
      def display_grandparents(self):
          print "In Side Grand Parents"


class Parents(GrandParents):
      def __init__(self):
          pass
      def display_parents(self):
          print "In Side Parents"

class Child(Parents):
    def __init__(self):
        pass
    def display_child(self):
        print "In Side Child"




if __name__ == '__main__':
    child=Child()
    child.display_grandparents()
    child.display_parents()
    child.display_child()

