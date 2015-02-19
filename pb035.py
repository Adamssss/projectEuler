import math

prime = [2,3,5]
primen = 2

while prime[primen] < 1000000:
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

length = len(prime)
#print (length)

# define a binary search 
def isPrime(item,lst):
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
    if dig == 1:
        count += 1
        target.remove(test)
    if dig > 1:
        number = []
        stillPossible = 1
        target.remove(test)
        temp = test
        for i in range(0,dig):
            number.append(temp%10)
            temp = temp//10
            if number[i]%2 == 0:
                stillPossible = 0
        i = 1
        counted = 0
        while stillPossible == 1 and i < dig:
            test = test//10 + (test%10)*math.pow(10,dig-1)
            if isPrime(test,prime) >= 0:
                i += 1
                if isPrime(test,target) >= 0:
                    target.remove(test)
                else:
                    counted += 1
            else:
                stillPossible = 0

        if stillPossible == 1:
            count += dig - counted
            
            
        


print (count)
