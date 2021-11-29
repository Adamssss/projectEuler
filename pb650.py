import math
import time

def init():
    global init_time
    init_time = time.time()

def timespent():
    print("time:",time.time()-init_time)

modN = 1000000007

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n*fact(n-1)

def Cv1(n,k):
    return fact(n)//fact(k)//fact(n-k)

def Bv1(n):
    r = 1
    for i in range(n+1):
        r *= Cv1(n,i)
    return r

def Dv1(n):
    B = Bv1(n)
    fc = []
    for i in range(2,n+1):
        if B%i ==0:
            c = 0
            while B%i == 0:
                B = B//i
                c += 1
            fc.append([i,c])
    r = 1
    for f in fc:
        r *= (f[0]**(f[1]+1)-1)//(f[0]-1)
    return r

def Sv1(n):
    r = 0
    for i in range(1,n+1):
        r += Dv1(i)
    return r

def test1():
    print(Sv1(5)) # 5736
    print(Sv1(10)) # 141740594713218418
    print(Sv1(100)%modN) # 332792866

Primes = []
def PrimeSieve(n):
    n = (n+1)//2
    p = [True]*(n)
    i = 1
    Primes.append(2)
    while i < n:
        if p[i]:
            t = 2*i+1
            Primes.append(t)
            p[i] = False
            j = 2*i*i+2*i
            while j < n:
                p[j] = False
                j += t
        i += 1
    return Primes



# 100 332792866 time: 0.44032955169677734
# 200 271664942 time: 6.808147668838501
def test2():
    N = 200
    print(Sv1(N)%modN)

def fctimes(ofc,nfc):
    fc = []
    i = 0
    j = 0
    ol = len(ofc)
    nl = len(nfc)
    while True:
        if i<ol and j <nl:
            if ofc[i][0]<nfc[j][0]:
                fc.append(ofc[i][:])
                i += 1
            elif ofc[i][0]>nfc[j][0]:
                fc.append(nfc[j][:])
                j += 1
            elif ofc[i][0]== nfc[j][0]:
                fc.append([ofc[i][0],ofc[i][1]+nfc[j][1]])
                j += 1
                i += 1
        elif i < ol:
            fc.append(ofc[i][:])
            i += 1
        elif j < nl:
            fc.append(nfc[j][:])
            j += 1
        else:
            break
    return fc
    
def fctimes2(ofc,nfc):
    fc = []
    i = 0
    j = 0
    ol = len(ofc)
    nl = len(nfc)
    while True:
        if i<ol and j <nl:
            if ofc[i][0]<nfc[j][0]:
                fc.append(ofc[i][:])
                i += 1
            elif ofc[i][0]>nfc[j][0]:
                fc.append([nfc[j][0],nfc[j][1]*2])
                j += 1
            elif ofc[i][0]== nfc[j][0]:
                fc.append([ofc[i][0],ofc[i][1]+nfc[j][1]*2])
                j += 1
                i += 1
        elif i < ol:
            fc.append(ofc[i][:])
            i += 1
        elif j < nl:
            fc.append([nfc[j][0],nfc[j][1]*2])
            j += 1
        else:
            break
    return fc

def factorof(n):
    fc = []
    nr = math.floor(math.sqrt(n))
    i = 0
    while Primes[i] <= nr:
        c = 0
        while n%Primes[i] == 0:
            n = n//Primes[i]
            c += 1
        nr = math.floor(math.sqrt(n))
        if c >0:
            fc.append([Primes[i],c])
        i += 1
    if n >1:
        fc.append([n,1])
    return fc

def factorofC(n,k):
    return factorof(Cv1(n,k))

