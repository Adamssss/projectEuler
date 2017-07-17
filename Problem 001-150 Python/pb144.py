import math
import time

t1 = time.time()

def getp(pa,pb):
    d1 = (pa[1]-pb[1])/(pa[0]-pb[0])
    d2 = 1/4/pb[0]*pb[1]
    #d3 = math.tan(math.atan(d2)*2-math.atan(d1))
    temp = 2*d2/(1-d2*d2)
    d3 = (temp-d1)/(1+temp*d1)
    b3 = pb[1]-pb[0]*d3
    # y = d3x+b3
    # 4x2+(d3x+b3)2 = 100
    # (4+d3^2)x2+2*d3*b3*x+b3^2-100 = 0
    xa = 4+d3*d3
    xb = 2*d3*b3
    # x1+x2 = -b/a
    pc = []
    pc.append(-xb/xa-pb[0])
    pc.append(pc[0]*d3+b3)
    return pc

p1 = [0,10.1]
p2 = [1.4,-9.6]

count = 1
while True:
    pn = getp(p1,p2)
    if pn[1] > 9.8 and pn[0] > -0.01 and pn[0] < 0.01:
        break
    count += 1
    p1 = p2
    p2 = pn

print(count) 

print("time:",time.time()-t1)  


    
