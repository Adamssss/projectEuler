import math

# prime generator required

# the distinct factors count
def factors(number):
    factx = 1
    i = 0
    count = 0
    nr = math.floor(math.sqrt(number))
    while prime[i] <= nr:
        while(number%prime[i] == 0):
            count=count+1
            number = number / prime[i]
        nr = math.floor(math.sqrt(number))
            
        if count > 0:
            factx += 1
            count = 0
            
        i = i+1
    if number == 1:
        factx -= 1
    return factx


