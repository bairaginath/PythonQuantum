__author__ = 'veradocs-web'
import math
def getNthMagicNumber(n):
	return int(round(math.sqrt(2*n)))


def input(L,R):
	S=0
	while(L<=R):
		S=S+getNthMagicNumber(L)
		L=L+1
	M=(10**9)+7
	return S%M


# print(input(7,17))


def calculate(speed,fuel):
    return (50000/fuel)*speed
print(map(calculate,[250,240,230,220,210,211],[5000,4500,4000,3500,3000,3000]))


import sys
sys.argv



# f(n) = 3 * f(n-1) + 2 * f(n-2) + 2 * g(n-1)+3 * g(n-2) , g(n) = g(n-1) + 2 * g(n-2).


def f(n,f0,f1,g0,g1):
    if n==0:
       return f0
    if n==1:
       return f1
    return 3*f(n-1,f0,f1,g0,g1)+2*f(n-2,f0,f1,g0,g1)+2*g(n-1,g0,g1)+3*g(n-2,g0,g1)



def g(n,g0,g1):
    if(n==0):
       return g0
    if(n==1):
       return g1
    return g(n-1,g0,g1)+2*g(n-2,g0,g1)

xx=f(4,1,1,1,1)
print xx



def anagrams_test(A,B):
       if len(A)!=len(B):
          return "No"
       for c in A:
            if c not in B:
               return "NO"
       else:
            return "YES"





print(anagrams_test('abcd','bcda'))