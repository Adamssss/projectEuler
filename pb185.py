import math
import time

t1 = time.time()

N = 16

#39542
rulestring = "90342 ;2 correct70794 ;0 correct39458 ;2 correct34109 ;1 correct51545 ;2 correct12531 ;1 correct"

if N == 16:
    rulestring = "5616185650518293 ;2 correct3847439647293047 ;1 correct5855462940810587 ;3 correct9742855507068353 ;3 correct4296849643607543 ;3 correct3174248439465858 ;1 correct4513559094146117 ;2 correct7890971548908067 ;3 correct8157356344118483 ;1 correct2615250744386899 ;2 correct8690095851526254 ;3 correct6375711915077050 ;1 correct6913859173121360 ;1 correct6442889055042768 ;2 correct2321386104303845 ;0 correct2326509471271448 ;2 correct5251583379644322 ;2 correct1748270476758276 ;3 correct4895722652190306 ;1 correct3041631117224635 ;3 correct1841236454324589 ;3 correct2659862637316867 ;2 correct"

# rules[i] = [[a,b,c,d,e],correctnumber]
rules = []
i = 0
while i < len(rulestring):
    r = []
    for j in range(N):
        r.append(ord(rulestring[i+j])-48)
    c = ord(rulestring[i+N+2])-48
    rules.append([r,c])
    i += N + 11


#=================================decipher8===================================

sortedrules = []
for i in [0,1,2,3]:
    for j in rules:
        if j[1] == i:
            sortedrules.append(j)

posc = []
for i in range(N):
    t = []
    for j in range(10):
        if j != sortedrules[0][0][i]:
            t.append(j)
    posc.append(t)

sortedrules.pop(0)

# Because it said to be unique solution
# the third digit can not be 0,3,6,8 as they don't show up in any rule
# if it is 0 then it can also be 3 and 6 and 8
# resulting multiple solutions
# Thus
if N == 16:
    posc[2] = [1, 4, 5, 7, 9]#from [0, 1, 3, 4, 5, 6, 7, 8, 9]
    posc[6] = [0, 1, 2, 3, 5, 8, 9]#from [0, 1, 2, 3, 4, 5, 7, 8, 9]
    posc[8] = [1, 3, 4, 5, 7, 9]#from [1, 2, 3, 4, 5, 6, 7, 8, 9]

def formone(opc):
    npc = []
    for i in range(16):
        npct = []
        for j in opc[i]:
            tt = []
            for r in sortedrules:
                if r[0][i] == j:
                    tt.append(1)
                else:
                    tt.append(0)
            npct.append([[j],tt])
        npc.append(npct)
    return npc

def onetotwo(pc):
    npc = []
    for i in range(8):
        npct = []
        for a in pc[i*2]:
            for b in pc[i*2+1]:
                tt = []
                possible = True
                for r in range(21):
                    cn = a[1][r]+b[1][r]
                    if cn > sortedrules[r][1]:
                        possible = False
                        break
                    tt.append(cn)
                if possible:
                    npct.append([a[0]+b[0],tt])
        npc.append(npct)
    return npc

def twotofour(pc):
    npc = []
    for i in range(4):
        npct = []
        for a in pc[i*2]:
            for b in pc[i*2+1]:
                tt = []
                possible = True
                for r in range(21):
                    cn = a[1][r]+b[1][r]
                    if cn > sortedrules[r][1]:
                        possible = False
                        break
                    tt.append(cn)
                if possible:
                    npct.append([a[0]+b[0],tt])
        npc.append(npct)
    return npc

def fourtoeight(pc):
    # 6 rules of 0/1 ---> 0~63
    # 7 rules of 0/1/2 ---> 0~2186
    # 8 rules of 0/1/2/3 --> 0~65535
    npc = []
    for i in range(2):
        npct = []
        for t in range(64*2187):
            tt = []
            npct.append(tt)
        for a in pc[i*2]:
            for b in pc[i*2+1]:
                tt = []
                possible = True
                for r in range(21):
                    cn = a[1][r]+b[1][r]
                    if cn > sortedrules[r][1]:
                        possible = False
                        break
                    tt.append(cn)
                if possible:
                    zoi = tt[0]*32+tt[1]*16+tt[2]*8+tt[3]*4+tt[4]*2+tt[5]
                    zoti = tt[6]*729+tt[7]*243+tt[8]*81+tt[9]*27+tt[10]*9+tt[11]*3+tt[12]
                    npct[zoi*2187+zoti].append([a[0]+b[0],tt])
        npc.append(npct)
    return npc

