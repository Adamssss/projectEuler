import math
import time

t1 = time.time()

N = 1000000

n = (N+1)//2

p = [True]*(n)

i = 1
prime = [2]

while i < n:
    if p[i]:
        t = 2*i+1
        prime.append(t)
        j = i
        while j < n:
            p[j] = False
            j += t
    i += 1
      
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

# define a binary search 
def isInList(item,lst):
    firstPoint = 0
    endPoint = len(lst)-1
    index = -1
    while firstPoint <= endPoint:
        midPoint = (firstPoint+endPoint)//2
        if lst[midPoint] == item:
            index = midPoint
            return index
        elif item > lst[midPoint]:
            firstPoint = midPoint +1
        else:
            endPoint = midPoint -1

    return index

target = prime[:]
count = 0
while len(target) > 0:
    #print(target)
    #print (count)
    test = target[0]
    dig = math.floor(math.log10(test))+1
    target.pop(0)
    if dig == 1:
        count += 1
        continue
    if dig > 1:
        i = 1
        counted = 0
        tl = True
        while i < dig:
            test = test//10 + (test%10)*math.pow(10,dig-1)
            if isPrime(test):
                i += 1
                ind = isInList(test,target)
                if ind >= 0:
                    target.pop(ind)
                else:
                    counted += 1
            else:
                tl = False
                break

        if tl:
            count += dig - counted
            
            
        


print (count)

print("time:",time.time()-t1)
