__author__ = 'veradocs-web'

class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

c=C()
c.x=5
print (c.x)
del c.x


class CC(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

cc=CC()
cc.x=4
print(cc.x)
del cc.x



class CCC(object):
    def __init__(self):
        self._x = None

    @property
    def getValue(self):
        """I'm the 'x' property."""
        return self._x

    @getValue.setter
    def setValue(self, value):
        self._x = value

    @getValue.deleter
    def deleteValue(self):
        del self._x

ccc=CCC()
ccc.setValue=6
print(ccc.getValue)
del ccc.deleteValue

