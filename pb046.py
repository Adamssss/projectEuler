import math

prime = [2,3,5]
primen = 2
oddcom = []

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
        if t == 1:
            oddcom.append(b)

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


for i in oddcom:
    n = math.floor(math.sqrt(i//2))
    t = 0
    for j in range(1,n+1):
        if isInList((i-2*j*j),prime) > 0:
            t = 1
    if t == 0:
        print (i)
        break
