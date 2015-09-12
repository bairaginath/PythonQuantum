__author__ = 'veradocs-web'



class World:
    instance=None
    # def __init__(self,value=None):
    #     self.value=value
    def get_instance(self,value=None):
        if self.instance:
           self.instance=World(value)
           return self.instance
        else:
           return self.instance




x=World.get_instance(5)
print x
y=x.get_instance()
print y