def eighttosixteen(pc):
    for i in range(len(pc[0])):
        zoi = i//2187
        zoti = i%2187
        # 110101 need 001010
        # and 1121002 would need 1101220
        j = (63-zoi)*2187+(2186-zoti)
        for a in pc[0][i]:
            for b in pc[1][j]:
                found = True
                for r in range(21):
                    cn = a[1][r]+b[1][r]
                    if cn != sortedrules[r][1]:
                        found = False
                        break
                if found:
                    return a[0]+b[0]

def decipher8():
    oposc = formone(posc)
    tposc = onetotwo(oposc)
    fposc = twotofour(tposc)
    eposc = fourtoeight(fposc)
    sposc = eighttosixteen(eposc)
    r = 0
    for i in sposc:
        r = r*10+i
    return r

print(decipher8())
     
print("time:",time.time()-t1)
#4640261571849533
#time: 178.17757987976074


# ------------------------------decipher8----------------------------------



'''
#=============================decipher1=======================
def comparewith(n,r):
    t = n
    c = 0
    for i in range(N):
        td = t %10
        t = t//10
        if r[0][N-1-i] == td:
            c += 1
    return c == r[1]

def compare(n):
    for j in rules:
        if not comparewith(n,j):
            return False
    return True

def decipher1():
    #pi = 10**(N-4)
    for i in range(10**N):
        #if i%pi == 0:
            #print(str(i//pi/100)+"%")
            #print("time:",time.time()-t1)  
        if compare(i):
            return i

print(decipher1())

print("time:",time.time()-t1)
#-----------------------decipher1---------------------
'''


'''
#========================decipher2============================
#print(10**16)                 10000000000000000    1
#print(9**16)                   1853020188851841    1
#print(16*(9**15))              3294258113514384    16
#print(16*15//2*(9**14))        2745215094595320    120
#print(16*15*14//6*(9**13))     1423444863864240    560

def decipher2():
    sortedrules = []
    for i in [0,1,2,3]:
        for j in rules:
            if j[1] == i:
                sortedrules.append(j)
    possiblecomb = []
    init = []
    for i in range(N):
        d = []
        for j in range(10):
            d.append(j)
        init.append(d)
    possiblecomb.append(init)
    while True:
        bri = 0
        bric = 10**N
        bril = 10**N
        bripc = []
        for ri in range(len(sortedrules)):
            r = sortedrules[ri]
            if r[1] > sortedrules[0][1]:
                break
            ncomb = []
            for c in possiblecomb:
                if r[1] == 0:
                    t = []
                    for i in range(N):
                        d = []
                        for j in range(10):
                            if r[0][i] != j:
                                if j in c[i]:
                                    d.append(j)
                        if len(d)>0:
                            t.append(d)
                        else:
                            break
                    if len(t) == N:
                        ncomb.append(t)
                    continue
                if r[1] == 1:
                    for cd in range(N):
                        t = []
                        for i in range(N):
                            if cd == i:
                                if r[0][i] in c[i]:
                                    t.append([r[0][i]])
                            else:
                                d = []
                                for j in range(10):
                                    if r[0][i] != j:
                                        if j in c[i]:
                                            d.append(j)
                                if len(d)>0:
                                    t.append(d)
                                else:
                                    break
                        if len(t) == N:
                            ncomb.append(t)
                    continue
                if r[1] == 2:
                    for cd1 in range(N-1):
                        for cd2 in range(cd1+1,N):
                            t = []
                            for i in range(N):
                                if cd1 == i or cd2 == i:
                                    if r[0][i] in c[i]:
                                        t.append([r[0][i]])
                                else:
                                    d = []
                                    for j in range(10):
                                        if r[0][i] != j:
                                            if j in c[i]:
                                                d.append(j)
                                    if len(d)>0:
                                        t.append(d)
                                    else:
                                        break
                            if len(t) == N:
                                ncomb.append(t)
                    continue
                if r[1] == 3:
                    for cd1 in range(N-2):
                        for cd2 in range(cd1+1,N-1):
                            for cd3 in range(cd2+1,N):
                                t = []
                                for i in range(N):
                                    if cd1 == i or cd2 == i or cd3 == i:
                                        if r[0][i] in c[i]:
                                            t.append([r[0][i]])
                                    else:
                                        d = []
                                        for j in range(10):
                                            if r[0][i] != j:
                                                if j in c[i]:
                                                    d.append(j)
                                        if len(d)>0:
                                            t.append(d)
                                        else:
                                            break
                                if len(t) == N:
                                    ncomb.append(t)
                    continue
            ric = countpos(ncomb)
            ril = len(ncomb)
            #print(ri,ric,ril)
            if ric == 1:
                return tonumberset(ncomb)[0]
            if ril < bril:
                bri = ri
                bripc = ncomb[:]
                bric = ric
                bril = ril
        possiblecomb = bripc[:]
        sortedrules.pop(bri)
        #print(countpos(possiblecomb),len(possiblecomb),time.time()-t1)

def countpos(pc):
    r = 0
    for i in pc:
        p = 1
        for j in i:
            p *= len(j)
        r += p
    return r

def tonumberset(pc):
    nset = []
    for c in pc:
        t = []
        for j in c[0]:
            t.append(j)
        for i in range(1,N):
            nt = []
            for kt in t:
                for j in c[i]:
                    nt.append(kt*10+j)
            t = nt[:]
        nset += t[:]
    return nset


print(decipher2())

print("time:",time.time()-t1)
#------------------------decipher2------------------------------------
'''

