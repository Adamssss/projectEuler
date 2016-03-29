import math
import time

t1 = time.time()

N = 50000000

prime = []

# dont need 2 this time
def primeSieve(n):
    global prime
    n = (n+1)//2
    p = [True]*(n)
    i = 1
    #prime.append(2)
    while i < n:
        if p[i]:
            t = 2*i+1
            prime.append(t)
            p[i] = False
            j = 2*i*i+2*i
            while j < n:
                p[j] = False
                j += t
        i += 1
    return prime

primeSieve(math.floor(N*1.42))
#print("time:",time.time()-t1) 
#t1 = time.time()

def factors(number,ic):
    r = []
    i = ic
    count = 0
    nr = math.floor(math.sqrt(number))
    while prime[i] <= nr:
        while(number%prime[i] == 0):
            count=count+1
            number = number / prime[i]
        
        if count > 0:
            r.append(prime[i])
            count = 0
            nr = math.floor(math.sqrt(number))
            
        i = i+1
    if number > 1 and len(r) > 0:
        r.append(int(number))
    return r

# 2t^2-1 = kp
# 2t^2 = kp+p+1
# t^2 = kp+(p+1)/2
# (ap+b)^2 = kp+(p+1)/2
# a^2p^2+2*a*b*p+b^2 = kp+(p+1)/2

def ttSieve(n):
    ip = [True]*(n+1)
    ip[0] = False
    ip[1] = False
    c = 0
    i = 2
    while i <= n:
        if ip[i]:
            t = 2*i*i-1
            ft = factors(t,0)
            if len(ft) == 0:
                #print(i)
                i +=1
                c += 1
                continue
            ip[i] = False
            #print(i,ft)
            for k in ft:
                j = i+k
                while j <= n:
                    ip[j] = False
                    j += k
                    '''
                if k > i:
                    j = 2*k-i
                    while j <= n:
                        ip[j] = False
                        j += k
                        '''
        i += 1
    return c

# sieve from the primes
def ttSieveav(n):
    ip = [True]*(n+1)
    ip[0] = False
    ip[1] = False
    c = 0
    for p in prime:
        ta = (p+1)//2
        if not ec(ta,p):
            continue
        for j in range(1,p//2+1):
            if (j*j)%p == ta:
                k = j
                if 2*k*k-1 == p:
                    k = j+p
                while k <= n:
                    ip[k] = False
                    k += p
                k = p-j
                while k <= n:
                    ip[k] = False
                    k += p
                break
    for i in ip:
        if i:
            c += 1
    return c

# Euler's criterion
# (ta**(ta-1))%p == 1
def ec(ta,p):
    return mp(ta,(p-1)//2,p) == 1

# x of power y mode p
def mp(x,y,p):
    if y == 0:
        return 1
    if y == 1:
        return x%p
    ny = y//2
    nx = (x*x)%p
    if y == ny*2:
        return mp(nx,ny,p)
    return (mp(nx,ny,p)*x)%p

# Tonelli–Shanks algorithm
def tsa(ta,p):
    Q = p-1
    S = 0
    while Q%2 == 0:
        Q = Q//2
        S += 1
    if S == 1:
        return mp(ta,(p+1)//4,p)
    z = 2
    while True:
        if not ec(z,p):
            break
        z += 1
    #print(z)
    c = mp(z,Q,p)
    R = mp(ta,(Q+1)//2,p)
    t = mp(ta,Q,p)
    M = S
    while True:
        #print(c,R,t,M)
        if t == 1:
            #print(ta,p,R,(R*R)%p-ta)
            return R
        i = 1
        tt = (t*t)%p
        while True:
            if tt == 1:
                break
            i += 1
            tt = (tt*tt)%p
            if i == M:
                print('Error')
        b = mp(c,2**(M-i-1),p)
        #print(i,b)
        R = (R*b)%p
        t = (t*b*b)%p
        c = (b*b)%p
        M = i

def ttSieveavtsa(n):
    ip = [True]*(n+1)
    ip[0] = False
    ip[1] = False
    c = 0
    for p in prime:
        ta = (p+1)//2
        if not ec(ta,p):
            continue
        j = tsa(ta,p)
        if j >= p//2:
            j = p-j
        k = j
        if 2*k*k-1 == p:
            k = j+p
        while k <= n:
            ip[k] = False
            k += p
        k = p-j
        while k <= n:
            ip[k] = False
            k += p
    for i in ip:
        if i:
            c += 1
    return c

print(ttSieveavtsa(N))

print("time:",time.time()-t1)

'''
print(N,ttSieveavtsa(N))
print("time:",time.time()-t1)

t1 = time.time()
print(N,ttSieveav(N))
print("time:",time.time()-t1)

t1 = time.time()
# correct answer
print(N,ttSieve(N))


print("time:",time.time()-t1)  
'''

    
