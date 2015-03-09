import math
import time

t1 = time.time()

def downTo(origin):
    i = 2
    while i <= 10:
        t = math.log(origin[0],i)
        if int(t)-t== 0:
            origin[1] *= int(t)
            origin[0] = i
            break
        i += 1

    return origin

string = []
for i in range(2,101):
    for j in range(2,101):
        temp = [i,j]
        if not downTo(temp) in string:
            string.append(downTo(temp))

print (len(string))
            
print("time:",time.time()-t1)    
    

