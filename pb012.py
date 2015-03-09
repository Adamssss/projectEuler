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
        
    if b > 15000:
        break

# to find out how many divisors
def dvsr(number):
    dvsrs = 1
    i = 0
    count = 0
    while number >1:
        while(number%prime[i] == 0):
            count=count+1
            number = number // prime[i]
            
        if count > 0:
            dvsrs = dvsrs * (count +1)
            count = 0
            
        i = i+1

    return dvsrs


# main program

triangle = 2
triangleNumber = 1
while True:
    triangleNumber += triangle  

    if dvsr(triangleNumber)> 500:
        print (triangleNumber)
        break
    
    triangle = triangle + 1
    
print("time:",time.time()-t1) 
    
        

            
