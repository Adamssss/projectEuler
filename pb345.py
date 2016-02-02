import math
import time

t1 = time.time()

# N = 5 or 15
N = 15

grid = []
if N == 15:
    grid.append([7,53,183,439,863,497,383,563,79,973,287,63,343,169,583])
    grid.append([627,343,773,959,943,767,473,103,699,303,957,703,583,639,913])
    grid.append([447,283,463,29,23,487,463,993,119,883,327,493,423,159,743])
    grid.append([217,623,3,399,853,407,103,983,89,463,290,516,212,462,350])
    grid.append([960,376,682,962,300,780,486,502,912,800,250,346,172,812,350])
    grid.append([870,456,192,162,593,473,915,45,989,873,823,965,425,329,803])
    grid.append([973,965,905,919,133,673,665,235,509,613,673,815,165,992,326])
    grid.append([322,148,972,962,286,255,941,541,265,323,925,281,601,95,973])
    grid.append([445,721,11,525,473,65,511,164,138,672,18,428,154,448,848])
    grid.append([414,456,310,312,798,104,566,520,302,248,694,976,430,392,198])
    grid.append([184,829,373,181,631,101,969,613,840,740,778,458,284,760,390])
    grid.append([821,461,843,513,17,901,711,993,293,157,274,94,192,156,574])
    grid.append([34,124,4,878,450,476,712,914,838,669,875,299,823,329,699])
    grid.append([815,559,813,459,522,788,168,586,966,232,308,833,251,631,107])
    grid.append([813,883,451,509,615,77,281,613,459,205,380,274,302,35,805])

if N == 5:
    grid.append([7,53,183,439,863])
    grid.append([497,383,563,79,973])
    grid.append([287,63,343,169,583])
    grid.append([627,343,773,959,943])
    grid.append([767,473,103,699,303])

# hungarian method
def rowshrink(gd):
    size = len(gd)
    rm = []
    outr = []
    outc = []
    cr = 0
    for i in range(size):
        m = 0
        mj = 0
        for j in range(size):
            if gd[i][j] > m:
                m = gd[i][j]
                mj = j
        rm.append(mj)
    for j in range(size):
        if rm.count(j) == 1:
            i = rm.index(j)
            outr.append(i)
            outc.append(j)
            cr += gd[i][j]
    ngd = []
    for i in range(size):
        if i not in outr:
            nr = []
            for j in range(size):
                if j not in outc:
                    nr.append(gd[i][j])
            ngd.append(nr[:])
    showgrid(ngd)
    return cr + smallmatrixsum(ngd)

def showgrid(gd):
    for i in gd:
        s = ''
        for j in i:
            if j < 100:
                s += ' '
            if j < 10:
                s += ' '
            s += str(j)
            s += ', '
        print(s)


def QPL(mylist):
    if len(mylist) == 1:
        return [mylist]
    qpl = []
    for i in mylist:
        rest = mylist[:]
        rest.remove(i)
        for j in QPL(rest):
            qpl.append([i]+j)
    return qpl

def smallmatrixsum(gd):
    temp = []
    size = len(gd)
    for i in range(size):
        temp.append(i)
    r = 0
    for i in QPL(temp):
        t = 0
        for j in range(size):
            t += gd[j][i[j]]
        if t > r:
            r = t
    return r

print(rowshrink(grid))

print("time:",time.time()-t1)


