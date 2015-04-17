import math
import time

t1 = time.time()

# lower bound of 1/3
def lb(num):
    return math.floor(num/3)+1

# upper bound of 3/7
def ub(num):
    return math.ceil(num/2)-1

# highest common factor
def gcd(x,y):
    if x < y:
        temp = x
        x = y
        y = temp
    while y > 0:
        temp = x%y
        x = y
        y = temp

    return x

# return the number of fractions
def nof(num):
    count = 0
    for i in range(lb(num),ub(num)+1):
        if gcd(i,num) == 1:
            #print(i,num)
            count += 1
    return count

total = 0
for i in range(2,12001):
    total += nof(i)

print(total)

print("time:",time.time()-t1)
                
