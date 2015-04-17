import time

t1 = time.time()

def times(x,b):
    result = x[:]
    for i in range(0,len(x)):
        result[i] = x[i]*b

    for i in range(0,len(result)-1):
        if result[i] > 9:
            result[i+1] += result[i]//10
            result[i] = result[i]%10

    while result[-1] > 9:
        result.append(result[-1]//10)
        result[-2] = result[-2]%10
    
    return result

# leave x = [1] 
def power(x,a,b):
    if b == 1:
        return times(x,a)
    return power(times(x,a),a,b-1)

def sumOf(x):
    total = 0
    for i in range(0,len(x)):
        total += x[i]
    return total

largest = 0
for i in range(1,100):
    for j in range(1,100):
        n = sumOf(power([1],i,j))
        if n > largest:
            largest = n

print (largest)

print("time:",time.time()-t1)
