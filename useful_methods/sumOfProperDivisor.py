import math

# prime generator required

# to find out the sum of the proper divisor
def spd(number):
    originNumber = number
    spd = 1
    i = 0
    count = 0
    nr = math.floor(math.sqrt(number))
    while prime[i] <= nr:
        while(number%prime[i] == 0):
            count=count+1
            number = number / prime[i]
        nr = math.floor(math.sqrt(number))
            
        if count > 0:
            spdtemp = (math.pow(prime[i],count+1)-1)//(prime[i]-1)      
            spd *= spdtemp
            count = 0
            
        i = i+1

    if number > 1:
        spd *= (number+1)

    return spd - originNumber


    
