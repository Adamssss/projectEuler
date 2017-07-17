import math
import time

t1 = time.time()

temp2 = [0]*100

def wiocb2(b):
    global temp2
    if 2 > b:
        return 0
    if 2 == b:
        return 1
    if temp2[b] > 0:
        return temp2[b]
    # starting with black block
    result = wiocb2(b-1)
    # starting with colored block
    result += wiocb2(b-2)+1
    temp2[b] = result
    return result

temp3 = [0]*100

def wiocb3(b):
    global temp3
    if 3 > b:
        return 0
    if 3 == b:
        return 1
    if temp3[b] > 0:
        return temp3[b]
    # starting with black block
    result = wiocb3(b-1)
    # starting with colored block
    result += wiocb3(b-3)+1
    temp3[b] = result
    return result

temp4 = [0]*100

def wiocb4(b):
    global temp4
    if 4 > b:
        return 0
    if 4 == b:
        return 1
    if temp4[b] > 0:
        return temp4[b]
    # starting with black block
    result = wiocb4(b-1)
    # starting with colored block
    result += wiocb4(b-4)+1
    temp4[b] = result
    return result

print(wiocb2(50)+wiocb3(50)+wiocb4(50))

print("time:",time.time()-t1)  


    
