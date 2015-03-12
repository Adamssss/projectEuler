import time

t1 = time.time()

#let 1-5 be the 5 inner position
#let 6-10 be the outer conresponding position
#use a [1,2,3,4,5,6,7,8,9,10] notation to mark one composition

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

# return the 5 sets
def sets(lst,n):
    result = []
    result.append(lst[n])
    result.append(lst[n+1])
    if n < 4:
        result.append(lst[n+6])
    else:
        result.insert(1,lst[0])
    return result

def isMagic(lst):
    total = sum(sets(lst,0))
    for i in range(1,5):
        if total!=sum(sets(lst,i)):
            return False
    return True

tp = QPL([1,2,3,4,5,6,7,8,9])

# add 10 to the string
# 10 has to be at an outer posotion

mp = []
for i in tp:
    for j in range(0,5):
        temp = i[:]
        temp.insert(5+j,10)
        if isMagic(temp):
            mp.append(temp)

# return the concatenated string
def valueOf(lst):
    smallest = 10
    si = 0
    for i in range(5,10):
        if lst[i] < smallest:
            si = i
            smallest = lst[i]
    
    temp = si%5
    q = []
    for i in range(0,5):
        temp -= 1
        if temp == -1:
            temp = 4
        q.append(temp)

    result = 0
    for i in q:
        s = sets(lst,i)
        a = s[2]
        if a == 10:
            result *= 10
        result = result*10+a
        b = s[1]
        result = result*10+b
        c = s[0]
        result = result*10+c

    return result

largest = 0
for i in mp:
    temp = valueOf(i)
    if temp > largest:
        largest = temp

print (largest)
                
print("time:",time.time()-t1)
                
