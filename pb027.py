prime = [2,3,5]
primen = 2

while prime[primen] < 10000:
    b = prime[primen]
    t = 1
    while (t == 1):
        b = b+2
        i = 0
        t = 0
        while (prime[i]*prime[i] < b)and (t == 0):
            i=i+1
            if (b%prime[i] == 0):
                t = 1

                
        if (t == 0):
            primen += 1
            prime.append(b)


# a[167] is 997 < 1000
# when n = 0 num = n^2+an+b =b
# so b must be a prime
# when n = b num = n^2+an+b = b(b+a+1)
# so the max is restricted by b

coe = []
for i in range(-999,1000):
    coe.append([i,2])
    
# if b is odd then a has to be odd
# for 1+a+b to be a prime
t = -999
while t < 1000:
    for i in range(1,168):
        coe.append([t,prime[i]])
    t += 2

n = 1
while len(coe) > 1:

    # print (len(coe))
    
    i = 0
    while i < len(coe):
        a = coe[i][0]
        b = coe[i][1]
        num = (n*n+n*a+b) 
        if num in prime:
            i += 1
        else:
            coe.pop(i)

    n += 1

print(coe[0][0]*coe[0][1])     