'''

# =============decipher3==================
def decipher3(passi):
    sortedrules = []
    for i in [0,1,2,3]:
        for j in rules:
            if j[1] == i:
                sortedrules.append(j)
    i = passi
    pid = 8
    pi = i[pid]
    while True:
        #print(i)
        if pi != i[pid]:
            pi = i[pid]
            print(str(ton(i[:pid+1])/(10**(pid-2)))+"%",i,time.time()-t1)
        tr = -1
        for r in sortedrules:
            tr = test(i,r)
            if tr > 0:
                break
        if tr == -1:
            return ton(i)
        i = addi(i,tr)

def test(i,r):
    cc = 0
    for d in range(N):
        if i[d] == r[0][d]:
            cc += 1
        if cc > r[1]:
            return d
    if cc == r[1]:
        return -1
    return N-1

def addi(i,tr):
    r = i[:]
    r[tr] += 1
    while tr > -1:
        if r[tr] > 9:
            r[tr] =0
            if tr > 0:
                r[tr-1] += 1
        else:
            return r
        tr -= 1
    return r

def ton(i):
    r = 0
    for j in i:
        r = r*10+j
    return r

#print(decipher3([0]*(N)))

print(decipher3([0, 0, 0, 0, 1, 3, 5, 3, 6, 0, 0, 2, 2, 1, 1, 8]))

print("time:",time.time()-t1)

# ---------decipher3-------------------
'''

