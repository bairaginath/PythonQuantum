__author__ = 'veradocs-web'


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b





if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]))
