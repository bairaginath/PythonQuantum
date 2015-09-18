__author__ = 'veradocs-web'


try:
    x=('4'+5)/0

except (RuntimeError, TypeError, NameError ) as err :
    print str(err)
except Exception,err:
    print str(err)



import sys

# The last except clause may omit the exception name(s), to serve as a wildcard. Use this with extreme caution,
# since it is easy to mask a real programming error in this way! It can also be used to print an error message and then re-raise the exception
# (allowing a caller to handle the exception as well):


try:
    f = open('test.txt')
    s = f.readline()
    i = int(s.strip())
    # x=5/0
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise




for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()

#commond line argument pass list of file name and then it reads one by one if it doesn't throws any exceptioin
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()





def returnValueFromTryExcept(n):
    try:
       p=69/n
       return "try block"
    except Exception,err:
       return "catch block"
    finally:
        return "finally block"






try:
     raise Exception('spam', 'eggs')
except Exception as inst:
    print type(inst)     # the exception instance
    print inst.args      # arguments stored in .args
    print inst           # __str__ allows args to be printed directly
    x, y = inst.args
    print 'x =', x
    print 'y =', y


# The problem with this code is that it leaves the file open for an indeterminate amount of time after the code has finished executing.
# This is not an issue in simple scripts, but can be a problem for larger applications. The with statement allows objects like files to be used in a way that ensures
# they are always cleaned up promptly and correctly.

for line in open("test.txt"):
    print line,

with open("test.txt") as f:
    for line in f:
        print line,






if __name__ == '__main__':
   print(returnValueFromTryExcept(2))
   print(returnValueFromTryExcept(0))