'''
# ========log decipher3
0.000178% [0, 0, 0, 0, 0, 0, 1, 7, 8, 0, 0, 0, 0, 0, 0, 0] 1610.1507456302643
0.000222% [0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 1, 6, 3] 217.77880096435547
0.000392% [0, 0, 0, 0, 0, 0, 3, 9, 2, 0, 0, 1, 0, 0, 0, 8] 1740.8299498558044
0.000758% [0, 0, 0, 0, 0, 0, 7, 5, 8, 0, 0, 0, 0, 0, 0, 0] 3208.531951904297
0.001338% [0, 0, 0, 0, 0, 1, 3, 3, 8, 0, 0, 0, 0, 0, 0, 0] 2683.3293178081512
0.001523% [0, 0, 0, 0, 0, 1, 5, 2, 3, 0, 0, 0, 0, 0, 0, 0] 1005.9654905796051
0.002557% [0, 0, 0, 0, 0, 2, 5, 5, 7, 0, 0, 0, 0, 1, 8, 0] 4426.74426651001
0.003135% [0, 0, 0, 0, 0, 3, 1, 3, 5, 0, 0, 1, 0, 1, 0, 0] 2681.26482629776
0.004369% [0, 0, 0, 0, 0, 4, 3, 6, 9, 0, 0, 1, 0, 1, 0, 0] 6638.338195800781
0.005028% [0, 0, 0, 0, 0, 5, 0, 2, 8, 0, 0, 2, 5, 1, 0, 7] 2386.563508272171
0.006004% [0, 0, 0, 0, 0, 6, 0, 0, 4, 0, 0, 1, 0, 0, 0, 0] 2115.6074969768524
0.006228% [0, 0, 0, 0, 0, 6, 2, 2, 8, 0, 0, 0, 7, 1, 0, 3] 4002.2169377803802
0.006546% [0, 0, 0, 0, 0, 6, 5, 4, 6, 0, 0, 1, 0, 1, 8, 7] 3449.1341433525085
0.007428% [0, 0, 0, 0, 0, 7, 4, 2, 8, 0, 0, 0, 0, 0, 0, 0] 7204.223630428314
0.009027% [0, 0, 0, 0, 0, 9, 0, 2, 7, 0, 0, 0, 0, 0, 0, 0] 4719.293655395508
0.009423% [0, 0, 0, 0, 0, 9, 4, 2, 3, 0, 0, 0, 0, 0, 0, 0] 3811.038725376129
0.009751% [0, 0, 0, 0, 0, 9, 7, 5, 1, 0, 0, 1, 0, 0, 0, 0] 2763.4022512435913
0.010004% [0, 0, 0, 0, 1, 0, 0, 0, 4, 0, 0, 1, 0, 0, 0, 0] 1817.9265341758728
0.013189% [0, 0, 0, 0, 1, 3, 1, 8, 9, 0, 0, 0, 0, 0, 0, 0] 15037.007983207703
0.013536% [0, 0, 0, 0, 1, 3, 5, 3, 6, 0, 0, 2, 2, 1, 1, 8] 2158.76797580719




#-------------------log3
'''



'''
#========================decipher4============================

def decipher4(r):
    if not possible(r):
        return []
    if len(r[0][0]) == 1:
        resultb = [True]*10
        rc = 0
        for i in r:
            if i[1] == 0:
                resultb[i[0][0]] = False
            if i[1] == 1:
                rc += 1
                fr = [i[0][0]]
        if rc > 1:
            return []
        if rc == 1:
            return fr
        fr = []
        for j in range(10):
            if resultb[j]:
                fr.append(j)
        return fr
    fr = []
    for i in range(10):
        nr = newrule(r,i)
        dr = decipher4(nr)
        pn = 10**(len(nr[0][0]))
        for j in dr:
            fr.append(i*pn+j)
    return fr

def possible(r):
    for i in r:
        if i[1] < 0:
            return False
        if len(i[0]) < i[1]:
            return False
    return True

def newrule(r,i):
    nr = []
    for j in r:
        cd = j[1]
        if i == j[0][0]:
            cd -= 1
        nr.append([j[0][1:],cd])
    return nr
    
print(decipher4(rules)[0])

print("time:",time.time()-t1)
#------------------------decipher4------------------------------------
'''

