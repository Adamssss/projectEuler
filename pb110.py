import math
import time

t1 = time.time()

#1/x+1/y = n
# y >= x
# x > n
# x <= 2n
# y = nx/(x-n)

def nds(n):
    count = 0
    for x in range(n+1,2*n+1):
        y = n*x/(x-n)
        if y == int(y):
            count += 1
    return count

prime = []

def primeSieve(n):
    global prime
    n = (n+1)//2
    p = [True]*(n)
    i = 1
    prime.append(2)
    while i < n:
        if p[i]:
            t = 2*i+1
            prime.append(t)
            j = i
            while j < n:
                p[j] = False
                j += t
        i += 1
    return prime

# it seems that dns is related to factor numbers
def factors(number):
    factx = 1
    i = 0
    count = 0
    nr = math.floor(math.sqrt(number))
    while prime[i] <= nr:
        while(number%prime[i] == 0):
            count=count+1
            number = number / prime[i]
        nr = math.floor(math.sqrt(number))
            
        if count > 0:
            factx *= (count+1)
            count = 0
            
        i = i+1
    if number > 1:
        factx *= 2
    return factx

'''
# test the theory
primeSieve(1000+50)
for i in range(10,1000):
    if nds(i)-(factors(i*i)+1)//2 != 0:
        print('error')
'''

def quickSort(L, low, high):
    i = low 
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1                                                             
        L[i] = L[j]
        while i < j and L[i] <= key:    
            i = i+1 
        L[j] = L[i]
    L[i] = key 
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L

# so nds(i)*2 = factors(i^2)+1
# factors(i^2) > 1999
# i must contain many factors and better be small

# let f be the factor
# let fi be the factors increased

# for 2 f = 2 fi = 3 (squared)
# for 3 f = 3 fi = 3
# for 4 which is 2^2 f = 2 fi = 5/3
# for 8 f = 2 fi = 7/5
# for 9 f = 3 fi = 5/3

# coe would be estabiled to represent the ratio between f and fi
# coe(2) = 2/3
# coe(3) = 1
# coe(4) = 6/5
# coe(5) = 5/3
# coe(7) = 7/3
# coe(8) = 10/7
# coe(9) = 9/5
# the smaller the better

N = 10000
ex = 4000000

primeSieve(N+50)
'''
last = 0
for i in range(2,N+1):
    temp = (factors(i*i)+1)//2
    if temp > last:
        print(i,temp)
        last = temp
'''

# factor limit estimation
lt = math.floor(math.sqrt(N))
# the list of coe
coe = []
i = 0
while prime[i] < lt:
    t = prime[i]
    j = 1
    fi = 2*j+1
    coe.append([math.log(t,2),t,fi])
    n = t*t
    while n < lt:
        j += 1
        fi = (2*j+1)/(2*j-1)
        coe.append([math.log(t,(j+1)/j),t,fi])
        n *= t
    i += 1

coe = quickSort(coe,0,len(coe)-1)

ss = 1
fs = 1
# use rs to keep record of the element used
rs = []

for i in coe:
    #print(i)
    ss *= i[1]
    fs *= i[2]
    ndss = int((fs+1)/2)
    rs.append([i[2],i[1]][:])
    #print(ss,ndss)
    if ndss > ex:
        mark = coe.index(i)
        break

rs = quickSort(rs,0,len(rs)-1)

# get rid of the most useless elements
for i in rs:
    fs = ndss*2-1
    fs = fs/i[0]
    ndss = int((fs+1)/2)
    if ndss > ex:
        ss = ss//i[1]
    else:
        print(ss)
        break
        
print("time:",time.time()-t1)  


    
