import math
import time

t1 = time.time()

# read the base & exp into a list
f = open('pb099_base_exp.txt','r')

bae= f.read().split('\n')

f.close()

def tonumber(p):
    number = 0
    for i in range(0,len(p)):
        temp = ord(p[i])-48
        number = number*10 + temp
    return number

count = 0

def tobe(bae):
    global count
    count += 1
    p = bae.split(',')
    b = tonumber(p[0])
    e = tonumber(p[1])
    temp = [count,b,e,math.log10(b)*e]
    return temp

listbe = []
for i in range(0,len(bae)):
    listbe.append(tobe(bae[i]))

def quickSort(L, low, high):
    i = low 
    j = high
    if i >= j:
        return L
    key = L[i][:]
    while i < j:
        while i < j and L[j][3] >= key[3]:
            j = j-1                                                             
        L[i] = L[j][:]
        while i < j and L[i][3] <= key[3]:    
            i = i+1 
        L[j] = L[i][:]
    L[i] = key[:] 
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L

listbe = quickSort(listbe,0,len(listbe)-1)

print(listbe[-1][0])

print("time:",time.time()-t1)  


    