'''
#========================decipher5=====================================
prN = 9**N

sortedrules = []
for i in [0,1,2,3]:
    for j in rules:
        if j[1] == i:
            sortedrules.append(j)
            
posc = []
for i in range(N):
    t = []
    for j in range(10):
        if j != sortedrules[0][0][i]:
            t.append(j)
    posc.append(t)

sortedrules.pop(0)

def countpos(pc):
    p = len(pc[0])
    for j in range(1,len(pc)):
        p *= len(pc[j])
    return p

def test(pc,rs,d,n):
    npc = pc[:]
    npc[d] = [n]
    for r in rs:
        if r[1] == 1:
            if r[0][d] == n:
                for i in range(N):
                    if i != d:
                        if r[0][i] in npc[i]:
                            npci = npc[i][:]
                            npci.pop(npci.index(r[0][i]))
                            npc[i] = npci[:]
    return npc

def uprule(rs,d,n):
    nr = []
    for r in rs:
        if r[0][d] == n:
            url = r[0][:]
            url[d] = -1
            urc = r[1] -1
            if urc > 0:
                nr.append([url,urc])
        else:
            nr.append(r)
    return nr

stepn = -1

def decipher5(pc,oc,rs,gn,pr):
    global stepn
    ocount = oc
    bcount = ocount
    if gn <= 4:
        percent = (round((prN-pr)/prN*100000))/1000
        s = ""
        for i in range(gn):
            s += "==="
        print(str(percent)+"%",pr,s,gn,bcount,time.time()-t1)
        if gn == 0:
            stepn += 1
            print("--->step:",stepn)
            for j in pc:
                print(len(j),j)
            print("======================================================================")
            print(pc)
            print("======================================================================")
            print(ocount,time.time()-t1)
    if bcount == 1:
        tr = testrules(pc)
        if tr > 0:
            #print(tr)
            return [[tr]]
        else:
            return [[]]
    if bcount == 0:
        return [[]]
    btestr = []
    bdi = 0
    bnj = 0
    for di in range(N):
        if len(pc[di]) > 1:
            for nj in pc[di]:
                testr = test(pc,rs,di,nj)
                count = countpos(testr)
                if count < bcount:
                    bcount = count
                    bdi = di
                    bnj = nj
                    btestr = testr[:]
                if bcount == 0:
                    break
        if bcount == 0:
            break
    if bcount == 0:
        ntest = pc[:]
        ntest[bdi] = []
        for j in pc[bdi]:
            if j != bnj:
                ntest[bdi].append(j)
        ncount = countpos(ntest)
        return decipher5(ntest,ncount,rs,gn,pr-(ocount-ncount))
    if bcount < 5000:
        #print(bcount,btestr)
        tr = testrules(btestr)
        if tr > 0:
            return [[tr]]
        else:
            ntest = pc[:]
            ntest[bdi] = []
            for j in pc[bdi]:
                if j != bnj:
                    ntest[bdi].append(j)
            ncount = countpos(ntest)
            return decipher5(ntest,ncount,rs,gn,pr-(ocount-ncount))
    nrs = uprule(rs,bdi,bnj)
    nd = decipher5(btestr,bcount,nrs,gn+1,pr)
    ncount = countpos(nd)
    if ncount == 0:
        ntest = pc[:]
        ntest[bdi] = []
        for j in pc[bdi]:
            if j != bnj:
                ntest[bdi].append(j)
        ncount = countpos(ntest)
        return decipher5(ntest,ncount,rs,gn,pr-(ocount-ncount))
    return nd
    
def testrules(pc):
    testpool = pc[0]
    for i in range(1,len(pc)):
        ntp = []
        for j in testpool:
            for k in pc[i]:
                ntp.append(j*10+k)
        testpool = ntp[:]
    #print(len(testpool))
    for i in testpool:
        if compare(i):
            return i
    return -1
        

def comparewith(n,r):
    t = n
    c = 0
    for i in range(N):
        td = t %10
        t = t//10
        if r[0][N-1-i] == td:
            c += 1
            if c > r[1]:
                return False
    return c == r[1]

def compare(n):
    for j in rules:
        if not comparewith(n,j):
            return False
    return True        


#posc = [[0, 1, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8, 9], [0, 1, 3, 4, 5, 6, 7, 8, 9], [0, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 9], [0, 1, 2, 3, 4, 5, 7, 8, 9], [0, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 9], [0, 1, 2, 3, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 6, 7, 8, 9]]

prN = countpos(posc)

print(decipher5(posc,prN,rules,0,prN)[0][0])

print("time:",time.time()-t1)
#----------------------------decipher5---------------------------------
'''

