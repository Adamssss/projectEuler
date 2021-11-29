import math
import time

def init():
    global init_time
    init_time = time.time()

def palindromictuple(n):
    if n == 1:
        return [[1]]
    if n == 2:
        return [[2],[1,1]]
    if n%2 == 1:
        result = [[n]]
        for i in range(n//2,0,-1):
            for j in palindromictuple(n-i*2):
                result.append([i]+j+[i])
        return result
    else:
        result = [[n],[n//2,n//2]]
        for i in range(n//2-1,0,-1):
            for j in palindromictuple(n-i*2):
                result.append([i]+j+[i])
        return result

def palindromictuplecount(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n%2 == 1:
        result = 1
        for i in range(n//2,0,-1):
            result = result + palindromictuplecount(n-i*2)
        return result
    else:
        result = 2
        for i in range(n//2-1,0,-1):
            result = result + palindromictuplecount(n-i*2)
        return result

def t(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n%2 == 1:
        result = 0
        for i in range(n//2,0,-1):
            if i == 2:
                result = result + palindromictuplecount(n-i*2)
            else:
                result = result + t(n-i*2)
        return result
    else:
        result = 0
        if n ==4:
            result = 1
        for i in range(n//2-1,0,-1):
            if i == 2:
                result = result + palindromictuplecount(n-i*2)
            else:
                result = result + t(n-i*2)
        return result
        
# dynamic programming
# at n =    [0,1,2,3,4,5,6,7,8,9]
# ptclist = [0,1,2,2,4,4,8,8,16,16, ...]
# tlist =   [0,0,1,0,2,1,4,3,9,7, ...]

# ptc(odd n) = 1+ptc(n-2)+ptc(n-4)+ptc(n-6)+...+ptc(3)+ptc(1) -> 2**(n//2)
# ptc(even n) = 2+ptc(n-2)+ptc(n-4)+ptc(n-6)+...+ptc(4)+ptc(2) -> 2**(n//2)

# t(odd n) = t(n-2)+ptc(n-4)+t(n-6)+t(n-8)+...+t(3)+t(1)
# t(even n) = t(n-2)+ptc(n-4)+t(n-6)+t(n-8)+...+(4)+t(2)

tlist = []
sumtlist = []
def tdp(n):
    global tlist, sumtlist
    # n = 0~7
    tlist=[0,0,1,0,2,1,4,3]
    sumtlist=[0,0,1,0,3,1,7,4]
    for i in range(8,n+1,2):
        ptci = 2**(i//2-2)
        tlist.append(tlist[i-2]+ptci+sumtlist[i-6])
        sumtlist.append(tlist[-1]+sumtlist[i-2])
        tlist.append(tlist[i-1]+ptci+sumtlist[i-5])
        sumtlist.append(tlist[-1]+sumtlist[i-1])


def test():
    for i in range(1,10):
        print(i,palindromictuplecount(i),t(i),palindromictuple(i))
    for i in range(10,20):
        print(i,palindromictuplecount(i),t(i))
    print(t(20))
    print(t(42))
    tdp(42)
    print(tlist)

#test()

def solve():
    N = 10**6
    global tlist, sumtlist
    # n = 0~7
    tlist=[0,0,1,0,2,1,4,3]
    sumtlist=[0,0,1,0,3,1,7,4]
    i = 8
    result = i
    ptci = 2
    while True:
        ptci = (ptci*2)%N
        result = i
        ti = (tlist[i-2]+ptci+sumtlist[i-6])%N
        tlist.append(ti)
        sumtlist.append((ti+sumtlist[i-2])%N)
        if ti == 0:
            break
        result = i + 1
        ti = (tlist[i-1]+ptci+sumtlist[i-5])%N
        tlist.append(ti)
        sumtlist.append((ti+sumtlist[i-1])%N)
        if ti == 0:
            break
        i = i +2
    return result

def timespent():
    print("time:",time.time()-init_time)


def main():
    result = solve()
    print("result:", result)


if __name__ == '__main__':
    init()
    main()
    timespent()
