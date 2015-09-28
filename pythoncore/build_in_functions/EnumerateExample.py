__author__ = 'veradocs-web'


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=1)))

# Equivalent to:

def enumerate1(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1


print(list(enumerate1(seasons)))
print(list(enumerate1(seasons, start=1)))


