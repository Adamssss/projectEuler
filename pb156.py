import math
import time

t1 = time.time()

def cdtn(n,d):
    r = 0
    while n > 0:
        t = n%10
        if t == d:
            r += 1
        n = n//10
    return r

def cdan(n,d):
    r = 0
    t = n%10
    if t >= d:
        r += 1
    if n >= 10:
        p = n//10
        r += cdan(p-1,d)*10+p+(t+1)*cdtn(p,d)
    return r

def tos(n):
    vi = [0]*11
    for c in range(10):
        vi[c] = n%10
        n = n//10
    return vi

def todc(n):
    dc = [0]*10
    while n > 0:
        t = n%10
        dc[t] += 1
        n = n//10
    return dc

# used for test data
def temp(i,n):
    vi = tos(i)
    lc = [0]*10
    dc = todc(i)
    out = [0]*10
    for j in range(10):
        out[j] = []
    for j in range(1,10):
        lc[j] = cdan(i,j)
    total = [0]*10
    while True:
        i += 1
        dc[vi[0]] -= 1
        vi[0] += 1
        for j in range(len(vi)):
            if vi[j] > 9:
                vi[j] = 0
                dc[vi[j+1]] -= 1
                vi[j+1] += 1
            else:
                dc[vi[j]] += 1
                break
        #print(vi,dc)
        for j in range(1,10):
            lc[j] += dc[j]
            if i == lc[j]:
                total[j] += i
                out[j].append(i)
                print(i,lc[j],j,total[j],len(out[j]))
        if i >= n:
            print(lc)
            print(total)
            for j in range(1,10):
                print(len(out[j]),out[j])
            a = sum(total)
            print(a)
            return a
        
# f(10^10,2~9) = 10^10
# f(n*10^10,n) = n*10^10+1
tenn = 10**10
# s(1) = 22786974071
# 5 & 9 has only solution of 10^10
# 2~4 only appears between 1-10^9 & 10^10
# 6~8 only appears between 9*10^9-10^10

# get results from 2 to 4
def rttf():
    i = 0
    vi = [0]*10
    lc = [0]*5
    dc = [0]*10
    r = [0]*10
    c = [0]*10
    while True:
        i += 1
        dc[vi[0]] -= 1
        vi[0] += 1
        for j in range(len(vi)):
            if vi[j] > 9:
                vi[j] = 0
                dc[vi[j+1]] -= 1
                vi[j+1] += 1
            else:
                dc[vi[j]] += 1
                break
        for j in range(2,5):
            lc[j] += dc[j]
            if i == lc[j]:
                r[j] += i
                c[j] += 1
                #print(i,j,r[j],c[j])
        if i >= 600000000:
            return [r,c]

# get results from 6 to 8
def rste():
    i = 9400000000
    vi = tos(i)
    lc = [0]*10
    dc = todc(i)
    for j in range(6,9):
        lc[j] = cdan(i,j)
    r = [0]*10
    c = [0]*10
    while True:
        i += 1
        dc[vi[0]] -= 1
        vi[0] += 1
        for j in range(len(vi)):
            if vi[j] > 9:
                vi[j] = 0
                dc[vi[j+1]] -= 1
                vi[j+1] += 1
            else:
                dc[vi[j]] += 1
                break
        for j in range(6,9):
            lc[j] += dc[j]
            if i == lc[j]:
                r[j] += i
                c[j] += 1
                #print(i,j,r[j],c[j])
        if i >= tenn:
            return [r,c]

# sum of 1-10^10
s = [0]*10
c = [0]*10
rc = rttf()
for i in range(2,5):
    s[i] += rc[0][i]+tenn
    c[i] += rc[1][i]+1
s[5] += tenn
c[5] += 1
rc = rste()
for i in range(6,9):
    s[i] += rc[0][i]
    c[i] += rc[1][i]
s[9] += tenn
c[9] += 1
#print(s)
#print(c)

total = 0
total += 22786974071
for i in range(2,10):
    total += s[i]*i+c[i]*i*(i-1)//2*tenn-i*tenn

print(total)

print("time:",time.time()-t1)
# 21295121502550
# time: 2957.6570880413055

