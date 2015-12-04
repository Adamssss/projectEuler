import math
import time

t1 = time.time()

N =80
# target = 0.5

# 1,2 -> X
# 1,2,3 -> 1+2+3=7
# 1,2,3,4 -> 3+4=10, 1+3+4=26
# 1,2,3,4,5 -> 1+4+5=21, 2+3+5=76
# p = 2,3,5,7,11,13,
'''
N = 35
plst = [2,3,4,5,6,7,8,9,10,12,14,15,18,20,21,24,25,28,30,35]
lcm = 12600
'''
'''
N = 45
plst = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,20,21,22,24,25,28,30,33,35,36,39,40,42,44,45]
lcm = 1801800
'''

# first try log:154 time:11669.037102937698
# used:2,3,4,5,6,7,8,9,10,12,14,15,18,20,21,24,28,30,35,36,40,42,45,56,60,63,70,72
# 13+39+52 = 12
# 11,16,25,27,49 not possible

N = 80
plst = [2,3,4,5,6,7,8,9,10,12,13,14,15,18,20,21,24,28,30,35,36,39,40,42,45,52,56,60,63,70,72]
lcm = 32760
        
def inversessum(lst,lcm):
    r = 0
    for i in lst:
        r += lcm//i//i
    return r

tlcm = lcm*lcm
target = tlcm//2

total = inversessum(plst,tlcm)
#print(target,tlcm,total,total/tlcm)
L = len(plst)-1

Solution = []

def dfs(sn,r,ps,tsol):
    #print(sn,r,ps)
    if  r == 0:
        #print(tsol,"time:",time.time()-t1)  
        Solution.append(tsol)
        return tsol
    inv = tlcm//(plst[sn]*plst[sn])
    ps -= inv
    if sn < L and ps >= r:
        dfs(sn+1,r,ps,tsol)
    r -= inv
    if r == 0:
        #print(tsol+[plst[sn]],"time:",time.time()-t1)  
        Solution.append(tsol+[plst[sn]])
        return tsol
    if sn == L:
        return
    nn = math.ceil(math.sqrt(tlcm/r))
    nsn = sn + 1
    while nsn < L:
        if plst[nsn] >= nn:
            break
        nsn += 1
    dfs(nsn,r,ps,tsol+[plst[sn]])

dfs(0,target,total,[])
#print(Solution)
print(len(Solution))

print("time:",time.time()-t1)  


    
