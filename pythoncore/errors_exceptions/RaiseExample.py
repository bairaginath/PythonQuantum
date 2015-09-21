__author__ = 'veradocs-web'


class B:
    pass
class C(B):
    pass
class D(C):
    pass

for c in [B, C, D]:
    try:
        raise c #raise using Class Name
    except D:
        print "D"
    except C:
        print "C"
    except B:
        print "B"



for c in [B, C, D]:
    try:
        raise c()  #raise using class Instance
    except D:
        print "D"
    except C:
        print "C"
    except B:
        print "B"


for c in [B, C, D]:
    try:
        raise c().__class__   #raise using instance class name
    except D:
        print "D"
    except C:
        print "C"
    except B:
        print "B"
