import math
import time

def init():
    global init_time
    init_time = time.time()

def timespent():
    print("time:",time.time()-init_time)


modN = 1000000007

def ds(i):
    if i<10:
        return i
    return i%10+ds(i//10)


def sv1(n):
    i =1
    while True:
        if ds(i) == n:
            return i
        i += 1

def Sv1(n):
    r = 0
    for i in range(1,n+1):
        r += sv1(i)
    return r

def test1():
    s = 0
    for i in range(1,1001):
        t =sv1(i)
        s += t
        print(i,t,s)

# 10 8042614 time: 16.475619554519653
def test2():
    fN = 10
    f0 = 0
    f1 = 1
    f2 = 1
    fi_1 = f2
    fi_2 = f1
    r = Sv1(f2)
    for i in range(3,fN+1):
        fi = fi_1+fi_2
        fi_2 = fi_1
        fi_1 = fi
        r += Sv1(fi)
    print(r)

def sv2(n):
    if n <10:
        return n
    t = n//9
    r = 9
    for i in range(1,t):
        r = r*10+9
    l = n-t*9
    r = l*(r+1)+r
    return r


def Sv2(n):
    r = 0
    for i in range(1,n+1):
        r += sv2(i)
    return r


# 10 8042614 time: 0.03490591049194336
# 20 107042993 time: 1.1255123615264893
def test3():
    fN = 20
    f0 = 0
    f1 = 1
    f2 = 1
    fi_1 = f2
    fi_2 = f1
    r = Sv2(f2)
    for i in range(3,fN+1):
        fi = fi_1+fi_2
        fi_2 = fi_1
        fi_1 = fi
        r += Sv2(fi)
        if r > modN:
            r =r%modN
    print(r)

# 10 8042614 time: 0.027927398681640625
# 20 107042993 time: 0.7240746021270752
# 21 819891931 time: 2.1428627967834473
# 22 518149920 time: 7.490607738494873
def test4():
    fN = 21
    f0 = 0
    f1 = 1
    f2 = 1
    fi_1 = f2
    fi_2 = f1
    r = sv2(f2)*(fN-1)
    for i in range(3,fN+1):
        fi = fi_1+fi_2
        fi_2 = fi_1
        fi_1 = fi
        for j in range(fi_2+1,fi+1):
            r += (sv2(j)*(fN-i+1))%modN
        r =r%modN
    print(r)


def sv3(n):
    if n <10:
        return n
    t = n//9
    l = n-t*9
    # l99...99 total of t 9s
    # 999999999 mod 1000000007 = -8
    # 1000000000 mod 1000000007 = -7
    tn = t//9
    tr = t%9
    # l9...9 total of tr 9s times 1000000000**tn + 999999999*1000000000**(tn-1)...
    # l9..9 * (-7)**tn + (-8)*(-7)**(tn-1)...
    r = 0
    for i in range(0,tr):
        r = r*10+9
    r = l*(r+1)+r
    for i in range(tn):
        r=r*(-7)+(-8)
    return r%modN

def sv4(n):
    if n <10:
        return n
    t = n//9
    l = n-t*9
    # l99...99 total of t 9s
    # 999999999 mod 1000000007 = -8
    # 1000000000 mod 1000000007 = -7
    tn = t//9
    tr = t%9
    # l9...9 total of tr 9s times 1000000000**tn + 999999999*1000000000**(tn-1)...
    # l9..9 * (-7)**tn + (-8)*(-7)**(tn-1)...
    nines = [0,9,99,999,9999,99999,999999,9999999,99999999,999999999]
    r = (l+1)*nines[tr]+l
    tnm = ((-7)**tn)%modN
    r = r*tnm+(tnm-1)
    return r%modN

# 10 8042614 time: 0.028253793716430664
# 20 107042993 time: 0.12454986572265625
# 22 518149920 time: 0.4318413734436035
# 25 692437619 time: 9.805579662322998
def test5():
    fN = 25
    f0 = 0
    f1 = 1
    f2 = 1
    fi_1 = f2
    fi_2 = f1
    r = sv2(f2)*(fN-1)
    for i in range(3,fN+1):
        fi = fi_1+fi_2
        fi_2 = fi_1
        fi_1 = fi
        for j in range(fi_2+1,fi+1):
            r += sv3(j)*(fN-i+1)
        r =r%modN
    print(r)

# 22 518149920 time: 0.083770751953125
# 25 692437619 time: 0.3590407371520996
# 30 159166760 time: 66.29606628417969
def test6():
    fN = 30
    f0 = 0
    f1 = 1
    f2 = 1
    fi_1 = f2
    fi_2 = f1
    r = sv2(f2)*(fN-1)
    for i in range(3,fN+1):
        fi = fi_1+fi_2
        fi_2 = fi_1
        fi_1 = fi
        for j in range(fi_2+1,fi+1):
            r += sv4(j)*(fN-i+1)
        r =r%modN
    print(r)


def atobmodN(a,b):
    if a == 1:
        return 1
    tb = math.ceil(math.log(modN,a))
    if b < tb:
        return (a**b)%modN
    return (atobmodN((a**tb)%modN,b//tb)*(a**(b%tb)))%modN

def sv5(n):
    if n <10:
        return n
    t = n//9
    l = n-t*9
    # l99...99 total of t 9s
    # 999999999 mod 1000000007 = -8
    # 1000000000 mod 1000000007 = -7
    tn = t//9
    tr = t%9
    # l9...9 total of tr 9s times 1000000000**tn + 999999999*1000000000**(tn-1)...
    # l9..9 * (-7)**tn + (-8)*(-7)**(tn-1)...
    nines = [0,9,99,999,9999,99999,999999,9999999,99999999,999999999]
    r = (l+1)*nines[tr]+l
    tnm = atobmodN(modN-7,tn)
    r = r*tnm+(tnm-1)
    return r%modN

# s(9p)+s(9p+1)+..+s(9p+8)
def s9v1(p):
    nines = [0,9,99,999,9999,99999,999999,9999999,99999999,999999999]
    r = (nines[p%9]+1)*atobmodN(modN-7,p//9)-1
    return (r*45+36)%modN
    

# sv4
# 25 692437619 time: 0.09530782699584961
# 30 159166760 time: 7.487579822540283
# 31 979170050 time: 25.237095832824707
# sv5
# 30 159166760 time: 2.349902391433716
# 31 979170050 time: 4.3732709884643555
# 35 645435163 time: 34.41228008270264
# s9v1
# 35 645435163 time: 33.09933662414551
def test7():
    fN = 35
    f0 = 0
    f1 = 1
    f2 = 1
    fi_1 = f2
    fi_2 = f1
    r = sv2(f2)*(fN-1)
    for i in range(3,fN+1):
        fi = fi_1+fi_2
        fi_2 = fi_1
        fi_1 = fi
        # fi_2+1...9p-1, 9p...9q-1, 9q...fi
        # 99..99, 199..99,,,899..99
        # 99..99*(1+2+..+9)+(1+2+..+8)
        fstart = fi_2+1
        fend = fi
        if fend-fstart > 18:
            fsp = fstart//9+1
            feq = fend//9
            for j in range(fstart,9*fsp):
                r += sv5(j)*(fN-i+1)
            for j in range(fsp,feq):
                r += s9v1(j)*(fN-i+1)
            for j in range(9*feq,fend+1):
                r += sv5(j)*(fN-i+1)
            r =r%modN
        else:
            for j in range(fstart,fend+1):
                r += sv4(j)*(fN-i+1)
            r =r%modN
    print(r)

# s(81p)+s(81p+1)+..+s(81p+80)
def s81v1(p):
    # r = (nines[0,1,...,8]+1)*atobmodN(modN-7,p)-1
    r = 111111111*atobmodN(modN-7,p)*45-81
    return r%modN


# s81v1
# 30 159166760 time: 0.2797408103942871
# 35 645435163 time: 3.5950522422790527
# 36 174686725 time: 6.78250789642334
def test8():
    fN = 40
    f0 = 0
    f1 = 1
    f2 = 1
    fi_1 = f2
    fi_2 = f1
    r = sv2(f2)*(fN-1)
    for i in range(3,fN+1):
        fi = fi_1+fi_2
        fi_2 = fi_1
        fi_1 = fi
        # S(fi)
        fstart = fi_2+1
        fend = fi
        if fend-fstart > 18:
            fsp = fstart//9+1
            feq = fend//9
            for j in range(fstart,9*fsp):
                r += sv5(j)*(fN-i+1)
            if feq -fsp > 18:
                fspp = fsp//9+1
                feqq = feq//9
                for j in range(fsp,fspp*9):
                    r += s9v1(j)*(fN-i+1)
                for j in range(fspp,feqq):
                    r += s81v1(j)*(fN-i+1)
                for j in range(feqq*9,feq):
                    r += s9v1(j)*(fN-i+1)
            else:
                for j in range(fsp,feq):
                    r += s9v1(j)*(fN-i+1)
            for j in range(9*feq,fend+1):
                r += sv5(j)*(fN-i+1)
            r =r%modN
        else:
            for j in range(fstart,fend+1):
                r += sv4(j)*(fN-i+1)
            r =r%modN
    print(r)



# 35 645435163 time: 0.1246483325958252
# 40 570500927 time: 0.9384679794311523
# 43 575042599 time: 3.7884631156921387
# 44 562446383 time: 6.180696964263916
def test9():
    fN = 15
    f0 = 0
    f1 = 1
    f2 = 1
    fi_1 = f2
    fi_2 = f1
    r = sv2(f2)*(fN-1)
    for i in range(3,fN+1):
        fi = fi_1+fi_2
        fi_2 = fi_1
        fi_1 = fi
        stimes = (fN-i+1)
        # S(fi)
        fstart = fi_2+1
        fend = fi
        if fend-fstart > 18:
            fsp = fstart//9+1
            feq = fend//9
            for j in range(fstart,9*fsp):
                r += sv5(j)*stimes
            if feq -fsp > 18:
                fspp = fsp//9+1
                feqq = feq//9
                for j in range(fsp,fspp*9):
                    r += s9v1(j)*stimes
                temp = atobmodN(modN-7,fspp)
                for j in range(fspp,feqq):
                    r += (111111111*temp*45-81)*stimes
                    temp = (temp*-7)%modN
                for j in range(feqq*9,feq):
                    r += s9v1(j)*stimes
            else:
                for j in range(fsp,feq):
                    r += s9v1(j)*stimes
            for j in range(9*feq,fend+1):
                r += sv5(j)*stimes
            r =r%modN
        else:
            for j in range(fstart,fend+1):
                r += sv4(j)*stimes
            r =r%modN
    print(r)

def atobmod8N(a,b):
    if a == 1:
        return 1
    tb = math.ceil(math.log(8*modN,a))
    if b < tb:
        return (a**b)%(8*modN)
    return (atobmod8N((a**tb)%(8*modN),b//tb)*(a**(b%tb)))%(8*modN)

# 40 570500927 time: 0.057847023010253906
def main():
    result = 0
    fN = 90
    f0 = 0
    f1 = 1
    f2 = 1
    fi_1 = f2
    fi_2 = f1
    r = sv2(f2)*(fN-1)
    for i in range(3,fN+1):
        fi = fi_1+fi_2
        fi_2 = fi_1
        fi_1 = fi
        stimes = (fN-i+1)
        # S(fi)
        fstart = fi_2+1
        fend = fi
        if fend-fstart > 18:
            fsp = fstart//9+1
            feq = fend//9
            for j in range(fstart,9*fsp):
                r += sv5(j)*stimes
            if feq -fsp > 18:
                fspp = fsp//9+1
                feqq = feq//9
                for j in range(fsp,fspp*9):
                    r += s9v1(j)*stimes
                temp = atobmodN(modN-7,fspp)
                fpptqq = feqq-fspp
                temps = -((atobmod8N(modN*8-7,fpptqq)-8*modN-1)//8)
                r += 111111111*temp*temps*45*stimes-81*stimes*fpptqq
                for j in range(feqq*9,feq):
                    r += s9v1(j)*stimes
            else:
                for j in range(fsp,feq):
                    r += s9v1(j)*stimes
            for j in range(9*feq,fend+1):
                r += sv5(j)*stimes
            r =r%modN
        else:
            for j in range(fstart,fend+1):
                r += sv4(j)*stimes
            r =r%modN
        result = r
    print("result:", result)


if __name__ == '__main__':
    init()
    #test9()
    main()
    timespent()