'''
# ============================log decipher5 ===========================

--->step: 0
9 [0, 1, 3, 4, 5, 6, 7, 8, 9]
9 [0, 1, 2, 4, 5, 6, 7, 8, 9]
9 [0, 1, 3, 4, 5, 6, 7, 8, 9]
9 [0, 2, 3, 4, 5, 6, 7, 8, 9]
9 [0, 1, 2, 4, 5, 6, 7, 8, 9]
9 [0, 1, 2, 3, 4, 5, 6, 7, 9]
9 [0, 1, 2, 3, 4, 5, 7, 8, 9]
9 [0, 2, 3, 4, 5, 6, 7, 8, 9]
9 [1, 2, 3, 4, 5, 6, 7, 8, 9]
9 [0, 1, 2, 3, 5, 6, 7, 8, 9]
9 [0, 1, 2, 4, 5, 6, 7, 8, 9]
9 [1, 2, 3, 4, 5, 6, 7, 8, 9]
9 [0, 1, 2, 4, 5, 6, 7, 8, 9]
9 [0, 1, 2, 3, 4, 5, 6, 7, 9]
9 [0, 1, 2, 3, 5, 6, 7, 8, 9]
9 [0, 1, 2, 3, 4, 6, 7, 8, 9]
======================================================================
[[0, 1, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8, 9], [0, 1, 3, 4, 5, 6, 7, 8, 9], [0, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 9], [0, 1, 2, 3, 4, 5, 7, 8, 9], [0, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 9], [0, 1, 2, 3, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 6, 7, 8, 9]]
======================================================================
1853020188851841 0.07718706130981445







# ------------------------------log5------------------------------------
'''


'''
#=================================decipher6===================================
maxmemorysize = 10**9

sortedrules = []
for i in [0,3,2,1]:
    for j in rules:
        if j[1] == i:
            sortedrules.append(j)

posc = []
for i in range(N):
    t = []
    for j in range(10):
        if j != sortedrules[0][0][i]:
            t.append(j)
    posc.append(t)

def countpos(pc):
    p = len(pc[0])
    for j in range(1,len(pc)):
        p *= len(pc[j])
    return p

# Because it said to be unique solution
# the third digit can not be 0,3,6,8 as they don't show up in any rule
# if it is 0 then it can also be 3 and 6 and 8
# resulting multiple solutions
# Thus
posc[2] = [1,4,5,7,9]#from [0, 1, 3, 4, 5, 6, 7, 8, 9]
posc[6] = [0, 1, 2, 3, 5, 8, 9]#from [0, 1, 2, 3, 4, 5, 7, 8, 9]
posc[8] = [1, 3, 4, 5, 7, 9]#from [1, 2, 3, 4, 5, 6, 7, 8, 9]



print(countpos(posc))


lper = 160160

def decipher6():
    a = 0
    for cd11 in range(0,N-2):
        for cd12 in range(cd11+1,N-1):
            for cd13 in range(cd12+1,N):
                for cd21 in range(0,N-2):
                    if cd21 != cd11 and cd21 != cd12 and cd21 != cd13:
                        for cd22 in range(cd21+1,N-1):
                            if cd22 != cd11 and cd22 != cd12 and cd22 != cd13:
                                for cd23 in range(cd22+1,N):
                                    if cd23 != cd11 and cd23 != cd12 and cd23 != cd13:
                                        temppc = []
                                        for i in range(N):
                                            tt = []
                                            if i == cd11 or i == cd12 or i ==  cd13:
                                                temppc.append([sortedrules[1][0][i]])
                                                continue
                                            if i == cd21 or i == cd22 or i == cd23:
                                                temppc.append([sortedrules[2][0][i]])
                                                continue
                                            for j in posc[i]:
                                                if j != sortedrules[1][0][i] and j != sortedrules[2][0][i]:
                                                    tt.append(j)
                                            temppc.append(tt)
                                        #n = countpos(temppc)
                                        result = decipher6part2(temppc,3)
                                        #result = testrules(temppc)
                                        a += 1
                                        print(round(a/lper*10000)/100,"%",a,time.time()-t1,(time.time()-t1)*lper/a)
                                        if result > 0:
                                            return result
rnlimit = 6

def decipher6part2(pc,rn):
    for cd11 in range(0,N-2):
        for cd12 in range(cd11+1,N-1):
            for cd13 in range(cd12+1,N):
                temppc = []
                for i in range(N):
                    tt = []
                    if i == cd11 or i == cd12 or i ==  cd13:
                        if sortedrules[rn][0][i] in pc[i]:
                            temppc.append([sortedrules[rn][0][i]])
                            continue
                        else:
                            temppc.append([])
                    for j in pc[i]:
                        if j != sortedrules[rn][0][i]:
                            tt.append(j)
                    temppc.append(tt)
                npc = countpos(temppc)
                if npc == 0:
                    continue
                if rn < rnlimit and npc > 10:
                    result =decipher6part2(temppc,rn+1)
                else:
                    result = testrules(pc)
                if result > 0:
                    return result
    return -1

def testrules(pc):
    testpool = pc[0]
    for i in range(1,len(pc)):
        ntp = []
        for j in testpool:
            for k in pc[i]:
                ntp.append(j*10+k)
        testpool = ntp[:]
    #print(len(testpool))
    for i in testpool:
        if compare(i):
            return i
    return -1

def compare(n):
    for j in range(rnlimit+1,len(sortedrules)):
        if not comparewith(n,sortedrules[j]):
            return False
    return True 

def comparewith(n,r):
    t = n
    c = 0
    for i in range(N):
        td = t %10
        t = t//10
        if r[0][N-1-i] == td:
            c += 1
            if c > r[1]:
                return False
    return c == r[1]


def decipher6dividestep(cd11,cd12,cd13,a):
    for cd21 in range(0,N-2):
        if cd21 != cd11 and cd21 != cd12 and cd21 != cd13:
            for cd22 in range(cd21+1,N-1):
                if cd22 != cd11 and cd22 != cd12 and cd22 != cd13:
                    for cd23 in range(cd22+1,N):
                        if cd23 != cd11 and cd23 != cd12 and cd23 != cd13:
                            temppc = []
                            for i in range(N):
                                tt = []
                                if i == cd11 or i == cd12 or i ==  cd13:
                                    temppc.append([sortedrules[1][0][i]])
                                    continue
                                if i == cd21 or i == cd22 or i == cd23:
                                    temppc.append([sortedrules[2][0][i]])
                                    continue
                                for j in posc[i]:
                                    if j != sortedrules[1][0][i] and j != sortedrules[2][0][i]:
                                        tt.append(j)
                                temppc.append(tt)
                            #n = countpos(temppc)
                            result = decipher6part2(temppc,3)
                            #result = testrules(temppc)
                            a += 1
                            print(round(a/lper*10000)/100,"%",a,time.time()-t1)
                            if result > 0:
                                return result
    print("============================================")
    print([cd11,cd12,cd13,a],time.time()-t1)
    return -1

def decipher6divide(divinfo):
    k1 = divinfo[0]
    k2 = divinfo[1]
    k3 = divinfo[2]
    a = divinfo[3]
    while True:
        result = decipher6dividestep(k1,k2,k3,a)
        if result > 0:
            return result
        k3 += 1
        if k3 == N:
            k2 += 1
            k3 = k2 + 1
            if k2 == N:
                k1 += 1
                k2 = k1+1


divinfo = [0, 1, 2, 0]
print(decipher6divide(divinfo))
    
     
print("time:",time.time()-t1)
# -----------------------------decipher6-------------------------------
'''


