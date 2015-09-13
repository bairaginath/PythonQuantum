__author__ = 'veradocs-web'


appendlist=[1,2,3]
list=[4,5,6]
extendlist=[1,2,3]
appendlist.append(list)
print appendlist
extendlist.extend(list)
print extendlist


def compare(item1, item2):
    if item1 < item2:
        return -1
    elif item1 > item2:
        return 1
    else:
        return


def name_filter(person):
    return person.name

def compare_object(item1, item2):
    if name_filter(item1) < name_filter(item2):
        return -1
    elif name_filter(item1) > name_filter(item2) :
        return 1
    else:
        return 0


list=[5,4,2,6,1,3]
lambda_list=list
list.sort(cmp=compare)
print "sorted  "+str(list)

lambda_list.sort(cmp=lambda x,y:cmp(x,y))
print "sorted  "+str(lambda_list)

class Person():
    def __init__(self,age,name):
        self.age=age
        self.name=name


personList=[Person(55,"rajib"),Person(65,"bairagi"),Person(44,"kuna")]
lambdaPersonList=personList
personList.sort(cmp=compare_object)
print ([person.name for person in personList])

lambdaPersonList.sort(cmp=lambda x,y:cmp(x,y),key=name_filter)
print ([person.name for person in lambdaPersonList])




