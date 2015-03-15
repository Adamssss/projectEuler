import time

t1 = time.time()

fac = [1,1]
for i in range(2,10):
    fac.append(fac[-1]*i)

def digfac(num):
    result = 0
    while num > 0:
        result += fac[num%10]
        num = num//10
    return result

def loop(num):
    temp = [num]
    n = num
    while True:
        n = digfac(n)
        if n in temp:
            break
        else:
            temp.append(n)
    return temp

def chain(num):
    return len(loop(num))

count = 0
for i in range(1,1000000):
    if chain(i) == 60:
        count += 1

print(count)

print("time:",time.time()-t1)

