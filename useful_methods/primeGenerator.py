import time

t1 = time.time()

# prime generator 4.1

prime = [2,3]
b = 3

while True:

    
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
        
    if b > 1000000:
        break



print (len(prime)-1)


print("time:",time.time()-t1)