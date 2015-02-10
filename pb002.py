fib = [1,2,3]
n = len(fib)
sum = 2
while fib[n-1] < 4000000:
    newfib = fib[n-2]+fib[n-1]
    fib.append(newfib)
    n = len(fib)
    if newfib%2 == 0:
        sum = sum + newfib

print (sum)
