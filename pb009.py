import time

t1 = time.time()

for a in range(1,334):
    for b in range(a,500):
        c = 1000-a-b
        dif = a*a +b*b -c*c
        if dif == 0:
            print (a*b*c)
            break
    if dif == 0:
        break

print("time:",time.time()-t1)
