import math
import time

def init():
    global init_time
    init_time = time.time()

def timespent():
    print("time:",time.time()-init_time)

def numtodiglist(n):
    on = n
    if n <10:
        return [n]
    result = []
    while n > 0:
        result.insert(0,n%10)
        n = n//10
    #print("numtodiglist of ",on, " is ", result)
    return result

def possiblesplitsum(diglist):
    possiblesplit = [[diglist[0]]]
    for i in range(len(diglist)-1):
        npossiblesplit = []
        for j in possiblesplit:
            npossiblesplit.append(j[:]+[diglist[i+1]])
            npossiblesplit.append(j[:-1]+[j[-1]*10+diglist[i+1]])
        possiblesplit = npossiblesplit[:]
    result  = []
    #print("possiblesplitsum of ",diglist, " are ", possiblesplit)
    for i in possiblesplit[:-1]:
        result.append(sum(i))
    return result

def nsquareisSnumber(n):
    nsquare = n*n
    possiblesplitsumofn = possiblesplitsum(numtodiglist(nsquare))
    return n in possiblesplitsumofn


def T(n):
    S = 0
    for i in range(4,math.floor(math.sqrt(n))+1):
        if nsquareisSnumber(i):
            S = S+i*i
            print(i,i*i)
    return S

# split sum is equal to original number mod 9
# so the square of number must also equals to itself mod 9
# thus only 0, 1 would be possible
def T2(n):
    S = 0
    for i in range(9,math.floor(math.sqrt(n))+1,9):
        if nsquareisSnumber(i):
            S = S+i*i
        if nsquareisSnumber(i+1):
            S = S+(i+1)**2
    return S


# 10**4 41333
# 10**6 10804656
# 10**8 2818842841
# 10**10 499984803177
#print(T2(10**10))

def brutal():
    S = 0
    N = 10**5
    for j in range(10):
        for i in range(j*N+9-j,(j+1)*N,9):
            if nsquareisSnumber(i):
                S = S+i*i
                #print(i,i*i)
            if nsquareisSnumber(i+1):
                S = S+(i+1)**2
                #print(i+1,(i+1)**2)
        print(j,S)
        timespent()
    return S


    
def main():
    print("result: ",brutal())

if __name__ == '__main__':
    init()
    main()
    timespent()
