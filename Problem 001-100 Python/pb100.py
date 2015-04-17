import math
import time

t1 = time.time()

# continued fraction of root2
# 3/2,7/5,17/12,41/29,99/70

# a+b=c
# a*(a-1)*2 = c*(c-1)
# c/a is close to root2

# generated c/a with brutalforce
# 21/15     =   3   *   7   /   5
# 120/85    =   5   *   24  /   17
# 697/493   =   17  *   41  /   29
# 4060/2871 =   29  *   140 /   99

# fraction of root 2: ta/tb
ta = [7]
tb = [5]

term = 1

a = [21]
c = [15]

last = 5

for i in range(0,20):
    term += 1
    tb.append(tb[-1]+ta[-1])
    ta.append(tb[-1]+tb[-2])
    if term%2 == 0:
        tempa = ta[-1]
        tempc = tb[-1]*2
    else:
        tempa = tb[-1]
        tempc = ta[-1]
    a.append(last*tempa)
    c.append(last*tempc)
    last = tempa

    if c[-1] > 1000000000000:
        print(a[-1])
        break

print("time:",time.time()-t1)  


    
