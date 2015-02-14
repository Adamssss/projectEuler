# prime generator

# the number of the primes
N = 2000

a = [2,3,5]
n = 2

while n < N:
    b = a[n]
    t = 1
    while (t == 1):
        b = b+2
        i = 0
        t = 0
        while (a[i]*a[i] < b)and (t == 0):
            i=i+1
            if (b%a[i] == 0):
                t = 1

                
        if (t == 0):
            n = n+1
            a.append(b)
            
# to find out how many divisors
def dvsr(number):
    dvsrs = 1
    i = 0
    count = 0
    while number >1:
        while(number%a[i] == 0):
            count=count+1
            number = number / a[i]
            
        if count > 0:
            dvsrs = dvsrs * (count +1)
            count = 0
            
        i = i+1

    return dvsrs

    
print (dvsr(48))
    
        

            
