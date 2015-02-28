import math

def isPrime(num):
    if num%2 == 0:
        return False
    i = 3
    while i < math.sqrt(num):
        if num%i == 0:
            return False
        i += 2
    return True

print(isPrime(121313))
print(isPrime(222323))
print(isPrime(323333))
print(isPrime(424343))
print(isPrime(525353))
print(isPrime(626363))
print(isPrime(727373))
print(isPrime(828383))
print(isPrime(929393))
