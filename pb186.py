import math
import time

t1 = time.time()

'''
sS = [0]

def S(k):
    global sS
    if len(sS) >= k+1:
        return sS[k]
    if k <= 55:
        r = (100003-200003*k+300007*k*k*k)%1000000
        sS.append(r)
        return r
    r = (sS[k-24]+sS[k-55])%1000000
    sS.append(r)
    return r
'''

snS = [0]*55
pnS = 0

def nS(k):
    global snS
    global pnS
    if k <= 55:
        r = (100003-200003*k+300007*k*k*k)%1000000
        snS[pnS] = r
        pnS += 1
        return r
    if pnS >= 55:
        pnS -= 55
    pnS24 = pnS - 24
    if pnS24 < 0:
        pnS24 += 55
    r = (snS[pnS] + snS[pnS24])%1000000
    snS[pnS] = r
    pnS += 1
    return r

recn = 0
def RecNr():
    global recn
    recn += 1
    caller = nS(2*recn-1)
    called = nS(2*recn)
    return [recn,caller,called]



phoneb = [-1]*(1000000)
phoneb[524287] = 0
cs = [[524287]]
cc = 1
fc = 1
#pc = 1

a = 0
while True:
    r = RecNr()
    if r[1] == r[2]:
        continue
    a += 1
    r1ci = phoneb[r[1]]
    r2ci = phoneb[r[2]]
    if r1ci < 0:
        if r2ci < 0:
            phoneb[r[1]] = cc
            phoneb[r[2]] = cc
            cs.append([r[1],r[2]])
            cc += 1
            #pc += 2
        else:
            phoneb[r[1]] = r2ci
            #pc += 1
            if r2ci == 0:
                fc += 1
            else:
                cs[r2ci].append(r[1])
    else:
        if r2ci < 0:
            phoneb[r[2]] = r1ci
            #pc += 1
            if r1ci == 0:
                fc += 1
            else:
                cs[r1ci].append(r[2])
        else:
            if r1ci == r2ci:
                continue
            ncn = r1ci
            wcn = r2ci
            if r1ci > r2ci:
                ncn = r2ci
                wcn = r1ci
            if ncn == 0:
                for j in cs[wcn]:
                    phoneb[j] = ncn
                    fc += 1
            else:
                for j in cs[wcn]:
                    phoneb[j] = ncn
                    cs[ncn].append(j)
    if fc >= 990000:
        print(a)
        break
    

print("time:",time.time()-t1)  





