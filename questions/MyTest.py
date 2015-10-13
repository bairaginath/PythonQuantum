__author__ = 'veradocs-web'

def fun(n,shrape,strength):
    for i in n:
        if strength[i]>shrape[i]:
           return "NO"
    else:
        return "YES"

testcases=raw_input()
for testcase in range(int(testcases)):
    total_animal =int(raw_input())
    shrape=[x for x in str(raw_input()).split(' ')]
    shrape.sort()
    strength=[x for x in str(raw_input()).split(' ')]
    strength.sort()
    print(fun(total_animal,shrape,strength))


str='34 334 223 2323 23 '
str.strip()

