import math

prime = [2,3,5]
primen = 2
N = 1000000

while prime[primen] < N:
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

# the last dig must be 2,3,5,7
# the last can not be 3,7

# the first dig must be 2,3,5,7

# no mid dig can be 0/2/4/6/8 or 5


# define a binary search 
def isPrime(item):
    firstPoint = 0
    endPoint = len(prime)-1
    index = -1
    while firstPoint <= endPoint:
        midPoint = (firstPoint+endPoint)//2
        if prime[midPoint] == item:
            index = midPoint
            return index
        elif item > prime[midPoint]:
            firstPoint = midPoint +1
        else:
            endPoint = midPoint -1

    return index

tenTo = [1]
for i in range(1,10):
    tenTo.append(tenTo[-1]*10)
    

cp = []
i = 7
while prime[i] < N:
    i += 1
    if not (prime[i]%10 == 3 or prime[i]%10 == 7):
        continue
    else:
        dig = math.floor(math.log10(prime[i]))+1
        f = prime[i] // tenTo[dig-1]
        if not (f == 2 or f == 3 or f == 5 or f == 7):
            continue
        else:
            t = 1
            if dig > 2:
                for j in range(1,dig-1):
                    fh = prime[i]//tenTo[dig-1-j]
                    lh = prime[i]%tenTo[j+1]
                    if isPrime(fh) < 0 or isPrime(lh) < 0:
                        t = 0
            if t == 1:
                cp.append(prime[i])
    

total = 0
for i in range(0,len(cp)):
    total += cp[i]

print (total)
