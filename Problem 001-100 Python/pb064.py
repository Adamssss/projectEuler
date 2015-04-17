import math
import time

t1 = time.time()

# use [num,a,b,c] to store a/b*(sqrt(num)-c)
def valueOf(com):
    result = (math.sqrt(com[0])-com[3])*com[1]/com[2]
    return math.floor(result*math.pow(10,6))

def gcd(x,y):
    if x < y:
        temp = x
        x = y
        y = temp
    while y > 0:
        temp = x%y
        x = y
        y = temp

    return x

def oneOver(com):
    na = com[2]
    nb = com[1]*(com[0]-com[3]*com[3])
    nc = -com[3]
    d = gcd(na,nb)
    return [com[0],na//d,nb//d,nc]

def head(com):
    return valueOf(com)//math.pow(10,6)

def trun(com,a):
    nc = com[3]+a*com[2]/com[1]
    return [com[0],com[1],com[2],nc]
    
def notation(num):
    root = math.sqrt(num)
    a = math.floor(root)
    if a == root:
        return [a,[]]
    rest = [num,1,1,a]
    mark = valueOf(rest)
    lst = []
    while True:
        temp = oneOver(rest)
        na = head(temp)
        lst.append(na)
        rest = trun(temp,na)
        if valueOf(rest) == mark:
            break
    return [a,lst]
        
def period(note):
    return len(note[1])

def isOdd(num):
    if num%2 == 1:
        return True
    return False

count = 0
for i in range(2,10001):
    if isOdd(period(notation(i))):
        count += 1

print(count)

print("time:",time.time()-t1)
