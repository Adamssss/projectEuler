import time

t1 = time.time()

def binary(x):
    b = []
    while x > 0:
        b.append(x%2)
        x = x//2
    length = len(b)//2
    if length == 0:
        return True
    for i in range(0,length):
        if b[i] != b[-1-i]:
            return False
    return True

def decimal(x):
    d = []
    while x > 0:
        d.append(x%10)
        x = x//10
    length = len(d)//2
    if length == 0:
        return True
    for i in range(0,length):
        if d[i] != d[-1-i]:
            return False
    return True

total = 0
for i in range(1,1000000):
    if binary(i) and decimal(i):
        total += i

print (total)

print("time:",time.time()-t1)