def fcBv1(n):
    fc = []
    for i in range(1,(n+1)//2):
        tfc = factorofC(n,i)
        fc = fctimes2(fc,tfc)
    if n%2 == 0:
        tfc = factorofC(n,n//2)
        fc = fctimes(fc,tfc)
    return fc

def Dv2(n):
    fc = fcBv1(n)
    r = 1
    for f in fc:
        r *= ((f[0]**(f[1]+1)-1)//(f[0]-1))%modN
    return r%modN

def Sv2(n):
    r = 0
    for i in range(1,n+1):
        r += Dv2(i)
    return r%modN

# 100 332792866 time: 0.24620509147644043
# 200 271664942 time: 1.6346492767333984
def test3():
    N = 200
    PrimeSieve(N)
    print(Sv2(N))

def Cv2(n,k):
    r = 1
    for i in range(k+1,n+1):
        r *= i
    for i in range(2,n-k+1):
        r = r//i
    return r

def fcBv2(n):
    fc = []
    for i in range(1,(n+1)//2):
        tfc = factorof(Cv2(n,i))
        fc = fctimes2(fc,tfc)
    if n%2 == 0:
        tfc = factorof(Cv2(n,n//2))
        fc = fctimes(fc,tfc)
    return fc


def Dv3(n):
    fc = fcBv2(n)
    print(n,fc)
    r = 1
    for f in fc:
        r *= ((f[0]**(f[1]+1)-1)//(f[0]-1))%modN
    return r%modN


def Sv3(n):
    r = 0
    for i in range(1,n+1):
        r += Dv3(i)
    return r%modN


# 100 332792866 time: 0.11468005180358887
# 200 271664942 time: 0.9175703525543213
# 500 899393748 time: 20.55744767189026
def test4():
    N = 50
    PrimeSieve(N)
    print(Sv3(N))

fcarray = [[[0,0]],[[1,1]],[[2,1]],[[3,1]],[[2,2]],[[5,1]]]
def fcN(n):
    for i in range(6,n+1):
        fcarray.append(factorof(i))
    return fcarray

def fcdivide(ofc,dfc):
    #print("fd",ofc)
    fc = []
    i = 0
    ol = len(ofc)
    for j in range(len(dfc)):
        while i<ol-1 and ofc[i][0]<dfc[j][0]:
            fc.append(ofc[i][:])
            i += 1
        if ofc[i][0]==dfc[j][0]:
            ofc[i][1] -= dfc[j][1]
            if ofc[i][1] > 0:
                fc.append(ofc[i][:])
            i += 1
    i -= 1
    for j in range(i+1,ol):
        fc.append(ofc[j])
    #print("divide",dfc,"=",fc)
    return fc


def factorofCv2(n,k):
    fc = []
    for i in range(k+1,n+1):
        fc = fctimes(fc,fcarray[i])
    for i in range(2,n-k+1):
        fc = fcdivide(fc,fcarray[i])
    return fc

def fcBv3(n):
    fc = fctimes2([],fcarray[n])
    for i in range(2,(n+1)//2):
        tfc = factorofCv2(n,i)
        fc = fctimes2(fc,tfc)
    if n%2 == 0:
        tfc = factorofCv2(n,n//2)
        fc = fctimes(fc,tfc)
    return fc


def Dv4(n):
    fc = fcBv3(n)
    #print(n,fc)
    r = 1
    for f in fc:
        r *= ((f[0]**(f[1]+1)-1)//(f[0]-1))%modN
    return r%modN


def Sv4(n):
    r = 1+3
    for i in range(3,n+1):
        r += Dv4(i)
    return r%modN


# 100 332792866 time: 1.6288161277770996
# 200 271664942 time: 20.458344221115112
def test5():
    N = 200
    PrimeSieve(N)
    fcN(N)
    print(Sv4(N))


'''
1 []
2 [[2, 1]]
3 [[3, 2]]
4 [[2, 5], [3, 1]]
5 [[2, 2], [5, 4]]
6 [[2, 4], [3, 4], [5, 3]]
7 [[3, 2], [5, 2], [7, 6]]
8 [[2, 17], [5, 1], [7, 5]]
9 [[2, 10], [3, 14], [7, 4]]
10 [[2, 12], [3, 10], [5, 8], [7, 3]]
11 [[2, 4], [3, 6], [5, 6], [7, 2], [11, 10]]
12 [[2, 18], [3, 13], [5, 4], [7, 1], [11, 9]]
13 [[2, 8], [3, 8], [5, 2], [11, 8], [13, 12]]
14 [[2, 11], [3, 3], [7, 12], [11, 7], [13, 11]]
15 [[3, 12], [5, 12], [7, 10], [11, 6], [13, 10]]
16 [[2, 49], [3, 6], [5, 9], [7, 8], [11, 5], [13, 9]]
17 [[2, 34], [5, 6], [7, 6], [11, 4], [13, 8], [17, 16]]
18 [[2, 36], [3, 28], [5, 3], [7, 4], [11, 3], [13, 7], [17, 15]]
19 [[2, 20], [3, 20], [7, 2], [11, 2], [13, 6], [17, 14], [19, 18]]
20 [[2, 42], [3, 12], [5, 16], [11, 1], [13, 5], [17, 13], [19, 17]]
21 [[2, 24], [3, 24], [5, 12], [7, 18], [13, 4], [17, 12], [19, 16]]
22 [[2, 27], [3, 15], [5, 8], [7, 15], [11, 20], [13, 3], [17, 11], [19, 15]]
23 [[2, 8], [3, 6], [5, 4], [7, 12], [11, 18], [13, 2], [17, 10], [19, 14], [23, 22]]
24 [[2, 58], [3, 20], [7, 9], [11, 16], [13, 1], [17, 9], [19, 13], [23, 21]]
25 [[2, 36], [3, 10], [5, 44], [7, 6], [11, 14], [17, 8], [19, 12], [23, 20]]
26 [[2, 39], [5, 38], [7, 3], [11, 12], [13, 24], [17, 7], [19, 11], [23, 19]]
27 [[2, 16], [3, 68], [5, 32], [11, 10], [13, 22], [17, 6], [19, 10], [23, 18]]
28 [[2, 47], [3, 55], [5, 26], [7, 24], [11, 8], [13, 20], [17, 5], [19, 9], [23, 17]]
29 [[2, 22], [3, 42], [5, 20], [7, 20], [11, 6], [13, 18], [17, 4], [19, 8], [23, 16], [29, 28]]
30 [[2, 26], [3, 58], [5, 43], [7, 16], [11, 4], [13, 16], [17, 3], [19, 7], [23, 15], [29, 27]]
31 [[3, 44], [5, 36], [7, 12], [11, 2], [13, 14], [17, 2], [19, 6], [23, 14], [29, 26], [31, 30]]
32 [[2, 129], [3, 30], [5, 29], [7, 8], [13, 12], [17, 1], [19, 5], [23, 13], [29, 25], [31, 29]]
33 [[2, 98], [3, 48], [5, 22], [7, 4], [11, 30], [13, 10], [19, 4], [23, 12], [29, 24], [31, 28]]
34 [[2, 100], [3, 33], [5, 15], [11, 27], [13, 8], [17, 32], [19, 3], [23, 11], [29, 23], [31, 27]]
35 [[2, 68], [3, 18], [5, 42], [7, 30], [11, 24], [13, 6], [17, 30], [19, 2], [23, 10], [29, 22], [31, 26]]
36 [[2, 106], [3, 73], [5, 34], [7, 25], [11, 21], [13, 4], [17, 28], [19, 1], [23, 9], [29, 21], [31, 25]]
37 [[2, 72], [3, 56], [5, 26], [7, 20], [11, 18], [13, 2], [17, 26], [23, 8], [29, 20], [31, 24], [37, 36]]
38 [[2, 75], [3, 39], [5, 18], [7, 15], [11, 15], [17, 24], [19, 36], [23, 7], [29, 19], [31, 23], [37, 35]]
39 [[2, 40], [3, 60], [5, 10], [7, 10], [11, 12], [13, 36], [17, 22], [19, 34], [23, 6], [29, 18], [31, 22], [37, 34]]
40 [[2, 122], [3, 42], [5, 41], [7, 5], [11, 9], [13, 33], [17, 20], [19, 32], [23, 5], [29, 17], [31, 21], [37, 33]]
41 [[2, 84], [3, 24], [5, 32], [11, 6], [13, 30], [17, 18], [19, 30], [23, 4], [29, 16], [31, 20], [37, 32], [41, 40]]
42 [[2, 87], [3, 47], [5, 23], [7, 36], [11, 3], [13, 27], [17, 16], [19, 28], [23, 3], [29, 15], [31, 19], [37, 31], [41, 39]]
43 [[2, 48], [3, 28], [5, 14], [7, 30], [13, 24], [17, 14], [19, 26], [23, 2], [29, 14], [31, 18], [37, 30], [41, 38], [43, 42]]
44 [[2, 95], [3, 9], [5, 5], [7, 24], [11, 40], [13, 21], [17, 12], [19, 24], [23, 1], [29, 13], [31, 17], [37, 29], [41, 37], [43, 41]]
45 [[2, 54], [3, 78], [5, 40], [7, 18], [11, 36], [13, 18], [17, 10], [19, 22], [29, 12], [31, 16], [37, 28], [41, 36], [43, 40]]
46 [[2, 58], [3, 57], [5, 30], [7, 12], [11, 32], [13, 15], [17, 8], [19, 20], [23, 44], [29, 11], [31, 15], [37, 27], [41, 35], [43, 39]]
47 [[2, 16], [3, 36], [5, 20], [7, 6], [11, 28], [13, 12], [17, 6], [19, 18], [23, 42], [29, 10], [31, 14], [37, 26], [41, 34], [43, 38], [47, 46]]
48 [[2, 162], [3, 62], [5, 10], [11, 24], [13, 9], [17, 4], [19, 16], [23, 40], [29, 9], [31, 13], [37, 25], [41, 33], [43, 37], [47, 45]]
49 [[2, 116], [3, 40], [7, 90], [11, 20], [13, 6], [17, 2], [19, 14], [23, 38], [29, 8], [31, 12], [37, 24], [41, 32], [43, 36], [47, 44]]
50 [[2, 119], [3, 18], [5, 88], [7, 82], [11, 16], [13, 3], [19, 12], [23, 36], [29, 7], [31, 11], [37, 23], [41, 31], [43, 35], [47, 43]]
'''
# how many p until n
def pcount(n,p):
    r = 0
    while n > 0:
        n = n//p
        r +=n
    return r

def dpfcaddminus(ofc,nfc,n):
    fc = []
    i = 0
    j = 0
    ol = len(ofc)
    nl = len(nfc)
    while True:
        if i<ol and j <nl:
            if ofc[i][0]<nfc[j][0]:
                p = ofc[i][0]
                nc = ofc[i][1]-pcount(n,p)
                if nc > 0:
                    fc.append([p,nc])
                i += 1
            elif ofc[i][0]>nfc[j][0]:
                p = nfc[j][0]
                nc = nfc[j][1]*n-pcount(n,p)
                if nc > 0:
                    fc.append([p,nc])
                j += 1
            elif ofc[i][0]== nfc[j][0]:
                p = ofc[i][0]
                nc = ofc[i][1]+nfc[j][1]*n-pcount(n,p)
                if nc > 0:
                    fc.append([p,nc])
                j += 1
                i += 1
        elif i < ol:
            p = ofc[i][0]
            nc = ofc[i][1]-pcount(n,p)
            if nc > 0:
                fc.append([p,nc])
            i += 1
        elif j < nl:
            p = nfc[j][0]
            nc = nfc[j][1]*n-pcount(n,p)
            if nc > 0:
                fc.append([p,nc])
            j += 1
        else:
            break
    return fc


Barray = [[[0,0]],[[1,1]],[[2,1]]]

# dp
def dpfcBv4(n):
    lastB = [[2,1]]
    for i in range(3,n+1):
        fcn = factorof(i)
        newB = dpfcaddminus(lastB,fcn,i)
        Barray.append(newB)
        lastB = newB[:]
    return lastB
        

def Dv5(n):
    #print(n,fc)
    r = 1
    for f in Barray[n]:
        r *= ((f[0]**(f[1]+1)-1)//(f[0]-1))%modN
    return r%modN


def Sv5(n):
    r = 1+3
    for i in range(3,n+1):
        r += Dv5(i)
    return r%modN


# 100 332792866 time: 0.03291678428649902
# 200 271664942 time: 0.036899566650390625
# 500 899393748 time: 0.16055536270141602
# 1000 361160563 time: 0.8257837295532227
# 2000 939425731 time: 7.3325090408325195
# 3000 665284696 time: 28.13561749458313
def test6():
    N = 3000
    PrimeSieve(N)
    dpfcBv4(N)
    #print(Barray)
    print(Sv5(N))

def cpc(p,pc):
    for f in pc:
        if f[0] == p:
            return f[1]
    return 0

def dpfcnewB(ofc,nfc,n,pc):
    fc = []
    i = 0
    j = 0
    ol = len(ofc)
    nl = len(nfc)
    while True:
        if i<ol and j <nl:
            if ofc[i][0]<nfc[j][0]:
                p = ofc[i][0]
                nc = ofc[i][1]-cpc(p,pc)
                if nc > 0:
                    fc.append([p,nc])
                i += 1
            elif ofc[i][0]>nfc[j][0]:
                p = nfc[j][0]
                nc = nfc[j][1]*n-cpc(p,pc)
                if nc > 0:
                    fc.append([p,nc])
                j += 1
            elif ofc[i][0]== nfc[j][0]:
                p = ofc[i][0]
                nc = ofc[i][1]+nfc[j][1]*n-cpc(p,pc)
                if nc > 0:
                    fc.append([p,nc])
                j += 1
                i += 1
        elif i < ol:
            p = ofc[i][0]
            nc = ofc[i][1]-cpc(p,pc)
            if nc > 0:
                fc.append([p,nc])
            i += 1
        elif j < nl:
            p = nfc[j][0]
            nc = nfc[j][1]*n-cpc(p,pc)
            if nc > 0:
                fc.append([p,nc])
            j += 1
        else:
            break
    return fc
    

def dpSv6(n):
    r = 1+3
    newB = [[2,1]]
    newpc = [[2,1]]
    for i in range(3,n+1):
        Dr = 1
        fcn = factorof(i)
        newpc = fctimes(newpc,fcn)
        newB = dpfcnewB(newB,fcn,i,newpc)
        for f in newB:
            Dr *= ((f[0]**(f[1]+1)-1)//(f[0]-1))%modN
        r += (Dr%modN)
    return r%modN

# 3000 665284696 time: 34.27035593986511
def test7():
    N = 3000
    PrimeSieve(N)
    print(dpSv6(N))

def dpSv7(n):
    r = 1+3
    nB = [0]*(n+1)
    npc = [0]*(n+1)
    nB[2]=1
    npc[2]=1
    for i in range(3,n+1):
        Dr = 1
        for f in factorof(i):
            npc[f[0]] += f[1]
            nB[f[0]] += f[1]*i
        for p in Primes:
            if p > i:
                break
            nB[p] -= npc[p]
            #if nB[p]<0:
                #nB[p]=0
            if nB[p]>0:
                Dr *= ((p**(nB[p]+1)-1)//(p-1))%modN
        r += (Dr%modN)
    return r%modN

# 1000 361160563 time: 0.763925313949585
# 2000 939425731 time: 6.892565011978149
# 3000 665284696 time: 27.979575157165527
def test8():
    N = 20000
    PrimeSieve(N)
    print(dpSv7(N))

def ppower(p,power,modpN):
    if power == 1:
        return p
    if power == 0:
        return p
    if p == 1:
        return 1
    tpower = math.ceil(math.log(modpN,p))
    if power < tpower:
        return (p**power)%modpN
    return (ppower((p**tpower)%modpN,power//tpower,modpN)*(p**(power%tpower)))%modpN
    

#((p**(nB[p]+1)-1)//(p-1))%modN
def ppowersum(p,power):
    return ((ppower(p,power+1,(p-1)*modN)-1)//(p-1))%modN
    

def dpSv8(n):
    r = 1+3
    nB = [0]*(n+1)
    npc = [0]*(n+1)
    nB[2]=1
    npc[2]=1
    for i in range(3,n+1):
        Dr = 1
        for f in factorof(i):
            npc[f[0]] += f[1]
            nB[f[0]] += f[1]*i
        for p in Primes:
            if p > i:
                break
            nB[p] -= npc[p]
            #if nB[p]<0:
                #nB[p]=0
            if nB[p]>0:
                Dr *= ppowersum(p,nB[p])
        r += (Dr%modN)
    return r%modN

# 1000 361160563 time: 1.0770800113677979
# 2000 939425731 time: 4.796186447143555
# 3000 665284696 time: 11.141255378723145
# 4000 809670819 time: 19.79210591316223
def test9():
    N = 20000
    PrimeSieve(N)
    print(dpSv8(N))
    
# 20000 538319652 time: 550.7671763896942
def main():
    result = 0
    N = 20000
    PrimeSieve(N)
    result = dpSv8(N)
    print("result:", result)


if __name__ == '__main__':
    init()
    #test9()
    main()
    timespent()
