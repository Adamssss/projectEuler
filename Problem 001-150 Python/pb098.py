import math
import time

t1 = time.time()

# read the words into a list
f = open('pb098_words.txt','r')

words= f.read().split(',')

f.close()

for i in range(0,len(words)):
    words[i] = words[i][1:len(words[i])-1]

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

def tolist(word):
    temp = []
    for i in word:
        temp.append(i)
    temp = quickSort(temp,0,len(temp)-1)
    temp.append(word)
    return temp

wl = []
for i in words:
    wl.append(tolist(i))

wl = quickSort(wl,0,len(wl)-1)


last = wl[0]
pwl = []

for i in range(1,len(wl)):
    if last[0:-1] == wl[i][0:-1]:
        pwl.append([last,wl[i]])
    last = wl[i]

def toorder(wl):
    temp = []
    for i in range(0,len(wl)-1):
        t = wl[-1].index(wl[i])
        temp.append(t)
    return temp

def tonlist(num):
    temp = []
    while num > 0:
        temp.insert(0,num%10)
        num = num//10
    return temp

def tonum(nl):
    if nl[0] == 0:
        return 10
    temp = 0
    for i in range(0,len(nl)):
        temp = temp*10+nl[i]
    return temp        

def illegal(nl,wl):
    for i in range(0,len(nl)):
        if nl.count(nl[i]) > 1:
            if not wl.count(wl[i]) > 1:
                return True
    return False

def changepattern(num,pwl):
    nl = tonlist(num)
    if len(nl) != len(pwl[0])-1:
        return 0
    if illegal(nl,pwl[0]):
        return 0
    nnl = nl[:]
    for i in range(len(nl)):
        nnl[toorder(pwl[1])[i]] = nl[toorder(pwl[0])[i]]
    ns = tonum(nnl)
    if isSquare(ns):
        #print(num,ns,pwl[0][-1],pwl[1][-1])
        if num == ns:
            return 0
        if num > ns:
            return num
        return ns
    return 0
        
def isSquare(num):
    r = math.floor(math.sqrt(num))
    if r*r == num:
        return True
    return False    

def testsquare(pwl):
    dig = len(pwl[0])-1
    ll = math.floor(math.sqrt(math.pow(10,dig-1)))
    ul = math.floor(math.sqrt(math.pow(10,dig)))+1
    lg = 0
    for i in range(ll,ul):
        temp = changepattern(i*i,pwl)
        if temp > lg:
            lg = temp
    return lg

largest = 0

for j in pwl:
    temp = testsquare(j)
    if temp > largest:
        largest = temp

print(largest)

print("time:",time.time()-t1)
    
