import math
import time

t1 = time.time()

def chg(m,n):   
    '''
    total = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            total += i*j
    return total
    '''
    return m*(m+1)*n*(n+1)//4

def cdg(m,n):
    '''
    total = 0
    tset = []
    for i in range(1,n):
        tset.append(2*i)
    for i in range(m-n):
        tset.append(2*n-1)
    for i in range(n-1,0,-1):
        tset.append(2*i)
    for i in range(1,m+n-1):
        for j in range(0,len(tset)-i+1):
            if m > n:
                k = min(min(tset[j:j+i]),max(tset[j:j+i])+1-i)
            else:
                k = min(tset[j:j+i])
            if k > 0:
                    total += k*(k+1)//2
    return total
    '''
    return n*((2*m-n)*(4*n*n-1)-3)//6

def dg(m,n):
    return chg(m,n)+cdg(m,n)

def dgm(m,n):
    total = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if i >= j:
                total += dg(i,j)
            else:
                total += dg(j,i)
    return total

print(dgm(47,43))
        
print("time:",time.time()-t1)  


    
