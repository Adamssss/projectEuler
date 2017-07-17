import math
import time

t1 = time.time()

N = 100000000

# 1+...+n^2
#= n*(n+1)*(2n+1)/6

def squarecon(a,n):
    #result = (a+n-1)*(a+n)*(2*a+2*n-1)//6
    #result -= (a-1)*a*(2*a-1)//6
    result = (n-1)*n*(2*n-1)//6
    result += a*n*(a+n-1)
    return result

def calc(N):
    a = 1
    n = 2
    t = []
    while True:
        temp = squarecon(a,n)
        #print(a,n,temp)
        if temp > N:
            if a == 1:
                break
            else:
                a = 1
                n += 1
                continue
        if panlidrome(temp):
            if not temp in t:
                t.append(temp)
        a += 1
    return t

def panlidrome(num):
    t = []
    while num > 0:
        t.append(num%10)
        num = num//10
    for i in range(len(t)//2):
        if t[i] != t[-i-1]:
            return False
    return True

print(sum(calc(N)))           

print("time:",time.time()-t1)  


    
