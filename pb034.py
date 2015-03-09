import time

t1 = time.time()

fac = [1,1]
for i in range(2,10):
    fac.append(fac[-1]*i)

#print (fac)

total = 0

# 2 digits
for i in range(1,5):
    for j in range(0,5):
        a = i*10 +j
        b = fac[i] + fac[j]
        if a-b == 0:
            #print (a)
            total += a

# 3 digits
for i in range(1,7):
    for j in range(0,7):
        for k in range(0,7):
            a = i*100+j*10+k
            b = fac[i] + fac[j] + fac[k]
            if a-b == 0:
                #print (a)
                total += a

# 4 digits
for i in range(1,8):
    for j in range(0,8):
        for k in range(0,8):
            for l in range(0,8):
                a = i*1000+j*100+k*10+l
                b = fac[i]+fac[j]+fac[k]+fac[l]
                if a-b == 0:
                    #print (a)
                    total += a

# 5 digits
for i in range(1,9):
    for j in range(0,9):
        for k in range(0,9):
            for l in range(0,9):
                for m in range(0,9):
                    a = i*10000+j*1000+k*100+l*10+m
                    b = fac[i]+fac[j]+fac[k]+fac[l]+fac[m]
                    if a-b == 0:
                        #print (a)
                        total += a

# 6 digits
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            for l in range(0,10):
                for m in range(0,10):
                    for n in range(0,10):
                        a = i*100000+j*10000+k*1000+l*100+m*10+n
                        b = fac[i]+fac[j]+fac[k]+fac[l]+fac[m]+fac[n]
                        if a-b == 0:
                            #print (a)
                            total += a

# 7 digits
for i in range(1,3):
    for j in range(8,10):
        for k in range(8,10):
            for l in range(8,10):
                for m in range(8,10):
                    for n in range(8,10):
                        for o in range(8,10):
                            a = i*1000000+j*100000+k*10000+l*1000+m*100+n*10+o
                            b = fac[i]+fac[j]+fac[k]+fac[l]+fac[m]+fac[n]+fac[o]
                            if a-b == 0:
                                #print (a)
                                total += a

print (total)

print("time:",time.time()-t1)

