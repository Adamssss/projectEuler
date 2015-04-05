import math
import time

t1 = time.time()

N = 50

# use vectors to test the right angle
def check(x1,y1,x2,y2):
    op = [x1,y1]
    oq = [x2,y2]
    pq = [x2-x1,y2-y1]
    if zerovector(op) or zerovector(oq) or zerovector(pq):
        return False
    # o is right angle
    if times(op,oq) == 0:
        return True
    # p is right angle
    if times(op,pq) == 0:
        return True
    # q is right angle
    if times(oq,pq) == 0:
        return True
    return False

def times(v1,v2):
    return v1[0]*v2[0]+v1[1]*v2[1]

def zerovector(v):
    return v[0] == 0 and v[1] == 0

count = 0

for x1 in range(0,N+1):
    for y1 in range(0,N+1):
        for x2 in range(0,N+1):
            for y2 in range(0,N+1):
                if check(x1,y1,x2,y2):
                    count += 1

#every triangle is counted twice
print(count//2)

print("time:",time.time()-t1)
    


    
