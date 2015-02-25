
prime = [2,3,5]
primen = 2

while prime[primen] < 7654321:
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

print (len(prime))
# 987654321 9-dig pandigital always has divisor 9
# 87654321 8-dig pandigtal also always has divisor 9

end = False
while not end:
    t = 0
    num = prime[-1]
    digs = [1,2,3,4,5,6,7]
    while num > 0:
        a = num%10
        num = num//10
        if a in digs:
            digs.remove(a)
        else:
            t = 1
    if t == 0:
        end = True
        print (prime[-1])
    else:
        prime.remove(prime[-1])
    
