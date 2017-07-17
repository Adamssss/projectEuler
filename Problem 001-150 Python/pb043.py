import time

t1 = time.time()

def QPL(m_list):
    if len(m_list) == 1:
        return [m_list]
    qpl = []
    for i in m_list:
        rest = m_list[:]
        rest.remove(i)
        for j in QPL(rest):
            qpl.append([i]+j)
    return qpl

total = [0,0,0,0,0,0,0,0,0,0]

def satisfy(lst):
    temp = lst[5] + lst[7] - lst[6]
    if  temp != 0 and temp != 11:
        return False
    if lst[3]%2 != 0:
        return False
    temp = lst[2]+lst[3]+lst[4]
    if temp%3 != 0:
        return False
    temp = lst[6]*100+lst[7]*10+lst[8]
    if temp%13 > 0:
        return False
    temp = (temp%100)*10+lst[9]
    if temp%17 > 0:
        return False
    temp = lst[4]*100+lst[5]*10+lst[6]
    if temp%7 > 0:
        return False
    return True

def add(lsta,lstb):
    for i in range(10):
        lsta[i] += lstb[i]
    return lsta

def tonumber(lst):
    result = 0
    for i in range(10):
        result = result*10+lst[i]
    return result

for i in QPL([9,8,7,6,4,3,2,1,0]):
    i.insert(5,5)
    if satisfy(i):
        total = add(total,i)

for i in QPL([9,8,7,6,5,4,3,2,1]):
    i.insert(5,0)
    if satisfy(i):
        total = add(total,i)
        
print (tonumber(total))

print("time:",time.time()-t1)
