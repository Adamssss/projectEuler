import math
import time

t1 = time.time()

N = 100000000

def count(n):
    total = 0
    temp = [0]*n
    temp[0] = 1
    while keepgoing(temp):
        if reversible(temp):
            #print(temp)
            total += 2
        temp = increase(temp)
    return total

def keepgoing(lst):
    if lst[0] == 10:
        return False
    return True

def increase(lst):
    lst[-1] += 1
    return clean(lst)

def clean(lst):
    for i in range(len(lst)-1,0,-1):
        if lst[i] > 9:
            lst[i] -= 10
            lst[i-1] += 1
    return lst

def add(lst1,lst2):
    for i in range(len(lst1)):
        lst1[i] += lst2[i]
    return clean(lst1)

def addreverse(lst):
    temp = lst[:]
    for i in range(len(lst)):
        temp[i] += lst[-i-1]
    return clean(temp)

def reversible(lst):
    if lst[-1] < lst[0]:
        return False
    if (lst[-1]+lst[0])%2 == 0:
        return False
    temp = addreverse(lst)
    return isodd(temp)

def isodd(lst):
    for i in lst:
        if i%2 == 0:
            return False
    return True

def counttotal(num):
    n = int(math.log10(num))
    total = 0
    for i in range(1,n+1):
        total += count(i)
    return total
    
#print(counttotal(N))

R = [0]*10

# two side digits sum equals n have k solutions
# [9,8],[7,6],[5,4],[3,2]
# total 20
R[2] = 20
# with odd digits the mid one is always even
# so the side must be [11,8],[13,6],[15,4],[17,2]
# total 20
# the mid must be 0,1,2,3,4
# total 5
# 3 digit total 5*20 = 100
R[3] = 120
# abcd
# a+d must be odd
# b+c must not exceed 9
# b+c must be odd
# a+d  R[2] = 20
# b and c can be zero
# [9,10],[7,8],[5,6],[3,4],[1,2]
# total 30
# 4 digit total 20*30 = 600
R[4] = 720
# abcde
# a+e must be odd
# b+d must not exceed 10
# c+c is even busted
R[5] = 720
# abcdef
# a+f must be odd
# b+e must not exceed 9
# c+d must be odd
# a+f 20
# b+e 30
# c+d 30
# total 20*30*30 = 18000
R[6] = 18720
# abcdefg
# a+g must be odd
# b+f must not exceed 9
# c+e must be odd and over 10
# b+f must be even
# a+g must over 10
# a+g 20
# b+f [8,9],[6,7],[4,5],[2,3],[0,1] = 25
# c+e 20
# d 5
# total 20*25*20*5 = 50000
R[7] = 68720
# abcdefgh
# a+h must be odd
# b+g must not exceed 9
# c+f must be odd
# d+e must not exceed 9
# d+e must be odd
# c+f must not exceed 9
# b_g must be odd
# a+h must not exceed 9
# a+h 20
# b-g 30 30 30
# total = 20*30*30*30 = 540000
R[8] = 608720
# abcdefghi
# a+i must be odd
# b+h must not exceed 9
# c+g must be odd
# d+f must not exceed 9
# e+e is even busted
R[9] = 608720

print(R[9])  

print("time:",time.time()-t1)  


    
