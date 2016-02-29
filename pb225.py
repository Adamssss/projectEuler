import math
import time

t1 = time.time()

def test(n):
    a = 1
    b = 1
    c = 1
    i = 0
    while True:
        i += 1
        d = (a+b+c)%n
        if d == 0:
            #print(n,i)
            return False
        a = b
        b = c
        c = d
        if a == 1 and b ==  1 and c == 1:
            #print(n,'infinite')
            return True

lst = []
count = 0
i = 3
while True:
    if i > 100000000:
        break
    i += 2
    if test(i):
        lst.append(i)
        count+=1
    if count == 124:
        print(i)
        #print(lst)
        break

print("time:",time.time()-t1)  


    
