__author__ = 'veradocs-web'


def if_elif_else():
    x = int(raw_input("Please enter an integer: "))
    if x < 0:
       x = 0
       print 'Negative changed to zero'
    elif x == 0:
        print 'Zero'
    elif x == 1:
         print 'Single'
    else:
        print 'More'





def no_increment_for_loop():
    i=0
    while i<10:
        print i
        i+=1

def for_loop():
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print w, len(w)

# xrange is a sequence object that evaluates lazily. range creates a list, so if you do range(1, 10000000) it creates a list in memory with 10000000 elements.
# xrange is a generator, so it is a sequence object is a that evaluates lazily

def myrange():
    for i in xrange():
        print i


def myxrange():
    for i in xrange(0,10,2):
        print i

def break_elseclause_example():
    for n in range(10):
        for x in range(2, n):
            if n%x==0:
               print n, 'equals', x, '*', n/x
               break
        else:
            # loop fell through without finding a factor
            print n, 'is a prime number'
        # the else clause belongs to the for loop, not the if statement.a loop’s else clause runs when no break occurs

def continue_example():
    for num in range(2, 10):
        if num % 2 == 0:
           print "Found an even number", num
           continue
        print "Found an odd number", num










if __name__ == '__main__':
    # if_elif_else()
    # no_increment_for_loop()
    # for_loop()
    # myrange()
    # myxrange()
    # break_elseclause_example()
    continue_example()



