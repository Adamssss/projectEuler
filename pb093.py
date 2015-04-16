import math
import time

t1 = time.time()

def pa(a,b,c,d):
    results = []
    # +++
    temp = a+b+c+d
    results.append(temp)
    # ++-
    temp = a+b+c-d
    results.append(temp)
    # ++*
    temp = a+b+c*d
    results.append(temp)
    temp = a+(b+c)*d
    results.append(temp)
    temp = (a+b+c)*d
    results.append(temp)
    # ++/
    temp = a+b+c/d
    if temp == int(temp):
        results.append(temp)
    temp = a+(b+c)/d
    if temp == int(temp):
        results.append(temp)
    temp = (a+b+c)/d
    if temp == int(temp):
        results.append(temp)
    # +-+
    temp = a+b-(c+d)
    results.append(temp)
    # +-*
    temp = a+b-c*d
    if temp > 0:
        results.append(temp)
    temp = a+(b-c)*d
    if temp > 0:
        results.append(temp)
    temp = (a+b-c)*d
    if temp > 0:
        results.append(temp)
    # +-/
    temp = a+b-c/d
    if temp == int(temp):
        results.append(temp)
    temp = a+(b-c)/d
    if temp == int(temp):
        results.append(temp)
    temp = (a+b+c)/d
    if temp == int(temp):
        results.append(temp)
    # +*+
    temp = (a+b)*(c+d)
    results.append(temp)
    # +*-
    temp = a+b*c-d
    results.append(temp)
    temp = (a+b)*c-d
    results.append(temp)
    temp = (a+b)*(c-d)
    results.append(temp)
    # +**
    temp = a+b*c*d
    results.append(temp)
    temp = (a+b)*c*d
    results.append(temp)
    # +*/
    temp = a+b*c/d
    if temp == int(temp):
        results.append(temp)
    temp = (a+b)*c/d
    if temp == int(temp):
        results.append(temp)
    # +/+
    temp = a+b/(c+d)
    if temp == int(temp):
        results.append(temp)
    temp = (a+b)/(c+d)
    if temp == int(temp):
        results.append(temp)
    # +/-
    temp = a+b/c-d
    if temp == int(temp):
        results.append(temp)
    temp = a+b/(c-d)
    if temp == int(temp):
        results.append(temp)
    temp = (a+b)/c-d
    if temp == int(temp):
        results.append(temp)
    temp = (a+b)/(c+d)
    if temp == int(temp):
        results.append(temp)
    # +/*
    temp = (a+b/c)*d
    if temp == int(temp):
        results.append(temp)
    # +//
    temp = a+b/c/d
    if temp == int(temp):
        results.append(temp)
    temp = (a+b)/c/d
    if temp == int(temp):
        results.append(temp)
    # -++
    temp = a-(b+c+d)
    if temp > 0:
        results.append(temp)
    # -+*
    temp = a-(b+c)*d
    if temp > 0:
        results.append(temp)
    # -+/
    temp = a-(b+c)/d
    if temp == int(temp):
        results.append(temp)
    # --*
    temp = a-b-c*d
    if temp > 0:
        results.append(temp)
    temp = (a-b-c)*d
    if temp > 0:
        results.append(temp)
    # --/
    temp = a-b-c/d
    if temp == int(temp):
        results.append(temp)
    temp = (a-b-c)/d
    if temp == int(temp):
        results.append(temp)
    # -*-
    temp = (a-b)*(c-d)
    if temp > 0:
        results.append(temp)
    temp = (a-b)*c-d
    results.append(temp)
    # -**
    temp = a-b*c*d
    if temp > 0:
        results.append(temp)
    # -*/
    temp = a-b*c/d
    if temp == int(temp):
        results.append(temp)
    # -/+
    temp = (a-b)/(c+d)
    if temp == int(temp):
        results.append(temp)
    # -//
    temp = a-b/c/d
    if temp == int(temp):
        results.append(temp)
    temp = (a-b)/c/d
    if temp == int(temp):
        results.append(temp)
    # *+*
    temp = a*b+c*d
    results.append(temp)
    temp = a*(b+c*d)
    results.append(temp)
    # *+/
    temp = a*b+c/d
    if temp == int(temp):
        results.append(temp)
    temp = (a*b+c)/d
    if temp == int(temp):
        results.append(temp)
    # *--
    temp = a*b-c-d
    results.append(temp)
    # *-*
    temp = a*b-c*d
    results.append(temp)
    temp = a*(b-c)*d
    results.append(temp)
    # *-/
    temp = a*b-c/d
    if temp == int(temp):
        results.append(temp)
    temp = a*(b-c)/d
    if temp == int(temp):
        results.append(temp)
    temp = a*(b-c/d)
    if temp == int(temp):
        results.append(temp)
    temp = (a*b-c)/d
    if temp == int(temp):
        results.append(temp)
    # **-
    temp = a*b*c-d
    results.append(temp)
    temp = a*(b*c-d)
    results.append(temp)
    # ***
    temp = a*b*c*d
    results.append(temp)
    # **/
    temp = a*b*c/d
    if temp == int(temp):
        results.append(temp)
    # */+
    temp = a*b/(c+d)
    if temp == int(temp):
        results.append(temp)
    # */-
    temp = a*b/(c-d)
    if temp == int(temp):
        results.append(temp)
    # *//
    temp = a*b/c/d
    if temp == int(temp):
        results.append(temp)
    # /+/
    temp = a/b+c/d
    if temp == int(temp):
        results.append(temp)
    temp = a/(b+c)/d
    if temp == int(temp):
        results.append(temp)
    # /-*
    temp = a/b-c*d
    if temp == int(temp):
        results.append(temp)
    # /-/
    temp = a/b-c/d
    if temp == int(temp):
        results.append(temp)
    temp = a/(b-c)/d
    if temp == int(temp):
        results.append(temp)
    # /*-
    temp = a*b/c-d
    if temp == int(temp):
        results.append(temp)
    # //-
    temp = a/b/c-d
    if temp == int(temp):
        results.append(temp)
    # ///
    temp = a/b/c/d
    if temp == int(temp):
        results.append(temp)

    return results

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

def possible(a,b,c,d):
    result = []
    for i in QPL([a,b,c,d]):
        for j in pa(i[0],i[1],i[2],i[3]):
            if j > 0 and not j in result:
                result.append(int(j))
    result = quickSort(result,0,len(result)-1)
    return result

def lgp(a,b,c,d):
    i = 0
    temp = possible(a,b,c,d)
    while True:
        i += 1
        if not temp[i-1] == i:
            break
    return i-1

lgt = 0

for a in range(1,7):
    for b in range(a+1,8):
        for c in range(b+1,9):
            for d in range(c+1,10):
                temp = lgp(a,b,c,d)
                if temp > lgt:
                    lgt = temp
                    answer = 1000*a+100*b+10*c+d

print(answer)    

print("time:",time.time()-t1)  


    
