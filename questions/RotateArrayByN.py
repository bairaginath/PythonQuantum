__author__ = 'veradocs-web'


def reverse(A,start,end):
    if start==end:
        return A
    temp=A[start]
    A[start]=A[end]
    A[end]=temp
    return reverse(A,start+1,end-1)

def rotate_array_by_n(A,n):
    index=A.index(n)
    reverse(A,0,index-1)
    reverse(A,index+1,len(A)-1)
    reverse(A,0,len(A)-1)
    pass



if __name__ == '__main__':
    A=[0,1,2,4,5,6,7]
    rotate_array_by_n(A,4)
    print A



