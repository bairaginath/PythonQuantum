__author__ = 'veradocs-web'

class Parent(object):
    def __init__(self):
        print "PARENT __init__()"

class Child(Parent):
    def __init__(self):
        print "CHILD, BEFORE PARENT __init__()"
        super(Child, self).__init__()
        print "CHILD, AFTER PARENT __init__()"
dad = Parent()
son = Child()



class Parent1(object):
    def __init__(self):
        print "In Side Parent1"

class Parent2(object):
    def __init__(self):
        print "In Side Parent2"

class Child1(Parent1,Parent2):
    def __init__(self):
        print "In Side Child1"
        super(Child1, self).__init__()


son = Child1()

class Animal(object):
    def __init__(self):
        print "in side animal"


class Dog(Animal):
    def __init__(self):
        print "in side dog"

dog=Dog()

