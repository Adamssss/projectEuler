
def collatz(n,length):
    if n == 1:
        return length

    length += 1
    if n%2 == 0:
        return collatz(n/2,length)
    
    return collatz(3*n+1,length)

string = []
for i in range(0,1000000):
    string.append(collatz(i+1,1))

largest = 0
for i in range(0,1000000):
    if string[i] > largest:
        largest = string[i]
        print (i+1)

