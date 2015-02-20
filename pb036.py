def binary(x):
    b = []
    while x > 0:
        if x%2 == 0:
            b.append(0)
        if x%2 == 1:
            b.append(1)
        x = x//2
    length = len(b)//2
    if length == 0:
        return True
    temp = True
    i = 0
    while temp and i < length:
        if not b[i] == b[len(b)-1-i]:
            temp = False
        i += 1
    return temp

def decimal(x):
    d = []
    while x > 0:
        d.append(x%10)
        x = x//10
    length = len(d)//2
    if length == 0:
        return True
    temp = True
    i = 0
    while temp and i < length:
        if not d[i] == d[len(d)-1-i]:
            temp = False
        i += 1
    return temp

total = 0
for i in range(1,1000000):
    if binary(i) and decimal(i):
        total += i

print (total)
