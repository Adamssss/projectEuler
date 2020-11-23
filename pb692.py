import math
import time

def init():
    global init_time
    init_time = time.time()

def timespent():
    print("time:",time.time()-init_time)


def Hv1(N, c, lm):
    if lm==0 or 2*lm >= c:
        if c == 1:
            return 1
        for i in range(1,c+1):
            cr = Hv1(N,c-i,i)
            if cr < 0:
                return i
        return -1
    else:
        for i in range(1,2*lm+1):
            cr = Hv1(N,c-i,i)
            if cr < 0:
                return i
        return -1

#H(1)=1
#H(2)=2
#H(3)=3
#H(4)=1
def H(n):
    return Hv1(n,n,0)

def G(n):
    Gr = 0
    for i in range(1,n+1):
        Gr += H(i)
    return Gr

def test():
    for i in range(1,50):
        print(i,H(i))
    print(G(13))
    # the H(fb(i))=fb(i)

def Hmakearray(n):
    global Harray
    Harray = [0,1,2,3]
    for i in range(4,n+1):
        for j in range(1,i+1):
            if j == i:
                Harray.append(i)
                break
            if Harray[i-j]>2*j:
                Harray.append(j)
                break
    

def test2():
    Hmakearray(120)
    for i in range(120):
        print(i,Harray[i])

def fbmakearray(i):
    global FB
    FB = [0,1,1,2,3]
    for j in range(4,i):
        FB.append(FB[-1]+FB[-2])

def Hfb(n):
    for i in range(len(FB)-1,0,-1):
        if n == FB[i]:
            return n
        if n > FB[i]:
            return Hfb(n-FB[i])

def test3():
    N = 23416728348467685
    fbmakearray(80)
    #N=FB80
    print(FB[80])
    Hmakearray(120)
    for i in range(120):
        print(i,Harray[i],Hfb(i))

def Gfb(n):
    Gr = 0
    for i in range(1,n+1):
        Gr += Hfb(i)
    return Gr

def GtoFB(i):
    if i == 1:
        return 1
    if i == 2:
        return 1+2
    if i==3:
        return 1+2+3
    return GtoFB(i-1)+GtoFB(i-2)-FB[i-1]+FB[i+1]

def test4():
    fbi = 20
    fbmakearray(fbi)
    N = FB[-1]
    print(Gfb(N),N)
    print(GtoFB(fbi-1))

def GtoFBmakearray(i):
    GtoFBarray = [0,1,3,6]
    for j in range(4,i+1):
        Gtemp = GtoFBarray[j-1]+GtoFBarray[j-2]-FB[j-1]+FB[j+1]
        GtoFBarray.append(Gtemp)
    return GtoFBarray[-1]

def main():
    result = 0
    fbi = 80
    fbmakearray(fbi)
    N = FB[-1]
    #result = GtoFB(fbi-1)
    result = GtoFBmakearray(fbi-1)
    print("result:", result)


if __name__ == '__main__':
    init()
    main()
    #test4()
    timespent()
