
def collatz(n,length):
    if n == 1:
        return length

    length += 1
    if n%2 == 0:
        return collatz(n/2,length)
    
    return collatz(3*n+1,length)

print (collatz(13,1))

largest = 0
for i in range(0,1000000):
    length = collatz(i,1)
    if length > largest:
        largest = length

print(largest)
