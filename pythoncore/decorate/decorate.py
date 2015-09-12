__author__ = 'veradocs-web'


def logger(func):
    print "before display"
    def world(*args, **kwargs):
        print "inside inner"
        return func(*args, **kwargs)
    return world






@logger
def display(x,y=1):
    print "in side display with parameter"
    return x*y










if __name__ == '__main__':
    display(1,2)

