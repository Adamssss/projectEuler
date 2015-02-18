
# code copied from pb 21

# prime number generator

a = [2,3,5]
n = 2

N = 28124

while a[n] < N:
    b = a[n]
    t = 1
    while (t == 1):
        b = b+2
        i = 0
        t = 0
        while (a[i]*a[i] < b)and (t == 0):
            i=i+1
            if (b%a[i] == 0):
                t = 1

                
        if (t == 0):
            n = n+1
            a.append(b)
            
#power: x to the y power
def power(x,y):
    product = 1
    for i in range(0,y):
        product *= x
    return product


# to find out the sum of the proper divsor
def spd(number):
    originNumber = number
    spd = 1
    i = 0
    count = 0
    while number > 1:
        while(number%a[i] == 0):
            count=count+1
            number = number / a[i]
            
        if count > 0:
            spdtemp = power(a[i],count+1)-1
            spdtemp = spdtemp // (a[i] - 1)
            spd *= spdtemp
            count = 0
            
        i = i+1

    return spd - originNumber


# find the abudant numbers
abundant = []
for i in range(1,N):
    if spd(i)>i:
        abundant.append(i)

#print (len(abundant))

# 28124/2 = 14062
#print (abundant[3489],abundant[3490])

# define a binary search for the list abundant
def inAbundant(item):
    firstPoint = 0
    endPoint = len(abundant)-1
    index = -1
    while firstPoint <= endPoint:
        midPoint = (firstPoint+endPoint)//2
        if abundant[midPoint] == item:
            index = midPoint
            return index
        elif item > abundant[midPoint]:
            firstPoint = midPoint +1
        else:
            endPoint = midPoint -1

    return index



total = N*(N-1)//2
for i in range(1,N):
    isPossible = 0
    j = 0
    while isPossible == 0 and j < 3490:
        if (i- abundant[j]) >= 0 and inAbundant(i- abundant[j]) >= 0:
            isPossible = 1
            total -= i
        j += 1


print (total)          
    
    

    
    
    
        

            
