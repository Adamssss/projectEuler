import time

t1 = time.time()

# code QPL generator copied from pb 41
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

divider = [1,2,3,5,7,11,13,17]
total = 0

def addif(lst):
    if lst[3]%2 != 0:
        return 0
    for j in range(2,8):
        if (lst[j]*100+lst[j+1]*10+lst[j+2])%divider[j] > 0:
            return 0
    num = 0
    for j in range(len(i)):
        num = num *10 + lst[j]
    return num
    
for i in QPL([9,8,7,6,5,4,3,2,1,0]):
    total += addif(i)
        
print (total)

print("time:",time.time()-t1)
