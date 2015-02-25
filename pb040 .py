import math

dig = []
dig.append([1,1])

for i in range(1,1000000):
    temp = dig[-1][:]
    l = math.floor(math.log10(temp[0])+1)
    if temp[1] < l :
        temp[1] += 1
    else:
        temp[0] += 1
        temp[1] = 1
    #print (temp)
    dig.append(temp)

def num(x):
    a = x[0]
    b = x[1]
    l = math.floor(math.log10(a)+1)
    a = a%pow(10,l+1-b)
    a = a//pow(10,l-b)
    return a

product = 1
for i in range(0,7):
    n = pow(10,i)
    product *= num(dig[n-1])

print (product)
