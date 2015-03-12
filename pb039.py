import time

t1 = time.time()

# a <= b <= c
# a <= p/3
# b <= p/2

# a^2+b^2 = (p-a-b)^2
#0=p^2+2ab-2ap-2bp
#b = p^2-2ap/2p-2a

#for each set of a & p
# at most one b can be found

largest = 0
largestp = 0
for p in range(12,1001,2):
    count = 0
    for i in range(1,p//3):
        n = p*p-2*i*p
        d = 2*p-2*i
        if n%d == 0:
            count += 1
    
    if count > largest:
        largest = count
        largestp = p

print (largestp)

print("time:",time.time()-t1)
