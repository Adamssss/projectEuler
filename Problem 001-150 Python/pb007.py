import time

t1 = time.time()

prime = [2,3]
total = 5
l = 2

while True:
    b = prime[-1]

    
    while True:
        b = b+2
        i = 0
        t = True
        while (prime[i]*prime[i] < b):
            i=i+1
            if (b%prime[i] == 0):
                t = False
                break
                
        if t:
            prime.append(b)
            l += 1
            break
        
    if l == 10001:
        break


print (b)

print("time:",time.time()-t1)
                
