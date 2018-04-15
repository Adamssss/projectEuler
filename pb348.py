import math
import time

t1 = time.time()



def testrun(cap):
    result = []
    R = {}
    for a in range(2,math.ceil(math.sqrt(cap))):
        r = cap - a*a
        for b in range(2,math.ceil(r**(1./3.))):
            t = a*a+b*b*b
            if isPalindromic(t):
                if t in R:
                    R[t] += 1
                else:
                    R[t] = 1
    for i in R:
        if R[i] == 4:
            result.append(i)
    return result

def des(n):
    print('number:',n)
    count = 0
    for b in range(2,math.ceil((n-4)**(1./3.))):
        r = n-b*b*b
        a = math.ceil(math.sqrt(r))
        if r == a*a:
            print(a,b,a*a,'+',b*b*b,'=',a*a+b*b*b)
            count += 1
    print('count:',count)
    return count

def slientdes(n):
    count = 0
    for b in range(2,math.ceil((n-4)**(1./3.))):
        r = n-b*b*b
        a = math.ceil(math.sqrt(r))
        if r == a*a:
            count += 1
    return count

def isPalindromic(n):
    t = []
    while True:
        t.append(n%10)
        n = n//10
        if n == 0:
            break
    for i in range(len(t)//2):
        if not t[i] == t[-i-1]:
            return False
    return True

def answer():
    t = testrun(10**9)
    count = 0
    result = 0
    for i in sorted(t):
        w = slientdes(i)
        if w == 4:
            #des(i)
            count += 1
            result += i
        if count == 5:
            break
    return result


print(answer())


print("time:",time.time()-t1)  





