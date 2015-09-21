class Parent(object):
    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"
dad = Parent()
son = Child()
dad.altered()
son.altered()


class Parent1(object):
    def altered(self):
        print "In Side Parent1"

class Parent2(object):
    def altered(self):
        print "In Side Parent2"

class Child1(Parent1,Parent2):
    def altered(self):
        print "In Side Child1"
        super(Child1, self).altered()


son = Child1()
son.altered()