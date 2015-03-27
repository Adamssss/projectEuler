import math
import time

t1 = time.time()

M = [0]

# let a box a*b*c and M>=a>=b>=c
# the shortest would be sqrt(a^2+(b+c)^2)
def calcM(m):
    a = m
    count = 0
    i = 0
    while a-i > 0:
        b = a-i
        for c in range(1,b+1):
            length = math.sqrt(a*a+(b+c)*(b+c))
            if length == int(length):
                #print(a,b,c,length)
                count += 1
        i += 1
    return M[m-1]+count

i = 1
while True:
    temp = calcM(i)
    M.append(temp)
    if temp >= 1000000:
        print(i)
        break
    i += 1

print("time:",time.time()-t1)
# time: 786.4902520179749
