import time

t1 = time.time()

# all the combination of 2&3 to form a row of n
def row(n):
    if n < 2:
        return []
    if n < 3:
        return [[2]]
    if n == 3:
        return [[3]]
    r = []
    for i in row(n-2):
        r.append(i+[2])
    for i in row(n-3):
        r.append(i+[3])
    return r

# cracks of a row apart from the first and the last
def crack(r):
    if len(r) <= 1:
        return []
    result = []
    t = 0
    for i in range(len(r)-1):
        t = t + r[i]
        result.append(t)
    return result

# run crack on the set of row combinations
def cracks(row):
    c = []
    for i in row:
        c.append(crack(i))
    return c

# compare two sorted cracks sets to find if there is a running crack
def running(a,b):
    la = len(a)
    lb = len(b)
    i = 0
    j = 0
    while i < la and j < lb:
        if a[i] == b[j]:
            return True
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
    return False

def nextrow(row):
    l = len(row)
    c = cracks(row)
    r = []
    for j in range(l):
        t = []
        for i in range(l):
           if not running(c[i],c[j]):
               t.append(i)
        r.append(t)
    return r

# the function w
def w(a,b):
    p = row(a)
    c = cracks(p)
    l = len(p)
    r = []
    for i in p:
        r.append([i])
    rc = []
    for i in c:
        rc.append([i])
    b = b-1
    while b > 0:
        nr = []
        nrc = []
        for j in range(len(r)):
            for i in range(l):
                if not running(c[i],rc[j][-1]):
                    nr.append(r[j]+[p[i]])
                    nrc.append(rc[j]+[c[i]])
        b = b-1
        r = nr
        rc = nrc
    #print(r)
    return len(r)

# improved function w
def nw(a,b):
    p = row(a)
    np = nextrow(p)
    r = []
    for i in range(len(p)):
        r.append([i])
    b = b-1
    while b > 0:
        nr = []
        for j in r:
            for i in np[j[-1]]:
                nr.append(j+[i])
        r = nr
        b = b-1
    print(r)
    return len(r)


def sw(a,b):
    p = row(a)
    np = nextrow(p)
    l = len(p)
    mi = [0]*l
    for i in range(l):
        if len(np[i])>0:
            mi[i] = 1
    b = b-1
    while b > 0:
        nmi = [0]*l
        for i in range(l):
            for j in np[i]:
                nmi[j] += mi[i]
        mi = nmi
        b = b-1
    return sum(mi)

'''
print(5,2,w(5,2))
print(9,3,w(9,3))
print("time:",time.time()-t1)
#print(w(32,10))
'''
#print(row(9),nextrow(row(9)))
#print(nw(5,2),nw(9,3))
#print(sw(5,2),sw(9,3))
#print(sw(11,6),nw(11,6),w(11,6))

print(sw(32,10))

print("time:",time.time()-t1)



