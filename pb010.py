import time

t1 = time.time()


prime = [2,3]
total = 5

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
            break
        
    if b > 2000000:
        break

    total += b

print (total)

print("time:",time.time()-t1)
                
