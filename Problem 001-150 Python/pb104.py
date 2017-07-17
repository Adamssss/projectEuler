import math
import time

t1 = time.time()

phi = (1+math.sqrt(5))/2
ovp = (1-math.sqrt(5))/2
# f(n) = (phi^n-ovp^n)/sqrt(5)
# one over phi is small when n is big
# f(n) = int(phi^n)/sqrt(5)
# log10(fn) = log10(phi)*n-log10(sqrt(5))
# first numbers = 10^(fractionpart(log10(fn))+8)
lp = math.log10(phi)
lsf = math.log10(math.sqrt(5))

def ff(n):
    temp = lp*n-lsf
    return round(math.pow(10,temp-math.floor(temp)+8))

def pandig(n):
    if n < 123456789:
        return False
    temp = []
    while n > 0:
        j = n%10
        n = n//10
        if j == 0: return False
        if j in temp:
            return False
        temp.append(j)
    return True

fn1 = 1
fn2 = 1
n = 2

ninth = math.pow(10,9)

while True:
    n += 1
    fn = fn1+fn2
    fn = fn%ninth
    fn1 = fn2
    fn2 = fn
    if pandig(fn):
        if pandig(ff(n)):
            print(n)
            break
    
print("time:",time.time()-t1)  


    
