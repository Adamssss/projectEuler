import math
import time

t1 = time.time()


#   --      0
#  |  |    1  2
#   --      3
#  |  |    4  5
#   --      6

clockd = []

# 0
clockd.append([True,True,True,False,True,True,True])
# 1
clockd.append([False,False,True,False,False,True,False])
# 2
clockd.append([True,False,True,True,True,False,True])
# 3
clockd.append([True,False,True,True,False,True,True])
# 4
clockd.append([False,True,True,True,False,True,False])
# 5
clockd.append([True,True,False,True,False,True,True])
# 6
clockd.append([True,True,False,True,True,True,True])
# 7
clockd.append([True,True,True,False,False,True,False])
# 8
clockd.append([True,True,True,True,True,True,True])
# 9
clockd.append([True,True,True,True,False,True,True])

def displayd(n):
    dd = clockd[n]
    print("")
    if dd[0]:
        print(" -- ")
    else:
        print("")
    s = ""
    if dd[1]:
        s += "|"
    else:
        s += " "
    if dd[2]:
        s += "  |"
    print(s)
    if dd[3]:
        print(" -- ")
    else:
        print("")
    s = ""
    if dd[4]:
        s += "|"
    else:
        s += " "
    if dd[5]:
        s += "  |"
    print(s)
    if dd[6]:
        print(" -- ")
    else:
        print("")
    print("")

# from right to left
def tolist(n):
    l = []
    while n > 0:
        l.append(n%10)
        n = n // 10
    return l

def dr(l):
    return sum(l)

def Sam(n):
    r = 0
    while n > 9:
        l = tolist(n)
        r += samt(l)*2
        n = dr(l)
    r += samt([n])*2
    return r

samtl = [0]*(10)
for i in range(10):
    r = 0
    for j in clockd[i]:
        if j:
            r += 1
    samtl[i] = r

def samt(l):
    r = 0
    for i in l:
        r += samtl[i]
    return r

def Max(n):
    r = 0
    ol = tolist(n)
    r += samt(ol)
    n = dr(ol)
    while n > 9:
        nl = tolist(n)
        r += maxt(ol,nl)
        n = dr(nl)
        ol = nl[:]
    r += maxt(ol,[n])
    r += samt([n])
    return r

# from old list to new list
def maxt(ol,nl):
    r = 0
    lol = len(ol)
    lnl = len(nl)
    for i in range(lnl):
        r += maxtrans(ol[i],nl[i])
    for j in range(lnl,lol):
        r += samtl[ol[j]]
    return r

maxtransl = [-1]*100

def maxtrans(od,nd):
    li = od*10+nd
    if maxtransl[li] >= 0:
        return maxtransl[li]
    r = 0
    for i in range(7):
        if clockd[od][i] != clockd[nd][i]:
            r += 1
    maxtransl[li] = r
    nli = nd*10+od
    maxtransl[nli] = r
    return r

N = 10**7

prime = []

def primeSieve(n):
    global prime
    n = (n+1)//2
    p = [True]*(n)
    i = 1
    prime.append(2)
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

primeSieve(2*N+100)

# Can improve more by specify Sam(n)-Max(n) to a SminM(n)
# Can store digit root answers for re-visiting
def answer():
    result = 0
    i = 0
    while prime[i] < N:
        i += 1
    while True:
        if prime[i] > 2*N:
            break
        result += Sam(prime[i])-Max(prime[i])
        i += 1
    return result

#print(Sam(137))
#print(Max(137))
print(answer())

print("time:",time.time()-t1)  





