import math
import time

t1 = time.time()

N = 500

prime = [2,3]
b = 3

while True:

    
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
        
    if b > N:
        break

def isPrime(item):
    root = math.floor(math.sqrt(item))
    i = 0
    t = prime[i]
    while t <= root:
        if item%t == 0:
            return False
        if t < prime[-1]:
            i += 1
            t = prime[i]
        else:
            t += 2
    return True

# i kinds of number make of j
# f(i,j) = f(i-1,j)+f(i,j-Pi)

def f(i,j):
    if j == 0:
        return 1
    if j < 1:
        return 0
    if i == 0:
        return 0
    return f(i-1,j)+f(i,j-prime[i-1])

def w(i):
    result = f(i//2+1,i)
    if isPrime(i):
        result -= 1
    return result

for i in range(50,N):
    if w(i) > 5000:
        print(i)
        break

print("time:",time.time()-t1)
