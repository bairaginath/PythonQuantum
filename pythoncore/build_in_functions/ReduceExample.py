__author__ = 'veradocs-web'

print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))


def reduce1(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value


def add(x,y):
    return x+y

print(reduce1(add,[1, 2, 3, 4, 5]))
