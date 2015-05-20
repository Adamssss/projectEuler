import math
import time

t1 = time.time()

def A(n):
    if n%2 == 0 or n%5 == 0:
        return 0
    count = 1
    r = 1
    while r != 0:
        while n > r:
            r = r*10+1
            count += 1
        r = r%n
    return count

# for i and k that gcd(i,k) == 1
# A(i*k) = lcm(A(i),A(k))
# for i^j
# A(i^j) = A(i)*i^(j-1)

# for prime p >= 7
# according to Fermat's lttle theorem
# a^(p-1)-1  = 0 mod p
# (10^(p-1)-1)/9 = R(p-1) A(p) <= p-1

# A(3) = 3
# for i > 3
# A(i) <= i

for i in range(1000003,1020000):
    if A(i) > 1000000:
        print(i)
        break

print("time:",time.time()-t1)


    
