import math
import time

t1 = time.time()

def digseq(num):
    if num == 0:
        return 2
    if num%3 == 1 or num%3 == 0:
        return 1
    return (num//3+1)*2

def convergents(n):
    if n == 1:
        return [2,1]
    i = n-1
    temp = [1,digseq(i)]
    while True:
        i -= 1
        t = digseq(i)
        ntemp = [t*temp[1]+temp[0],temp[1]]
        flip = [ntemp[1],ntemp[0]]
        if t == 0:
            return flip
        temp = flip[:]

tc = convergents(100)
num = tc[0]

total = 0
while num > 0:
    total += num%10
    num = num //10

print(total)

print("time:",time.time()-t1)
