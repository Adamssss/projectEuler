import math
import time

t1 = time.time()

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

# all number treated in 4 digits array

# define a method to check if it is a prime
def isPrime(test):
    num = valueOf(test)
    if num%2 == 0:
        return False
    i = 3
    while i < math.sqrt(num):
        if num%i == 0:
            return False
        i += 2
    return True

meets = []

# value of
def valueOf(test):
    num = 0
    for i in range(0,4):
        num = num*10+test[i]
    return num
    
# sequences
def isSeq(test):
    global meets
    l = len(test)
    for i in range(0,l-2):
        a = valueOf(test[i])
        for j in range(i+1,l-1):
            b = valueOf(test[j])
            c = b*2-a
            if a!=b:
                temp = [0,0,0,0]
                for k in range(0,4):
                    temp[3-k] = c%10
                    c = c//10
                if temp in test:
                    seq = [a,b,b*2-a]
                    if not seq in meets:
                        meets.append(seq)
    


for a in range(1,10):
    for b in range(a,10):
        for c in range(b,10):
            for d in range(c,10):
                temp = QPL([a,b,c,d])[:]
                rest = []
                for i in temp:
                    if isPrime(i):
                        rest.append(i)

                if len(rest) >= 3:
                    isSeq(rest)

answer = 0
for i in range(0,3):
    answer = answer*10000 + meets[2][i]

print(answer)
                
print("time:",time.time()-t1)        
