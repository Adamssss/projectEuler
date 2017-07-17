import time

t1 = time.time()


# 987654321 9-dig pandigital always has divisor 9
# 87654321 8-dig pandigtal also always has divisor 9

def QPL(m_list):
    if len(m_list) == 1:
        return [m_list]
    qpl = []
    for i in m_list:
        rest = m_list[:]
        rest.remove(i)
        for j in QPL(rest):
            qpl.append([i]+j)
    return qpl

prime = [2,3,5]
primen = 2

# square root of 7654321
while prime[primen] < 2767:
    b = prime[primen]
    t = 1
    while (t == 1):
        b = b+2
        i = 0
        t = 0
        while (prime[i]*prime[i] < b)and (t == 0):
            i=i+1
            if (b%prime[i] == 0):
                t = 1
               
        if (t == 0):
            primen += 1
            prime.append(b)


def isPrime(item):
    for i in range(0,len(prime)):
        if item%prime[i] == 0:
            return False
    return True


for i in QPL([7,6,5,4,3,2,1]):
    if i[-1]!=1 and i[-1]!=3 and i[-1]!=7:
        continue
    num = 0
    for j in range(0,len(i)):
        num = num*10 + i[j]
    if isPrime(num):
        print(num)
        break

print("time:",time.time()-t1)
