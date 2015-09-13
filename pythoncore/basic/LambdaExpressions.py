__author__ = 'veradocs-web'


# The general syntax of a lambda function is quite simple:
# lambda argument_list: expression
# The argument list consists of a comma separated list of arguments and the expression is an arithmetic expression using these arguments.
# You can assign the function to a variable to give it a name.

f=lambda x,y:x+y
print f(1,2)


def make_increment(n):
    """
    :param n:
    :return:
    intialize then constant,then increment it by using lambda function
    """
    return lambda x:x+n




fun=make_increment(54)
print fun(5)
print fun(10)
print make_increment.__doc__