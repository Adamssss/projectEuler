import time

t1 = time.time()

#calculate the numbers all in a ten digits array

# define an add of the two numbers
def add(a,b):
    c = [0,0,0,0,0,0,0,0,0,0]
    for i in range(0,10):
        c[i] = a[i]+b[i]+c[i]
        if c[i] > 9:
            c[i] -= 10
            if i != 9:
                c[i+1] += 1

    return c

# define to show the value of the digits array
def show(a):
    num = 0
    for i in range(0,10):
        num = num*10 + a[9-i]

    return num

# define power of
def power(x):
    result = [1,0,0,0,0,0,0,0,0,0]
    for i in range(0,x):
        for j in range(0,10):
            result[j] *= x
            
        for j in range(0,10):
            if result[j] > 9:
                if j != 9:
                    result[j+1] += result[j]//10
                result[j] = result[j]%10

    return result


N = 1000
total = [0,0,0,0,0,0,0,0,0,0]
for i in range(1,N+1):
    total = add(total,power(i))

print (show(total))

print("time:",time.time()-t1)
