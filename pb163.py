import math
import time

t1 = time.time()



# x,y,no
#       0
#   1,      2
#       3
# 4,    5,      6

        

    #               (0.5,sqrt(3)/2)
    #       (0.25,sqrt(3)/4)    (0.75,sqrt(3)/4)
    #               (0.5,sqrt(3)/6)
    # (0,0)             (0.5,0)         (1,0)

    # x = a*1/12, y = b*sqrt(3)/12
    # a,b:
    #           6,6
    #       3,3     9,3
    #           6,2
    # 0,0       6,0         12,0

    # triangle i (from 1 to n), j (from 1 to 2*i-1):

# T1
# 1(6)+2(3)+3(6)+6(1)
# T2
# 1(24)+2(12+6)+3(24)+4(12)+6(4+6)+8(3)+9(6)+12(6)+24(1)

def toxy(n):
    if n == 1:
        result = []
        result.append([6,6])
        result.append([3,3])
        result.append([9,3])
        result.append([6,2])
        result.append([0,0])
        result.append([6,0])
        result.append([12,0])
        return result
    result = toxy(n-1)
    x = (n-1)*6
    y = (n-1)*6
    result.append([x+6,y+6])
    result.append([x+3,y+3])
    result.append([x+9,y+3])
    result.append([x+6,y+2])
    result.append([x+6,y+0])
    result.append([x+12,y+0])
    for i in range(n-1):
        x = (n-1)*12-i*6
        y = i*6
        result.append([x+0,y+4])
        result.append([x+3,y+3])
        result.append([x+9,y+3])
        result.append([x+6,y+2])
        result.append([x+6,y+0])
        result.append([x+12,y+0])
    return result

def connected(a,b):
    axr = a[0] % 12
    ayr = a[1] % 12
    dx = b[0]-a[0]
    dy = b[1]-a[1]
    if (axr == 0 and ayr == 0) or (axr == 6 and ayr == 6):
        if dx == 0:
            return True
        if dy == 0:
            return True
        if dx == dy*3:
            return True
        if dx == dy:
            return True
        if dx == -3*dy:
            return True
        if dx == -dy:
            return True
        return False
    if (axr == 0 and ayr == 4) or (axr == 0 and ayr == 8) or (axr == 6 and ayr == 2) or (axr == 6 and ayr == 10):
        if dx == 0:
            return True
        if dx == dy*3:
            return True
        if dx == -3*dy:
            return True
        return False
    if (axr == 3 and ayr == 3) or (axr == 9 and ayr == 9):
        if dx == -3*dy:
            return True
        if dx == dy:
            return True
        return False
    if (axr == 6 and ayr == 0) or (axr == 0 and ayr == 6):
        if dy == 0:
            return True
        if dx == 0:
            return True
        return False
    if (axr == 3 and ayr == 9) or (axr == 9 and ayr == 3):
        if dx == -dy:
            return True
        if dx == 3*dy:
            return True
        return False
    return False

def notline(a,b,c):
    dxba = b[0]-a[0]
    dyba = b[1]-a[1]
    dxca = c[0]-a[0]
    dyca = c[1]-a[1]
    if dxba * dyca == dxca * dyba:
        return False
    return True
        
def T(n):
    count = 0
    nodes = toxy(n)
    #print(nodes)
    l = len(nodes)
    #print(l)
    for i in range(0,l-2):
        for j in range(i+1,l-1):
            if connected(nodes[i],nodes[j]):
                for k in range(j+1,l):
                    if connected(nodes[i],nodes[k]) and connected(nodes[k],nodes[j]) and notline(nodes[i],nodes[j],nodes[k]):
                        count = count + 1
                        #print( nodes[i],nodes[j],nodes[k])
    return count


print(T(36))

print("time:",time.time()-t1)  
#343047
#time: 515.099244594574

    
