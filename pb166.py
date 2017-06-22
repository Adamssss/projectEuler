import math
import time

t1 = time.time()

gd = [0]*16

c = 0
for i in range(0,10):
    gd[0] = i
    for j in range(0,10):
        gd[1] = j
        for k in range(0,10):
            gd[2] = k
            for l in range(0,10):
                gd[3] = l
                sod = gd[0]+gd[1]+gd[2]+gd[3]
                for m in range(0,10):
                    gd[4] = m
                    for n in range(0,10):
                        gd[5] = n
                        for o in range(0,10):
                            gd[6] = o
                            gd[7] = sod-gd[4]-gd[5]-gd[6]
                            if gd[7] >= 0 and gd[7] < 10:
                                for p in range(0,10):
                                    gd[8] = p
                                    gd[12] = sod-gd[0]-gd[4]-gd[8]
                                    if gd[12] >= 0 and gd[12] < 10:
                                        gd[9] = sod-gd[3]-gd[6]-gd[12]
                                        if gd[9] >= 0 and gd[9] < 10:
                                            gd[13] = sod-gd[1]-gd[5]-gd[9]
                                            if gd[13] >= 0 and gd[13] < 10:
                                                for q in range(0,10):
                                                    gd[10] = q
                                                    gd[11] = sod-gd[8]-gd[9]-gd[10]
                                                    if gd[11] >= 0 and gd[11] < 10:
                                                        gd[14] = sod-gd[2]-gd[6]-gd[10]
                                                        if gd[14] >= 0 and gd[14] < 10:
                                                            gd[15] = sod-gd[3]-gd[7]-gd[11]
                                                            if gd[15] >= 0 and gd[15] < 10:
                                                                  if gd[0]+gd[5]+gd[10]+gd[15] == sod:
                                                                      if gd[12]+gd[13]+gd[14]+gd[15] == sod:
                                                                          c += 1

                                                                          

print(c)

print("time:",time.time()-t1)  


    
