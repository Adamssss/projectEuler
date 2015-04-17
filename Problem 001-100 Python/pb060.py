import math
import time

t1 = time.time()

N = 30000
n = 5

prime = [2,3,5]
primen = 2

while prime[primen] < 10000:
    b = prime[primen]
    t = 1
    while (t == 1):
        b = b+2
        i = 0
        t = 0
        while (prime[i]*prime[i] < b)and (t == 0):
            i=i+1
            if (b%prime[i] == 0):
                t = 1
               
        if (t == 0):
            primen += 1
            prime.append(b)

# possible set
ps = []

# expnad the ps
def moveTo(num):
    for i in range(0,len(ps)):
        temp = app(ps[i],num)
        if test(temp):
            if show(temp):
                return True
            ps.append(temp)

    if num <15 and isPrime(num):
        ps.append([num])
    return False

# append the set to the sum
def app(theset,x):
    total = sum(theset)
    temp = theset[:]
    temp.append(x - total)
    return temp

# test the set meets the pair prime rule
def test(testset):
    if testset[-1] < testset[-2]:
        return False
    if not isPrime(testset[-1]):
        return False
    total = sum(testset) + (n-len(testset))*testset[-1]
    if total > N:
        return False
    for i in range(0,len(testset)-1):
        a = seq(testset[i],testset[-1])
        if not isPrime(a):
            return False
        b = seq(testset[-1],testset[i])
        if not isPrime(b):
            return False
    return True

# make two number concatenate
def seq(a,b):
    dig = math.floor(math.log10(b)+1)
    return a*math.pow(10,dig)+b

def isPrime(item):
    root = math.floor(math.sqrt(item))
    i = 0
    t = prime[i]
    while t <= root:
        if item%t == 0:
            return False
        if t < prime[-1]:
            i += 1
            t = prime[i]
        else:
            t += 2
    return True


# show the list
def show(theset):
    if len(theset) == n:
        print (sum(theset))
        return True
    return False

for i in range(3,N):
    if moveTo(i):
        break

print("time:",time.time()-t1)
