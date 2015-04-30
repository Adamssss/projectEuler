import math
import time

t1 = time.time()

maxn = 1929394959697989990
minn = 1020304050607080900

mk = math.floor(math.sqrt(maxn)) # 1389026623
nk = math.ceil(math.sqrt(minn)) # 1010101011

# the first dig would be 1
# the last two has to be 0
# the number will be 1abcdefgh0
# h must be 3 or 7

s = nk//100
e = mk//100

def test(n):
    t = n*n
    t = t//100
    if t%10 != 8:
        return False
    t = t//100
    if t%10 != 7:
        return False
    t = t//100
    if t%10 != 6:
        return False
    t = t//100
    if t%10 != 5:
        return False
    t = t//100
    if t%10 != 4:
        return False
    t = t//100
    if t%10 != 3:
        return False
    t = t//100
    if t%10 != 2:
        return False
    return True
    
for i in range(s,e+1):
    temp = 10*i+3
    if test(temp):
        break
    temp = 10*i+7
    if test(temp):
        break

answer = temp*10
print(answer)

print("time:",time.time()-t1)  


    
