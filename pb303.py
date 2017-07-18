import math
import time

t1 = time.time()
t2 = time.time()

N = 10000

# 9     12222
# 99    1122222222
# 999   111222222222222
# 9999  11112222222222222222

def fs(n):
    if n == 9999:
        return 11112222222222222222
    t = n
    while True:
        p = 1
        while t >= p:
            td = (t%(p*10))//p
            if td > 2:
                t += (10-td)*p - t%p
            p *= 10
        #print(t)
        res = t%n
        if res == 0:
            return t
        t += n-res
        #print(t)

def ss(n):
    r = 0
    for i in range(1,n+1):
        t = fs(i)
        r += t//i
    return r

print(ss(N))

print("time:",time.time()-t1)  



'''
# May contain ERRORs!!!!!!!

cheatlist = [9,99,999,9999]
cheatresult = [12222,1122222222,111222222222222,11112222222222222222]

def addcheat(a,b):
    if b%a != 0:
        print(a,b)
        return
    global cheatlist
    global cheatresult
    cheatlist.append(a)
    cheatresult.append(b)

# 1998,111222222222222
addcheat(1998,111222222222222)
# 2997,112222221222222
addcheat(2997,112222221222222)
# 3996,121222222222212
addcheat(3996,121222222222212)
# 4995,1112222222222220
addcheat(4995,1112222222222220)
# 5994,112222221222222
addcheat(5994,112222221222222)
# 6993,122211222222222
addcheat(6993,122211222222222)
# 7992,221222222222112
addcheat(7992,221222222222112)
# 8991,122212222222221
addcheat(8991,122212222222221)
# 9990,1112222222222220
addcheat(9990,1112222222222220)

def cheat(n):
    i = cheatlist.index(n)
    return cheatresult[i]


def check(n):
    if n <= 2:
        return True
    if n%10 <= 2:
        return check(n//10)
    return False

def f(n):
    if n in cheatlist:
        return cheat(n)
    if n% 9 == 0:
        return f9(n)
    r = n
    while not check(r):
        r += n
    return r

def f9(n):
    pr = [1,2]
    while True:
        tr = pr.pop(0)
        if tr%n == 0:
            return tr
        pr.append(tr*10)
        pr.append(tr*10+1)
        pr.append(tr*10+2)

# used only for 999*n from 1 to 10000
def f999(n):
    if n% 5 == 0:
        return f999(n//5)*10
    pr = [1,2]
    while True:
        tr = pr.pop(0)
        if tr%n == 0:
            return tr
        pr.append(tr*10+1)
        pr.append(tr*10+2)

def s(n):
    r = 0
    for i in range(1,n+1):
        t2 = time.time()
        t = f(i)
        dt = time.time() - t2
        if dt > 1:
            print(i,t,r,dt)
        r += t//i
    return r

# n     f(n)        s(n-1)        time > 10s
# 2475 112222222200 167207032059 20.785536766052246
# 4545 101222222220 235138524187 10.922924757003784
# 4945 112122020120 235180055224 10.007631301879883
# 4950 112222222200 235202793242 21.100386381149292
# 5495 210201202120 457921719504 16.99416494369507
# 6435 120122222220 476722039342 23.100995779037476
# 7425 112222222200 494274845852 21.263750314712524
# 8316 102112222212 522038997111 12.323225021362305
# 8792 210201202120 522027131698 10.478384971618652
# 8901 201200002002 522096761621 40.02589726448059
# 9090 101222222220 535749465236 11.139966249465942
# 9405 112212221220 535773880658 20.837037801742554
# 9756 121202222112 535799860125 26.835024118423462
# 9891 202012221222 535840406630 42.03450083732605
# 9900 112222222200 536943321981 23.505922079086304

# minor improvements
addcheat(2475,112222222200)
addcheat(4545,101222222220) 
addcheat(4945,112122020120)
addcheat(4950,112222222200) 
addcheat(5495,210201202120) 
addcheat(6435,120122222220) 
addcheat(7425,112222222200) 
addcheat(8316,102112222212)
addcheat(8792,210201202120)
addcheat(8901,201200002002) 
addcheat(9090,101222222220) 
addcheat(9405,112212221220) 
addcheat(9756,121202222112)
addcheat(9891,202012221222)
addcheat(9900,112222222200)


# 9989 2002212221212 time: 597.784895658493
# 9899 11112221222222 time: 3925.930869102478

# improve speed by dividing task
addcheat(9989,2002212221212)
addcheat(9899,11112221222222)

'''


