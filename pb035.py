import math
import time

t1 = time.time()

prime = [2,3]
b = 3

while True:

    if b > 1000000:
        break
    
    while True:
        b = b+2
        i = 0
        t = True
        while (prime[i]*prime[i] < b):
            i=i+1
            if (b%prime[i] == 0):
                t = False
                break
                
        if t:
            prime.append(b)
            break
      
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
