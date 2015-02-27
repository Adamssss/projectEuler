
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
for i in QPL([9,8,7,6,5,4,3,2,1,0]):
    t = 1
    for j in range(1,8):
        if (i[j]*100+i[j+1]*10+i[j+2])%divider[j] > 0:
            t = 0

    if t == 1:
        num = 0
        for j in range(len(i)):
            num = num *10 + i[j]
        total += num
        
print (total)
