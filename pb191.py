import math
import time

t1 = time.time()

# Prize String counting
# psc(1) = 3
# psc(2) = 8 (no LL)
# psc(3):
# starting with O - psc(2)
# starting with L - psc(2) without L
# starting with A:
# following with AO - 1
# following with AL - without L
# following with L - psc(1) without L
# following with O psc(1)
# 8+4+1+1+2+3 = 19
# psc(4) = psc(3)+psc(3)wl+psc(1)+psc(1)wl+psc(2)wl+psc(2)
# 19+7+3+2+4+8 = 43

# pscwl(1) = 2
# pscwl(2) = 4
# pscwl(3):
# starting with O - pscwl(2)
# starting with A:
# following with AO 1
# following with O - pscwl(1)
# 4+1+2 = 7

N = 30

# use array to store the calculated values
psca = [0]*(N+1)
pscwla = [0]*(N+1)


psca[0] = 1
psca[1] = 3
psca[2] = 8
def psc(n):
    if psca[n] > 0:
        return psca[n]
    temp = psc(n-1)+pscwl(n-1)+psc(n-3)+pscwl(n-3)+psc(n-2)+pscwl(n-2)
    psca[n] = temp
    return temp

pscwla[0] = 1
pscwla[1] = 2
pscwla[2] = 4
def pscwl(n):
    if pscwla[n] > 0:
        return pscwla[n]
    temp = pscwl(n-1)+pscwl(n-2)+pscwl(n-3)
    pscwla[n] = temp
    return temp

print(psc(N))

print("time:",time.time()-t1)  


    
