import math


N = 100

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
            factx *= (count+1)
            count = 0
            
        i = i+1
    if number > 1:
        factx *= 2
    return factx


print(factors(4))
