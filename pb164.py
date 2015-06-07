import math
import time

t1 = time.time()

def getrq(d):
    if d == 1:
        result = []
        for i in range(1,10):
            result.append([i])
        return result
    if d == 2:
        result = []
        for i in getrq(1):
            s = i[0]
            for j in range(10):
                if j+s <= 9:
                    result.append(i+[j])
        return result
    result = []
    for i in getrq(d-1):
        s = i[-1]+i[-2]
        for j in range(10):
            if j+s <= 9:
                result.append(i+[j])
    return result

def tdset(d):
    temp = [0]*1000
    if d == 1:
        for i in range(1,10):
            temp[i] += 1
        return temp
    if d == 2:
        for i in range(1,10):
            for j in range(10):
                if i+j <= 9:
                    temp[i*10+j] += 1
        return temp
    if d == 3:
        for i in range(1,10):
            for j in range(10):
                for k in range(10):
                    if i+j+k <= 9:
                        temp[i*100+j*10+k] += 1
        return temp
    lset = tdset(d-1)
    for i in range(1000):
        if lset[i] > 0:
            r = i%100
            s = r%10+r//10
            for j in range(10):
                if s+j <= 9:
                    temp[r*10+j] += lset[i]
    return temp    

# 1     9       
# 2     45      
# 3     165     
# 4     990     
# 5     5445    
# 6     27588   
# 7     146586  
# 8     783057

#print(len(getrq(8)))
print(sum(tdset(20)))

print("time:",time.time()-t1)  


    
