__author__ = 'veradocs-web'

Matrix=[[0,0,1,0, 1],
[0,0,0,0,0],
[0,1,1,1,1],
[0,1,1,0,0]
]

def move_condition(M,x,y):
    numrows = len(M)
    numcols = len(M)
    if x-1<0 or x+1 >= numrows:
        return False


def move_left(M,x,y):
    numrows = len(M)
    numcols = len(M)
    if x-1<0 :
        return False
    if M[x-1][y]==1:
        return False
    return True


def move_right(M,x,y):
    numrows = len(M)
    numcols = len(M)
    if  x+1 >= numrows:
        return False
    if M[x+1][y]==1:
        return False
    return True


def move_up(M,x,y):
    numrows = len(M)
    numcols = len(M)
    if  y-1 >= numcols:
        return False
    if M[x][y-1]==1:
        return False
    return True

def move_down(M,x,y):
    numrows = len(M)
    numcols = len(M)
    if  y+1 >= numcols:
        return False
    if M[x][y+1]==1:
        return False
    return True



def check_path_exist(M,A,B):
    x1,y1=A
    x2,y2=B
    if M[x1][y1]==1 or M[x2][y2]==1:
        return False

















if __name__ == '__main__':
    print check_path_exist(Matrix,(3,0),(0,3))