'''
================================decipher6 log===============================
[0, 1, 2, 286] 6001.048817396164












---------------------------------log6-------------------------------------

'''

'''
#=================================decipher7===================================


sortedrules = []
for i in [0,1,2,3]:
    for j in rules:
        if j[1] == i:
            sortedrules.append(j)

posc = []
for i in range(N):
    t = []
    for j in range(10):
        if j != sortedrules[0][0][i]:
            t.append(j)
    posc.append(t)

def countpos(pc):
    p = len(pc[0])
    for j in range(1,len(pc)):
        p *= len(pc[j])
    return p

sortedrules.pop(0)

# Because it said to be unique solution
# the third digit can not be 0,3,6,8 as they don't show up in any rule
# if it is 0 then it can also be 3 and 6 and 8
# resulting multiple solutions
# Thus
if N == 16:
    posc[2] = [1, 4, 5, 7, 9]#from [0, 1, 3, 4, 5, 6, 7, 8, 9]
    posc[6] = [0, 1, 2, 3, 5, 8, 9]#from [0, 1, 2, 3, 4, 5, 7, 8, 9]
    posc[8] = [1, 3, 4, 5, 7, 9]#from [1, 2, 3, 4, 5, 6, 7, 8, 9]

perlevel = 7
per = 0
poss = countpos(posc)
posstep = poss//100//(10**perlevel)
possthre = poss-posstep

def guessone(pc,rs):
    global per, poss,possthre
    if poss <= possthre:
        per += math.pow(10,-perlevel)
        possthre -= posstep
        print(per,poss,time.time()-t1,totime((time.time()-t1)/per*(100-per)))
    if len(pc) == 1:
        cd = []
        for r in rs:
            if r[1] == 1:
                cd.append(r[0][0])
            else :
                poss -= len(pc[0])
                return -1
        if len(cd) > 1:
            poss -= len(pc[0])
            return -1
        if cd[0] in pc[0]:
            return cd[0]
        poss -= len(pc[0])
        return -1
    cpc = countpos(pc)
    if cpc == 0:
        return -1
    if len(rs) == 0:
        if cpc >1:
            poss -= cpc
            return -1
        return tonumber(pc)
    for j in pc[0]:
        npc = pc[1:]
        nrs = []
        for r in rs:
            if r[0][0] != j:
                nrs.append([r[0][1:],r[1]])
            else:
                nrc = r[1] -1
                if nrc > 0:
                    nrs.append([r[0][1:],nrc])
                else:
                    for k in range(len(r[0])-1):
                        npc[k]=pc[k+1][:]
                        if  r[0][k+1] in npc[k]:
                            npc[k].pop(npc[k].index(r[0][k+1]))
        result = guessone(npc,nrs)
        if result > 0:
            return j*(10**(len(pc)-1))+result
    return -1

def tonumber(pc):
    r = 0
    for j in pc:
        r = r*10+j
    return r

def totime(t):
    s = ""
    t = round(t)
    s = s+str(t%60)+"s"
    t = t//60
    s = str(t%60)+"m"+s
    t = t//60
    s = str(t%24)+"h"+s
    t = t//24
    s = str(t%365)+"d"+s
    t = t//365
    s = str(t)+"y"+s
    return s
            
print(guessone(posc,sortedrules))

     
print("time:",time.time()-t1)

# ------------------------------decipher7----------------------------------
'''



