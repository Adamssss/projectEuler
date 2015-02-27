import math

prime = [2,3,5]
primen = 2

while primen < 547:
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

# define a method to check if it is a prime
def isPrime(num):
    if num%2 == 0:
        return False
    i = 3
    while i < math.sqrt(num):
        if num%i == 0:
            return False
        i += 2
    return True

#  first 546 consective prime sum is the greatest less than 1 million
def sumOf(start,number):
    total = 0
    i = 0
    while i<number:
        total += prime[start+i]
        i += 1
    return total

# print(sumOf(0,546))

for i in range(0,500):
    for j in range(0,i+1):
        test = sumOf(j,546-i)
        if isPrime(test):
            break
    if isPrime(test):
        print (test)
        break   