'''
The original test data
contains mistakes but is helpful for getting the final algorithm
N = 500000000
temp(40*N,50*N)

0 - N
[0, 1146663393, 805727654, 4215999875, 5499999885, 0, 0, 0, 0, 0]
42 [1, 199981, 199982, 199983, 199984, 199985, 199986, 199987, 199988, 199989, 199990, 200000, 200001, 1599981, 1599982, 1599983, 1599984, 1599985, 1599986, 1599987, 1599988, 1599989, 1599990, 2600000, 2600001, 13199998, 35000000, 35000001, 35199981, 35199982, 35199983, 35199984, 35199985, 35199986, 35199987, 35199988, 35199989, 35199990, 35200000, 35200001, 117463825, 500000000]
4 [28263827, 35000000, 242463827, 500000000]
11 [371599983, 371599984, 371599985, 371599986, 371599987, 371599988, 371599989, 371599990, 371599991, 371599992, 500000000]
11 [499999984, 499999985, 499999986, 499999987, 499999988, 499999989, 499999990, 499999991, 499999992, 499999993, 500000000]
0 []
0 []
0 []
0 []
0 []
11668390807
time: 1818.437008857727

N - 2N
[0, 20529199568, 1063263827, 0, 0, 0, 0, 0, 0, 0]
40 [500000001, 500199981, 500199982, 500199983, 500199984, 500199985, 500199986, 500199987, 500199988, 500199989, 500199990, 500200000, 500200001, 501599981, 501599982, 501599983, 501599984, 501599985, 501599986, 501599987, 501599988, 501599989, 501599990, 502600000, 502600001, 513199998, 535000000, 535000001, 535199981, 535199982, 535199983, 535199984, 535199985, 535199986, 535199987, 535199988, 535199989, 535199990, 535200000, 535200001]
2 [528263827, 535000000]
0 []
0 []
0 []
0 []
0 []
0 []
0 []
21592463395
time: 1673.2967081069946

2N - 4N
[0, 1111111110, 0, 0, 0, 0, 0, 0, 0, 0]
1 [1111111110]
0 []
0 []
0 []
0 []
0 []
0 []
0 []
0 []
1111111110
time: 3521.52130818367

4N - 10N
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
0 []
0 []
0 []
0 []
0 []
0 []
0 []
0 []
0 []
0
time: 10270.912463188171

10N - 20N
[0, 0, 10000000000, 10000000000, 10000000000, 10000000000, 115783999905, 68131008510, 419040935919, 10000000000]
0 []
1 [10000000000]
1 [10000000000]
1 [10000000000]
1 [10000000000]
12 [9500000000, 9628399986, 9628399987, 9628399988, 9628399989, 9628399990, 9628399991, 9628399992, 9628399993, 9628399994, 9628399995, 10000000000]
7 [9465000000, 9471736170, 9500000000, 9757536170, 9965000000, 9971736170, 10000000000]
43 [9465000000, 9486799989, 9486799990, 9486799991, 9486799992, 9486799993, 9486799994, 9486799995, 9486799996, 9486799997, 9497400000, 9498399989, 9498399990, 9498399991, 9498399992, 9498399993, 9498399994, 9498399995, 9498399996, 9498399997, 9500000000, 9882536171, 9965000000, 9986799989, 9986799990, 9986799991, 9986799992, 9986799993, 9986799994, 9986799995, 9986799996, 9986799997, 9997400000, 9998399989, 9998399990, 9998399991, 9998399992, 9998399993, 9998399994, 9998399995, 9998399996, 9998399997, 10000000000]
1 [10000000000]
652955944334
time: 17972.196951150894

20N - 30N
[0, 0, 61868991481, 114215999875, 115499999885, 0, 0, 0, 0, 0]
0 []
6 [10028263827, 10035000000, 10242463827, 10500000000, 10528263827, 10535000000]
11 [10371599983, 10371599984, 10371599985, 10371599986, 10371599987, 10371599988, 10371599989, 10371599990, 10371599991, 10371599992, 10500000000]
11 [10499999984, 10499999985, 10499999986, 10499999987, 10499999988, 10499999989, 10499999990, 10499999991, 10499999992, 10499999993, 10500000000]
0 []
0 []
0 []
0 []
0 []
291584991241
time: 17589.00478696823

30N - 40N
[0, 0, 20000000000, 20000000000, 20000000000, 20000000000, 235783999905, 138131008510, 849040935919, 20000000000]
0 []
1 [20000000000]
1 [20000000000]
1 [20000000000]
1 [20000000000]
12 [19500000000, 19628399986, 19628399987, 19628399988, 19628399989, 19628399990, 19628399991, 19628399992, 19628399993, 19628399994, 19628399995, 20000000000]
7 [19465000000, 19471736170, 19500000000, 19757536170, 19965000000, 19971736170, 20000000000]
43 [19465000000, 19486799989, 19486799990, 19486799991, 19486799992, 19486799993, 19486799994, 19486799995, 19486799996, 19486799997, 19497400000, 19498399989, 19498399990, 19498399991, 19498399992, 19498399993, 19498399994, 19498399995, 19498399996, 19498399997, 19500000000, 19882536171, 19965000000, 19986799989, 19986799990, 19986799991, 19986799992, 19986799993, 19986799994, 19986799995, 19986799996, 19986799997, 19997400000, 19998399989, 19998399990, 19998399991, 19998399992, 19998399993, 19998399994, 19998399995, 19998399996, 19998399997, 20000000000]
1 [20000000000]
1322955944334
time: 18975.398368120193

40N - 50N
[0, 0, 0, 224215999875, 225499999885, 0, 0, 0, 0, 0]
0 []
0 []
11 [20371599983, 20371599984, 20371599985, 20371599986, 20371599987, 20371599988, 20371599989, 20371599990, 20371599991, 20371599992, 20500000000]
11 [20499999984, 20499999985, 20499999986, 20499999987, 20499999988, 20499999989, 20499999990, 20499999991, 20499999992, 20499999993, 20500000000]
0 []
0 []
0 []
0 []
0 []
449715999760
time: 17527.144902944565
'''
    