'''
#==========================another try=========================================
test = []
for i in range(N):
    t = []
    for j in range(10):
        t.append(j)
    test.append(t)

nr = []
for i in range(4):
    for j in rules:
        if j[1] == i:
            nr.append(j)

rules = nr[:]

rulec = []
for i in rules:
    c = []
    if i[1] == 0:
        t = []
        for j in range(N):
            tt = []
            for k in range(10):
                if k != i[0][j]:
                    tt.append(k)
            t.append(tt)
        c.append(t)
    if i[1] == 1:
        for l in range(N):
            t = []
            for j in range(N):
                tt = []
                if l == j:
                    tt.append(i[0][j])
                else:
                    for k in range(10):
                        if k != i[0][j]:
                            tt.append(k)
                t.append(tt)
            c.append(t)
    if i[1] == 2:
        for l in range(N-1):
            for m in range(l+1,N):
                t = []
                for j in range(N):
                    tt = []
                    if l == j or m == j:
                        tt.append(i[0][j])
                    else:
                        for k in range(10):
                            if k != i[0][j]:
                                tt.append(k)
                    t.append(tt)
                c.append(t)
    if i[1] == 3:
        for l in range(N-2):
            for m in range(l+1,N-1):
                for o in range(m+1,N):
                    t = []
                    for j in range(N):
                        tt = []
                        if l == j or m == j or o == j:
                            tt.append(i[0][j])
                        else:
                            for k in range(10):
                                if k != i[0][j]:
                                    tt.append(k)
                        t.append(tt)
                    c.append(t)         
    rulec.append(c)


def co(a,b):
    c = []
    for i in range(N):
        t = []
        for j in a[i]:
            for k in b[i]:
                if j == k:
                    t.append(j)
        if len(t) == 0:
            return []
        c.append(t)
    return c

def g(t,n):
    if n == len(rulec):
        if len(t) > 0:
            for i in t:
                if len(i) != 1:
                    return []
            return t
        return []
    for j in rulec[n]:
        nt = co(t,j)
        if len(nt)>0:
            r = g(nt,n+1)
            if len(r)>0:
                return r
    return []

def ton(t):
    r = 0
    for j in t:
        r = r*10+j[0]
    return r

print(ton(g(test,0)))

print("time:",time.time()-t1)  
'''
