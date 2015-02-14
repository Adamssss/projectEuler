
# code copied from pb 12

# prime number generator copied from pb 7


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


totalspd = 0
for i in range(2,10000):
    if spd(spd(i)) == i:
        if not spd(i)-i == 0:
            # print (i,spd(i))
            totalspd += i

print (totalspd)



    
    
    
        

            
