import math
import time

t1 = time.time()

prime = [2,3]
b = 3

while True:

    if b > 1000:
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

# wikipedia phi function

ps = [0,1]

# phi(m*n) = phi(m)*phi(n) if gcd(m,n) == 1
# prime phi(p) = p-1
def phi(number):
    root = math.floor(math.sqrt(number))
    result = 1
    i = 0
    t = prime[i]
    while t <= root:
        count = 0
        while number%t == 0:
            count += 1
            number = number//t
        if count > 1:
            result *= int(math.pow(t,count-1))
        if count > 0:
            result *= ps[t]
            return result*ps[number]
        i += 1
        t = prime[i]
    return (number-1)

N = 1000000

# let ele(x) be the function that returns the number of elements in the set
# ele(x)-els(x-1) would be the phi(x)

# in other words: ele(x) = sum(ps)-1

for i in range(2,N+1):
    ps.append(phi(i))

print(sum(ps)-1)

print("time:",time.time()-t1)
                
