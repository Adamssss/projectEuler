import math

# n(3n-1)/2
N = 10000
pentagon = []
for i in range(0,N):
    pentagon.append(i*(3*i-1)//2)


def isPentagon(item):
    num = math.floor(math.sqrt(item*2//3))+1
    if num*(3*num-1)//2 == item:
        return True
    return False


lowest = N*N*2
for i in range(1,N-1):
    for j in range(i+1,N):
        if isPentagon(pentagon[i]+pentagon[j]):
            D = pentagon[j]-pentagon[i]
            if isPentagon(D):
                if D < lowest:
                    lowest = D

print (lowest)
