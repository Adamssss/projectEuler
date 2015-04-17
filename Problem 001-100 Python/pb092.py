import math
import time

t1 = time.time()

N = 10000000

e = [0]*(N+1)

def nn(num):
    result = 0
    while num > 0:
        temp = num%10
        num = num//10
        result += temp*temp
    return result

def E(n):
    global e
    if n == 1 or n == 89:
        e[n] = n
    if e[n] > 0:
        return

    nnn = nn(n)        
    if e[nnn] == 0:
        E(nnn)
                
    if e[nnn] > 0:
        e[n] = e[nnn]
        return

for i in range(1,N+1):
    E(i)

count = 0

for i in e:
    if i == 89:
        count += 1

print(count)
  
print("time:",time.time()-t1)
    


    
