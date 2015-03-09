import time

t1 = time.time()

# a <= b <= c
# a <= p/3
# b <= p/2

largest = 0
largestp = 0
for p in range(12,1001):
    count = 0
    for i in range(1,p//3):
        for j in range(i,p//2):
            c = p-i-j
            if i*i+j*j-c*c == 0:
                count += 1
    
    if count > largest:
        largest = count
        largestp = p

print (largestp)

print("time:",time.time()-t1)
