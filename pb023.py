
# code copied from pb 21

# prime number generator

a = [2,3,5]
n = 2

while n < 10000:
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
            spdtemp = 1
            while count > 0:
                spdtemp = spdtemp *a[i] +1
                count -= 1
            
                
            spd *= spdtemp
            count = 0
            
        i = i+1

    return spd - originNumber

N = 28124
# find the abudant numbers
abundant = []
for i in range(1,N):
    if spd(i)>i:
        abundant.append(i)


length = len(abundant)
total = 0
for i in range(1,N):
    j = 0
    isPossible = 0
    while isPossible == 0 and j < length:
        if (i-abundant[j]) in abundant:
           isPossible = 1           
        j = j+1

    if isPossible == 0:
        total += i

print (total)
        
    
    

    
    
    
        

            
