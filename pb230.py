import math
import time

t1 = time.time()

#A                  1   [[1][]]         
#B                  1   [[][1]]
#AB                 2   [[1][2]]
#BAB                3   [[2][1,3]]
#ABBAB              5   [[1,4][2,3,5]]
#BABABBAB           8   [[2,4,7][1,3,5,6,8]]
#ABBABBABABBAB      13  


fab = [1,1,2,3]

def addfab():
    global fab
    nfab = fab[-1]+fab[-2]
    fab.append(nfab)
    return nfab


def example():
    A = "1415926535"
    B = "8979323846"

    l = 10
    n = 35
    
    return D(A,B,n,l)
    

def isA(n,i):
    #print(n,i,fab[i])
    if i == 2:
        if n == 1:
            return True
        if n == 2:
            return False
    if i == 3:
        if n == 2:
            return True
        if n == 1 or n == 3:
            return False
    if n == 0:
        return False
    if n > fab[i-2]:
        return isA(n-fab[i-2],i-1)
    else:
        return isA(n,i-2)
    

def D(A,B,n,l):
    isan = math.ceil(n/l)
    if fab[-1] < isan:
        nfab = addfab()
        while nfab < isan:
            nfab = addfab()
        isai = len(fab)-1
    else:
        isai = 0
        while fab[isai] < isan:
            isai += 1
    S = B
    # fab[i-1]< n <= fab[i]
    if isA(isan,isai):
        S = A
    d = n - isan*l+l
    return ord(S[d-1])-48


def answer():
    A = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    B = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"

    l = 100

    result = 0
    for i in range(0,18):
        n = (127+19*i)*(7**i)
        result += (10**i)*D(A,B,n,l)
    return result

#print(example())
print(answer())

print("time:",time.time()-t1)  





