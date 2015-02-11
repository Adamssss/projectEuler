string = []

for i in range(0,1000000):
    string.append(0)

string[0] = 1

def collatz(n):
    N = 1000000
    global string
    global count
    if n<=N:
        if string[n-1] > 0:
            count = string[n-1]
            return

    if n%2 == 0:
        if n > N:
            collatz(n//2)
            count += 1
            
        if n <= N:
            if string[n//2-1] == 0:
                collatz(n//2)
                
            if string[n//2-1] > 0:
                string[n-1] = string[(n//2-1)] + 1
                count = string[n-1]
                return

    if n%2 == 1:
        if 3*n+1 > N:
            collatz(3*n+1)
            count += 1
            
        if 3*n+1 <= N:
            if string [3*n] == 0:
                collatz(3*n+1)
                
            if string[3*n] > 0:
                string[n-1] = string[3*n] + 1
                count = string[n-1]
                return

    if n <= N:
        string[n-1] = count
        
 
for i in range(1,1000000):
    collatz(i)

largest = 0
for i in range(0,1000000):
    if string[i] > largest:
        largest = string[i]

print (string.index(largest)+1)



    
