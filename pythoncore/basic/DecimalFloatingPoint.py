__author__ = 'veradocs-web'

from decimal import *
x = Decimal('0.70') * Decimal('1.05')
print x
print x.quantize(Decimal('0.01'))  # round to nearest cent

print round(.70 * 1.05, 2)         # same calculation with floats



print Decimal('1.00') % Decimal('.10')



print sum([Decimal('0.1')]*10) == Decimal('1.0')

print  sum([0.1]*10) == 1.0

getcontext().prec = 36
print  Decimal(1) / Decimal(7)
